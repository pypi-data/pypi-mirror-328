"""Test cases for CryptoManager class."""

import unittest
import os
import tempfile
from secureutils.crypto import CryptoManager
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa

class TestCryptoManager(unittest.TestCase):
    def setUp(self):
        self.crypto = CryptoManager()
        self.test_data = b"Hello, World! This is a test message."
        self.test_string = "Hello, World! This is a test message."
        self.signing_key = self.crypto.generate_signing_key(2048)
        self.public_key = self.signing_key.public_key()

    def test_encryption_algorithms(self):
        """Test all supported encryption algorithms."""
        algorithms = ['aes', 'chacha20', 'rc4', 'xor']

        for algorithm in algorithms:
            with self.subTest(algorithm=algorithm):
                # Generate appropriate key size for the algorithm
                key_size = 32 if algorithm in ['aes', 'chacha20'] else 16
                key = self.crypto.generate_key(algorithm, key_size)

                # Test byte encryption/decryption
                encrypted = self.crypto.encrypt_bytes(self.test_data, key, algorithm)
                decrypted = self.crypto.decrypt_bytes(encrypted, key, algorithm)
                self.assertEqual(decrypted, self.test_data)

                # Test string encryption/decryption
                encrypted_str = self.crypto.encrypt_string(self.test_string, key, algorithm)
                decrypted_str = self.crypto.decrypt_string(encrypted_str, key, algorithm)
                self.assertEqual(decrypted_str, self.test_string)

                # Verify that encryption produces different output for same input
                if algorithm != 'xor' and algorithm != 'rc4':  # These are deterministic
                    encrypted2 = self.crypto.encrypt_bytes(self.test_data, key, algorithm)
                    self.assertNotEqual(encrypted, encrypted2)

    def test_digital_signature_generation(self):
        """Test RSA key generation and digital signatures."""
        # Test key generation
        self.assertIsInstance(self.signing_key, rsa.RSAPrivateKey)
        self.assertEqual(self.signing_key.key_size, 2048)

        # Test data signing and verification
        signature = self.crypto.sign_data(self.test_data, self.signing_key)
        self.assertTrue(
            self.crypto.verify_signature(self.test_data, signature, self.public_key)
        )

        # Test with different hash algorithms
        hash_algorithms = {
            'sha256': hashes.SHA256(),
            'sha384': hashes.SHA384(),
            'sha512': hashes.SHA512()
        }

        for name, hash_algo in hash_algorithms.items():
            signature = self.crypto.sign_data(
                self.test_data,
                self.signing_key,
                hash_algorithm=hash_algo
            )
            self.assertTrue(
                self.crypto.verify_signature(
                    self.test_data,
                    signature,
                    self.public_key,
                    hash_algorithm=hash_algo
                )
            )

    def test_string_signature(self):
        """Test string signing and verification."""
        # Test normal signing and verification
        signature = self.crypto.sign_string(self.test_string, self.signing_key)
        self.assertTrue(
            self.crypto.verify_string_signature(
                self.test_string,
                signature,
                self.public_key
            )
        )

        # Test invalid signature
        self.assertFalse(
            self.crypto.verify_string_signature(
                self.test_string + "modified",
                signature,
                self.public_key
            )
        )

    def test_file_signature(self):
        """Test file signing and verification."""
        sig_path = None  # Initialize sig_path
        with tempfile.NamedTemporaryFile(delete=False) as test_file:
            test_file.write(self.test_data)
            test_file.flush()

            try:
                # Sign the file
                sig_path = self.crypto.sign_file(
                    test_file.name,
                    self.signing_key
                )
                self.assertTrue(os.path.exists(sig_path))

                # Verify valid signature
                self.assertTrue(
                    self.crypto.verify_file_signature(
                        test_file.name,
                        sig_path,
                        self.public_key
                    )
                )

                # Modify file and verify it fails
                with open(test_file.name, 'ab') as f:
                    f.write(b"modified")
                self.assertFalse(
                    self.crypto.verify_file_signature(
                        test_file.name,
                        sig_path,
                        self.public_key
                    )
                )

            finally:
                # Clean up
                os.unlink(test_file.name)
                if sig_path and os.path.exists(sig_path):
                    os.unlink(sig_path)

    def test_invalid_hash_algorithm(self):
        """Test error handling for invalid hash algorithms."""
        with self.assertRaises(ValueError):
            self.crypto.sign_data(
                self.test_data,
                self.signing_key,
                hash_algorithm=None  # This will raise ValueError
            )

    def test_key_validation(self):
        """Test key size validation for different algorithms."""
        test_cases = [
            ('aes', 16, True),    # AES-128
            ('aes', 24, True),    # AES-192
            ('aes', 32, True),    # AES-256
            ('aes', 15, False),   # Invalid AES key size
            ('des', 24, True),    # Triple DES
            ('des', 16, False),   # Invalid Triple DES key size
            ('chacha20', 32, True),  # ChaCha20
            ('chacha20', 16, False), # Invalid ChaCha20 key size
            ('rc4', 16, True),    # RC4
            ('rc4', 24, True),    # RC4
            ('rc4', 32, True),    # RC4
            ('xor', 8, True),     # XOR supports any key size
            ('xor', 16, True),
            ('xor', 32, True),
        ]

        for algorithm, key_size, expected in test_cases:
            with self.subTest(algorithm=algorithm, key_size=key_size):
                key = os.urandom(key_size)
                result = self.crypto.validate_key_size(algorithm, key)
                self.assertEqual(result, expected, 
                    f"Key validation failed for {algorithm} with size {key_size}")

    def test_invalid_algorithm(self):
        """Test error handling for invalid algorithms."""
        key = self.crypto.generate_key('aes', 32)
        with self.assertRaises(ValueError):
            self.crypto.encrypt_bytes(self.test_data, key, 'invalid_algorithm')

    def test_file_encryption(self):
        """Test file encryption and decryption."""
        algorithms = ['aes', 'chacha20', 'rc4', 'xor']

        for algorithm in algorithms:
            with self.subTest(algorithm=algorithm):
                # Create temporary files
                with tempfile.NamedTemporaryFile(delete=False) as input_file, \
                     tempfile.NamedTemporaryFile(delete=False) as encrypted_file, \
                     tempfile.NamedTemporaryFile(delete=False) as decrypted_file:

                    # Write test data
                    input_file.write(self.test_data)
                    input_file.flush()

                    # Generate key
                    key_size = 32 if algorithm in ['aes', 'chacha20'] else 16
                    key = self.crypto.generate_key(algorithm, key_size)

                    try:
                        # Encrypt file
                        self.crypto.encrypt_file(
                            input_file.name,
                            encrypted_file.name,
                            key,
                            algorithm
                        )

                        # Decrypt file
                        self.crypto.decrypt_file(
                            encrypted_file.name,
                            decrypted_file.name,
                            key,
                            algorithm
                        )

                        # Verify content
                        with open(decrypted_file.name, 'rb') as f:
                            decrypted_content = f.read()
                            self.assertEqual(decrypted_content, self.test_data)

                    finally:
                        # Clean up
                        os.unlink(input_file.name)
                        os.unlink(encrypted_file.name)
                        os.unlink(decrypted_file.name)

    def test_key_generation(self):
        """Test key generation for different sizes."""
        # Test valid key sizes
        for algorithm, size in [
            ('aes', 16), ('aes', 24), ('aes', 32),
            ('chacha20', 32),
            ('rc4', 16), ('rc4', 24), ('rc4', 32),
            ('xor', 8), ('xor', 16), ('xor', 32)
        ]:
            with self.subTest(algorithm=algorithm, size=size):
                key = self.crypto.generate_key(algorithm, size)
                self.assertEqual(len(key), size)

        # Test invalid key sizes
        with self.assertRaises(ValueError):
            self.crypto.generate_key('aes', 15)
        with self.assertRaises(ValueError):
            self.crypto.generate_key('des', 16) #This line remains because it is testing for an error
        with self.assertRaises(ValueError):
            self.crypto.generate_key('invalid_algorithm', 32)

if __name__ == '__main__':
    unittest.main()