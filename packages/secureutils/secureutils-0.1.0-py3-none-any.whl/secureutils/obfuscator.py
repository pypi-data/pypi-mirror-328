"""
Code obfuscation utility for Python source code.
"""

import ast
import random
import string
import base64
import codecs
from typing import Dict, Set
import logging
import astor  # For Python 3.8 compatibility

logger = logging.getLogger(__name__)

class NameGenerator:
    def __init__(self):
        """Initialize name generator for obfuscation."""
        self.used_names: Set[str] = set()
        self._counter = 0
        self._preserved = {
            '__name__', '__main__', '__init__', '__file__',
            'self', 'cls', 'super', 'True', 'False', 'None',
            'Exception', 'BaseException', 'object', '_decode_str',
            'print', 'exec', 'result'  # Add common built-ins and test variables
        }

    def generate(self, length: int = 8) -> str:
        """Generate a unique obfuscated name."""
        while True:
            name = f"_{self._counter}_{''.join(random.choices(string.ascii_letters, k=length))}"
            self._counter += 1
            if name not in self.used_names and name not in self._preserved:
                self.used_names.add(name)
                return name

class Obfuscator(ast.NodeTransformer):
    """Python code obfuscator."""

    def __init__(self):
        """Initialize code obfuscator."""
        super().__init__()
        self.name_generator = NameGenerator()
        self.name_map: Dict[str, str] = {}

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.AST:
        """Handle class definitions."""
        if node.name not in self.name_generator._preserved:
            if node.name not in self.name_map:
                self.name_map[node.name] = self.name_generator.generate()
            node.name = self.name_map[node.name]
        return self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        """Handle function definitions."""
        if node.name not in self.name_generator._preserved:
            if node.name not in self.name_map:
                self.name_map[node.name] = self.name_generator.generate()
            node.name = self.name_map[node.name]
        return self.generic_visit(node)

    def visit_Name(self, node: ast.Name) -> ast.AST:
        """Handle variable names."""
        if node.id in self.name_generator._preserved:
            return node

        if isinstance(node.ctx, ast.Store):
            if node.id not in self.name_map:
                self.name_map[node.id] = self.name_generator.generate()

        if node.id in self.name_map:
            node.id = self.name_map[node.id]
        return node

    def visit_Str(self, node: ast.Str) -> ast.AST:
        """Handle string literals (Python < 3.8)."""
        if len(node.s) > 0:
            # Use base64 for better compatibility
            encoded = base64.b64encode(node.s.encode()).decode()
            return ast.Call(
                func=ast.Name(id='_decode_str', ctx=ast.Load()),
                args=[ast.Constant(value=encoded) if hasattr(ast, 'Constant') else ast.Str(s=encoded)],
                keywords=[]
            )
        return node

    def visit_Constant(self, node: ast.Constant) -> ast.AST:
        """Handle string literals (Python 3.8+)."""
        if isinstance(node.value, str) and len(node.value) > 0:
            # Use base64 for better compatibility
            encoded = base64.b64encode(node.value.encode()).decode()
            return ast.Call(
                func=ast.Name(id='_decode_str', ctx=ast.Load()),
                args=[ast.Constant(value=encoded)],
                keywords=[]
            )
        return node

    def obfuscate(self, source_code: str) -> str:
        """
        Obfuscate Python source code.

        Args:
            source_code: Source code to obfuscate

        Returns:
            str: Obfuscated source code
        """
        try:
            # Parse source code into AST
            tree = ast.parse(source_code)

            # Add string decoder function at the beginning
            decoder_func = ast.parse('''
def _decode_str(s):
    import base64
    return base64.b64decode(s.encode()).decode()
''').body[0]

            # Transform the AST
            transformed = self.visit(tree)

            # Insert decoder function at the beginning
            transformed.body.insert(0, decoder_func)

            # Fix missing locations
            ast.fix_missing_locations(transformed)

            # Convert AST back to source code using astor
            return astor.to_source(transformed)

        except Exception as e:
            logger.error(f"Obfuscation failed: {str(e)}")
            raise

def obfuscate_file(input_path: str, output_path: str):
    """
    Obfuscate a Python source file.

    Args:
        input_path: Input file path
        output_path: Output file path
    """
    try:
        with open(input_path, 'r') as f:
            source = f.read()

        obfuscator = Obfuscator()
        obfuscated_code = obfuscator.obfuscate(source)

        with open(output_path, 'w') as f:
            f.write(obfuscated_code)

    except Exception as e:
        logger.error(f"File obfuscation failed: {str(e)}")
        raise