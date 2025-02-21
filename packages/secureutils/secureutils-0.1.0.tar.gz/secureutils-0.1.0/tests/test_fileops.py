import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
from secureutils.fileops import FileManager
import tempfile
import shutil

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.manager = FileManager(self.temp_dir)
        
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
        
    def test_create_directory(self):
        test_dir = "test_dir"
        created_path = self.manager.create_directory(test_dir)
        self.assertTrue(created_path.exists())
        self.assertTrue(created_path.is_dir())
        
    def test_list_files(self):
        # Create test files
        Path(self.temp_dir, "test1.txt").touch()
        Path(self.temp_dir, "test2.txt").touch()
        
        files = self.manager.list_files(".", "*.txt")
        self.assertEqual(len(files), 2)
        
    def test_secure_delete(self):
        test_file = Path(self.temp_dir, "test.txt")
        test_file.touch()
        
        self.manager.secure_delete(test_file)
        self.assertFalse(test_file.exists())
        
    def test_copy_file(self):
        source = Path(self.temp_dir, "source.txt")
        source.write_text("test content")
        
        dest = Path(self.temp_dir, "dest.txt")
        self.manager.copy_file(source, dest)
        
        self.assertTrue(dest.exists())
        self.assertEqual(dest.read_text(), "test content")

if __name__ == '__main__':
    unittest.main()
