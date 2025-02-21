"""
File and folder operations utility with secure handling and type checking.
"""

import os
import shutil
from typing import List, Optional, Union
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class FileManager:
    def __init__(self, base_path: Optional[str] = None):
        """
        Initialize FileManager with optional base path.
        
        Args:
            base_path (str): Base directory for all operations
        """
        self.base_path = Path(base_path) if base_path else Path.cwd()
        
    def _ensure_path(self, path: Union[str, Path]) -> Path:
        """Convert string path to Path object and ensure it's absolute."""
        path = Path(path)
        return path if path.is_absolute() else self.base_path / path
        
    def create_directory(self, path: Union[str, Path], exist_ok: bool = True) -> Path:
        """
        Create a directory and return its Path object.
        
        Args:
            path: Directory path to create
            exist_ok: If False, raise error when directory exists
            
        Returns:
            Path: Created directory path
        """
        path = self._ensure_path(path)
        try:
            path.mkdir(parents=True, exist_ok=exist_ok)
            return path
        except Exception as e:
            logger.error(f"Failed to create directory {path}: {str(e)}")
            raise
            
    def list_files(self, path: Union[str, Path], pattern: str = "*") -> List[Path]:
        """
        List all files in a directory matching the pattern.
        
        Args:
            path: Directory to list
            pattern: Glob pattern for filtering
            
        Returns:
            List[Path]: List of matching file paths
        """
        path = self._ensure_path(path)
        try:
            return list(path.glob(pattern))
        except Exception as e:
            logger.error(f"Failed to list files in {path}: {str(e)}")
            raise
            
    def secure_delete(self, path: Union[str, Path]) -> None:
        """
        Securely delete a file or directory.
        
        Args:
            path: Path to delete
        """
        path = self._ensure_path(path)
        try:
            if path.is_file():
                # Overwrite file with zeros before deletion
                with open(path, 'wb') as f:
                    f.write(b'\x00' * path.stat().st_size)
                path.unlink()
            elif path.is_dir():
                shutil.rmtree(path)
        except Exception as e:
            logger.error(f"Failed to delete {path}: {str(e)}")
            raise
            
    def copy_file(
        self,
        source: Union[str, Path],
        destination: Union[str, Path],
        overwrite: bool = False
    ) -> Path:
        """
        Copy a file with optional overwrite.
        
        Args:
            source: Source file path
            destination: Destination file path
            overwrite: Whether to overwrite existing files
            
        Returns:
            Path: Destination path
        """
        source = self._ensure_path(source)
        destination = self._ensure_path(destination)
        
        try:
            if not overwrite and destination.exists():
                raise FileExistsError(f"Destination file {destination} already exists")
                
            shutil.copy2(source, destination)
            return destination
        except Exception as e:
            logger.error(f"Failed to copy {source} to {destination}: {str(e)}")
            raise
