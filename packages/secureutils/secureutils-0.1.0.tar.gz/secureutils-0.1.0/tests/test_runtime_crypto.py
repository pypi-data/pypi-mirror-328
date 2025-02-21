"""Test cases for runtime function encryption."""

import unittest
from secureutils.crypto import CryptoManager, RuntimeEncryption, encrypted_function

class TestRuntimeEncryption(unittest.TestCase):
    def setUp(self):
        self.crypto_manager = CryptoManager()
        self.runtime_encryption = RuntimeEncryption(self.crypto_manager)
    
    def test_function_encryption(self):
        """Test basic function encryption and execution."""
        @encrypted_function(self.runtime_encryption)
        def test_func(x, y):
            return x + y
        
        # Test function execution
        result = test_func(5, 3)
        self.assertEqual(result, 8)
    
    def test_complex_function(self):
        """Test encryption of more complex function."""
        @encrypted_function(self.runtime_encryption)
        def complex_func(data):
            processed = []
            for item in data:
                if isinstance(item, int):
                    processed.append(item * 2)
                elif isinstance(item, str):
                    processed.append(item.upper())
            return processed
        
        test_data = [1, "hello", 3, "world"]
        expected = [2, "HELLO", 6, "WORLD"]
        result = complex_func(test_data)
        self.assertEqual(result, expected)
    
    def test_function_cleanup(self):
        """Test that decrypted functions are cleaned up."""
        @encrypted_function(self.runtime_encryption)
        def cleanup_test():
            return "test"
        
        # Execute function
        cleanup_test()
        
        # Verify cleanup
        func_id = f"cleanup_test_{id(cleanup_test)}"
        self.assertNotIn(func_id, self.runtime_encryption._decrypted_functions)
    
    def test_encryption_key_management(self):
        """Test that different keys produce different results."""
        # Create two RuntimeEncryption instances with different keys
        runtime1 = RuntimeEncryption(self.crypto_manager)
        runtime2 = RuntimeEncryption(self.crypto_manager)
        
        def sample_func():
            return "test"
        
        # Encrypt the same function with different keys
        encrypted1 = runtime1.encrypt_function(sample_func)
        encrypted2 = runtime2.encrypt_function(sample_func)
        
        # Verify different encryptions
        self.assertNotEqual(encrypted1, encrypted2)

if __name__ == '__main__':
    unittest.main()
