import unittest
import ast
from secureutils.obfuscator import Obfuscator, obfuscate_file
import tempfile
import os

class TestObfuscator(unittest.TestCase):
    def setUp(self):
        self.obfuscator = Obfuscator()
        self.test_code = '''
def greet(name):
    message = "Hello, " + name
    return message

result = greet("World")
'''

    def test_name_obfuscation(self):
        obfuscated = self.obfuscator.obfuscate(self.test_code)
        
        # Original names should not appear in obfuscated code
        self.assertNotIn('greet', obfuscated)
        self.assertNotIn('message', obfuscated)
        
        # But functionality should remain
        namespace = {}
        exec(obfuscated, namespace)
        self.assertIn('result', namespace)
        self.assertEqual(namespace['result'], 'Hello, World')

    def test_string_encryption(self):
        obfuscated = self.obfuscator.obfuscate('x = "test string"')
        
        # Original string should not appear in obfuscated code
        self.assertNotIn('test string', obfuscated)
        
        # But functionality should remain
        namespace = {}
        exec(obfuscated, namespace)
        self.assertEqual(namespace['x'], 'test string')

    def test_file_obfuscation(self):
        # Create temporary files
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as input_file:
            input_file.write(self.test_code)
            input_path = input_file.name

        output_path = input_path + '.obf'
        
        try:
            # Obfuscate the file
            obfuscate_file(input_path, output_path)
            
            # Check if output file exists and is different from input
            self.assertTrue(os.path.exists(output_path))
            with open(output_path, 'r') as f:
                obfuscated_content = f.read()
            
            self.assertNotEqual(self.test_code, obfuscated_content)
            
            # Test if obfuscated code runs
            namespace = {}
            exec(obfuscated_content, namespace)
            self.assertEqual(namespace['result'], 'Hello, World')
            
        finally:
            # Clean up
            os.unlink(input_path)
            if os.path.exists(output_path):
                os.unlink(output_path)

if __name__ == '__main__':
    unittest.main()
