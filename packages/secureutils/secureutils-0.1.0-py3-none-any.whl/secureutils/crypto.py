"""
Encryption and decryption utility supporting multiple algorithms and digital signatures.
Includes runtime function encryption capabilities.
"""

import os
import marshal
import types
import functools
from typing import Union, Optional, Dict, Literal, Callable, Any
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asymmetric_padding
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
import base64
import logging

logger = logging.getLogger(__name__)

HashAlgorithm = Union[hashes.HashAlgorithm, Literal['sha256', 'sha384', 'sha512']]

class CryptoManager:
    """Handles encryption/decryption operations and digital signatures."""

    def __init__(self):
        self.backend = default_backend()
        self._algorithm_key_sizes = {
            'aes': [16, 24, 32],  # AES-128, AES-192, AES-256
            'chacha20': [32],     # ChaCha20 requires 32 bytes
            'rc4': [16, 24, 32],  # RC4 supports variable key sizes
            'xor': None,          # XOR supports any key size
            'des': [24]           # Triple DES (24 bytes)
        }
        self._hash_algorithms = {
            'sha256': hashes.SHA256(),
            'sha384': hashes.SHA384(),
            'sha512': hashes.SHA512()
        }

    def generate_signing_key(self, key_size: int = 2048) -> rsa.RSAPrivateKey:
        """
        Generate an RSA key pair for digital signatures.

        Args:
            key_size: Size of the RSA key in bits (default: 2048)

        Returns:
            RSAPrivateKey: Generated private key
        """
        return rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=self.backend
        )

    def _get_hash_algorithm(self, hash_algorithm: HashAlgorithm) -> hashes.HashAlgorithm:
        """Get the hash algorithm instance."""
        if isinstance(hash_algorithm, hashes.HashAlgorithm):
            return hash_algorithm
        elif isinstance(hash_algorithm, str):
            hash_algo = self._hash_algorithms.get(hash_algorithm.lower())
            if not hash_algo:
                raise ValueError(f"Unsupported hash algorithm: {hash_algorithm}")
            return hash_algo
        else:
            raise ValueError("Invalid hash algorithm type")

    def sign_data(
        self,
        data: bytes,
        private_key: rsa.RSAPrivateKey,
        hash_algorithm: HashAlgorithm = 'sha256'
    ) -> bytes:
        """
        Sign data using RSA-PSS and the specified hash algorithm.

        Args:
            data: Data to sign
            private_key: RSA private key for signing
            hash_algorithm: Hash algorithm to use

        Returns:
            bytes: Digital signature
        """
        try:
            if hash_algorithm is None:
                raise ValueError("Hash algorithm cannot be None")

            hash_algo = self._get_hash_algorithm(hash_algorithm)

            signature = private_key.sign(
                data,
                asymmetric_padding.PSS(
                    mgf=asymmetric_padding.MGF1(hash_algo),
                    salt_length=asymmetric_padding.PSS.MAX_LENGTH
                ),
                hash_algo
            )
            return signature
        except Exception as e:
            logger.error(f"Signing failed: {str(e)}")
            raise

    def verify_signature(
        self,
        data: bytes,
        signature: bytes,
        public_key: rsa.RSAPublicKey,
        hash_algorithm: HashAlgorithm = 'sha256'
    ) -> bool:
        """
        Verify a digital signature.

        Args:
            data: Original data
            signature: Signature to verify
            public_key: RSA public key for verification
            hash_algorithm: Hash algorithm used in signing

        Returns:
            bool: True if signature is valid
        """
        try:
            hash_algo = self._get_hash_algorithm(hash_algorithm)
            public_key.verify(
                signature,
                data,
                asymmetric_padding.PSS(
                    mgf=asymmetric_padding.MGF1(hash_algo),
                    salt_length=asymmetric_padding.PSS.MAX_LENGTH
                ),
                hash_algo
            )
            return True
        except InvalidSignature:
            return False
        except Exception as e:
            logger.error(f"Signature verification failed: {str(e)}")
            raise

    def sign_string(
        self,
        text: str,
        private_key: rsa.RSAPrivateKey,
        hash_algorithm: HashAlgorithm = 'sha256',
        encoding: str = 'utf-8'
    ) -> str:
        """
        Sign a string and return base64 encoded signature.

        Args:
            text: String to sign
            private_key: RSA private key for signing
            hash_algorithm: Hash algorithm to use
            encoding: String encoding

        Returns:
            str: Base64 encoded signature
        """
        try:
            data = text.encode(encoding)
            signature = self.sign_data(data, private_key, hash_algorithm)
            return base64.b64encode(signature).decode('ascii')
        except Exception as e:
            logger.error(f"String signing failed: {str(e)}")
            raise

    def verify_string_signature(
        self,
        text: str,
        signature: str,
        public_key: rsa.RSAPublicKey,
        hash_algorithm: HashAlgorithm = 'sha256',
        encoding: str = 'utf-8'
    ) -> bool:
        """
        Verify a base64 encoded signature for a string.

        Args:
            text: Original string
            signature: Base64 encoded signature
            public_key: RSA public key for verification
            hash_algorithm: Hash algorithm used in signing
            encoding: String encoding

        Returns:
            bool: True if signature is valid
        """
        try:
            data = text.encode(encoding)
            sig_bytes = base64.b64decode(signature.encode('ascii'))
            return self.verify_signature(data, sig_bytes, public_key, hash_algorithm)
        except Exception as e:
            logger.error(f"String signature verification failed: {str(e)}")
            return False

    def sign_file(
        self,
        file_path: str,
        private_key: rsa.RSAPrivateKey,
        signature_path: Optional[str] = None,
        hash_algorithm: HashAlgorithm = 'sha256',
        chunk_size: int = 64 * 1024
    ) -> str:
        """
        Sign a file and save the signature.

        Args:
            file_path: Path to file to sign
            private_key: RSA private key for signing
            signature_path: Path to save signature (default: file_path + '.sig')
            hash_algorithm: Hash algorithm to use
            chunk_size: Size of chunks to read

        Returns:
            str: Path to the signature file
        """
        try:
            # Hash the file contents
            hash_algo = self._get_hash_algorithm(hash_algorithm)
            hasher = hashes.Hash(hash_algo)
            with open(file_path, 'rb') as f:
                while chunk := f.read(chunk_size):
                    hasher.update(chunk)
            file_hash = hasher.finalize()

            # Sign the hash
            signature = self.sign_data(file_hash, private_key, hash_algorithm)

            # Save the signature
            if signature_path is None:
                signature_path = f"{file_path}.sig"

            with open(signature_path, 'wb') as f:
                f.write(signature)

            return signature_path

        except Exception as e:
            logger.error(f"File signing failed: {str(e)}")
            raise

    def verify_file_signature(
        self,
        file_path: str,
        signature_path: str,
        public_key: rsa.RSAPublicKey,
        hash_algorithm: HashAlgorithm = 'sha256',
        chunk_size: int = 64 * 1024
    ) -> bool:
        """
        Verify a file's signature.

        Args:
            file_path: Path to the original file
            signature_path: Path to the signature file
            public_key: RSA public key for verification
            hash_algorithm: Hash algorithm used in signing
            chunk_size: Size of chunks to read

        Returns:
            bool: True if signature is valid
        """
        try:
            # Hash the file contents
            hash_algo = self._get_hash_algorithm(hash_algorithm)
            hasher = hashes.Hash(hash_algo)
            with open(file_path, 'rb') as f:
                while chunk := f.read(chunk_size):
                    hasher.update(chunk)
            file_hash = hasher.finalize()

            # Read the signature
            with open(signature_path, 'rb') as f:
                signature = f.read()

            # Verify the signature
            return self.verify_signature(file_hash, signature, public_key, hash_algorithm)

        except Exception as e:
            logger.error(f"File signature verification failed: {str(e)}")
            return False

    def validate_key_size(self, algorithm: str, key: bytes) -> bool:
        """
        Validate key size for the specified algorithm.

        Args:
            algorithm: Algorithm name
            key: Encryption/decryption key

        Returns:
            bool: True if key size is valid
        """
        valid_sizes = self._algorithm_key_sizes.get(algorithm.lower())
        if valid_sizes is None:  # For XOR
            return True
        return len(key) in valid_sizes

    def generate_key(self, algorithm: str, size: Optional[int] = None) -> bytes:
        """
        Generate a random key for the specified algorithm.

        Args:
            algorithm: Algorithm name ('aes', 'des', 'chacha20', 'rc4', 'xor')
            size: Key size in bytes, if not provided uses minimum valid size

        Returns:
            bytes: Generated key

        Raises:
            ValueError: If algorithm or key size is invalid
        """
        algorithm = algorithm.lower()
        valid_sizes = self._algorithm_key_sizes.get(algorithm)

        if algorithm not in self._algorithm_key_sizes:
            raise ValueError(f"Unsupported algorithm: {algorithm}")

        if valid_sizes and size and size not in valid_sizes:
            raise ValueError(
                f"Invalid key size for {algorithm}. Valid sizes: {valid_sizes}"
            )

        size = size or (valid_sizes[0] if valid_sizes else 32)
        return os.urandom(size)

    def _pad_data(self, data: bytes, block_size: int) -> bytes:
        """Add PKCS7 padding to data."""
        padder = padding.PKCS7(block_size * 8).padder()
        return padder.update(data) + padder.finalize()

    def _unpad_data(self, data: bytes, block_size: int) -> bytes:
        """Remove PKCS7 padding from data."""
        unpadder = padding.PKCS7(block_size * 8).unpadder()
        return unpadder.update(data) + unpadder.finalize()

    def _rc4_transform(self, data: bytes, key: bytes) -> bytes:
        """RC4 encryption/decryption implementation."""
        S = list(range(256))
        j = 0

        # Key-scheduling algorithm (KSA)
        for i in range(256):
            j = (j + S[i] + key[i % len(key)]) % 256
            S[i], S[j] = S[j], S[i]

        # Pseudo-random generation algorithm (PRGA)
        i = j = 0
        result = bytearray()

        for byte in data:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            k = S[(S[i] + S[j]) % 256]
            result.append(byte ^ k)

        return bytes(result)

    def encrypt_bytes(
        self,
        data: bytes,
        key: bytes,
        algorithm: str = 'aes',
        **kwargs
    ) -> bytes:
        """
        Encrypt bytes using the specified algorithm.

        Args:
            data: Data to encrypt
            key: Encryption key
            algorithm: Algorithm to use ('aes', 'chacha20', 'rc4', 'xor')
            **kwargs: Additional algorithm-specific parameters

        Returns:
            bytes: Encrypted data

        Raises:
            ValueError: If algorithm is not supported or key size is invalid
        """
        if not isinstance(data, bytes) or not isinstance(key, bytes):
            raise ValueError("Data and key must be bytes")

        algorithm = algorithm.lower()
        if not self.validate_key_size(algorithm, key):
            raise ValueError(
                f"Invalid key size for {algorithm}. Required sizes: "
                f"{self._algorithm_key_sizes[algorithm]}"
            )

        try:
            if algorithm == 'rc4':
                return self._rc4_transform(data, key)

            elif algorithm == 'xor':
                return bytes(a ^ b for a, b in zip(
                    data,
                    key * (len(data) // len(key) + 1)
                ))

            iv = os.urandom(16)  # Generate IV for CBC mode

            if algorithm == 'aes':
                padded_data = self._pad_data(data, 16)
                cipher = Cipher(
                    algorithms.AES(key),
                    modes.CBC(iv),
                    backend=self.backend
                )
                encryptor = cipher.encryptor()
                return iv + encryptor.update(padded_data) + encryptor.finalize()

            elif algorithm == 'chacha20':
                nonce = os.urandom(16)
                cipher = Cipher(
                    algorithms.ChaCha20(key, nonce),
                    None,
                    backend=self.backend
                )
                return nonce + cipher.encryptor().update(data)

            elif algorithm == 'des':
                iv = os.urandom(8)
                cipher = Cipher(
                    algorithms.TripleDES(key),
                    modes.CBC(iv),
                    backend=self.backend
                )
                encryptor = cipher.encryptor()
                padded_data = self._pad_data(data, 8)
                return iv + encryptor.update(padded_data) + encryptor.finalize()

            raise ValueError(f"Unsupported algorithm: {algorithm}")

        except Exception as e:
            logger.error(f"Encryption failed: {str(e)}")
            raise

    def decrypt_bytes(
        self,
        encrypted_data: bytes,
        key: bytes,
        algorithm: str = 'aes',
        **kwargs
    ) -> bytes:
        """
        Decrypt bytes using the specified algorithm.

        Args:
            encrypted_data: Data to decrypt
            key: Decryption key
            algorithm: Algorithm to use
            **kwargs: Additional algorithm-specific parameters

        Returns:
            bytes: Decrypted data
        """
        algorithm = algorithm.lower()
        if not self.validate_key_size(algorithm, key):
            raise ValueError(
                f"Invalid key size for {algorithm}. Required sizes: "
                f"{self._algorithm_key_sizes[algorithm]}"
            )

        try:
            if algorithm == 'rc4':
                return self._rc4_transform(encrypted_data, key)

            elif algorithm == 'xor':
                return bytes(a ^ b for a, b in zip(
                    encrypted_data,
                    key * (len(encrypted_data) // len(key) + 1)
                ))

            elif algorithm == 'aes':
                iv, ciphertext = encrypted_data[:16], encrypted_data[16:]
                cipher = Cipher(
                    algorithms.AES(key),
                    modes.CBC(iv),
                    backend=self.backend
                )
                decryptor = cipher.decryptor()
                padded_data = decryptor.update(ciphertext) + decryptor.finalize()
                return self._unpad_data(padded_data, 16)

            elif algorithm == 'chacha20':
                nonce, ciphertext = encrypted_data[:16], encrypted_data[16:]
                cipher = Cipher(
                    algorithms.ChaCha20(key, nonce),
                    None,
                    backend=self.backend
                )
                return cipher.decryptor().update(ciphertext)
            
            elif algorithm == 'des':
                iv, ciphertext = encrypted_data[:8], encrypted_data[8:]
                cipher = Cipher(
                    algorithms.TripleDES(key),
                    modes.CBC(iv),
                    backend=self.backend
                )
                decryptor = cipher.decryptor()
                padded_data = decryptor.update(ciphertext) + decryptor.finalize()
                return self._unpad_data(padded_data, 8)

            raise ValueError(f"Unsupported algorithm: {algorithm}")

        except Exception as e:
            logger.error(f"Decryption failed: {str(e)}")
            raise

    def encrypt_string(
        self,
        text: str,
        key: bytes,
        algorithm: str = 'aes',
        encoding: str = 'utf-8'
    ) -> str:
        """
        Encrypt a string and return base64 encoded result.

        Args:
            text: String to encrypt
            key: Encryption key
            algorithm: Algorithm to use
            encoding: String encoding

        Returns:
            str: Base64 encoded encrypted string
        """
        try:
            data = text.encode(encoding)
            encrypted = self.encrypt_bytes(data, key, algorithm)
            return base64.b64encode(encrypted).decode('ascii')
        except Exception as e:
            logger.error(f"String encryption failed: {str(e)}")
            raise

    def decrypt_string(
        self,
        encrypted_text: str,
        key: bytes,
        algorithm: str = 'aes',
        encoding: str = 'utf-8'
    ) -> str:
        """
        Decrypt a base64 encoded encrypted string.

        Args:
            encrypted_text: Base64 encoded encrypted string
            key: Decryption key
            algorithm: Algorithm to use
            encoding: String encoding

        Returns:
            str: Decrypted string
        """
        try:
            encrypted_data = base64.b64decode(encrypted_text.encode('ascii'))
            decrypted = self.decrypt_bytes(encrypted_data, key, algorithm)
            return decrypted.decode(encoding)
        except Exception as e:
            logger.error(f"String decryption failed: {str(e)}")
            raise

    def encrypt_file(
        self,
        input_path: str,
        output_path: str,
        key: bytes,
        algorithm: str = 'aes',
        chunk_size: int = 64 * 1024
    ):
        """
        Encrypt a file.

        Args:
            input_path: Path to input file
            output_path: Path to save encrypted file
            key: Encryption key
            algorithm: Algorithm to use
            chunk_size: Size of chunks to process
        """
        try:
            with open(input_path, 'rb') as in_file, open(output_path, 'wb') as out_file:
                while True:
                    chunk = in_file.read(chunk_size)
                    if not chunk:
                        break
                    encrypted_chunk = self.encrypt_bytes(chunk, key, algorithm)
                    out_file.write(encrypted_chunk)
        except Exception as e:
            logger.error(f"File encryption failed: {str(e)}")
            raise

    def decrypt_file(
        self,
        input_path: str,
        output_path: str,
        key: bytes,
        algorithm: str = 'aes',
        chunk_size: int = 64 * 1024
    ):
        """
        Decrypt a file.

        Args:
            input_path: Path to encrypted file
            output_path: Path to save decrypted file
            key: Decryption key
            algorithm: Algorithm to use
            chunk_size: Size of chunks to process
        """
        try:
            with open(input_path, 'rb') as in_file, open(output_path, 'wb') as out_file:
                while True:
                    chunk = in_file.read(chunk_size)
                    if not chunk:
                        break
                    decrypted_chunk = self.decrypt_bytes(chunk, key, algorithm)
                    out_file.write(decrypted_chunk)
        except Exception as e:
            logger.error(f"File decryption failed: {str(e)}")
            raise


class RuntimeEncryption:
    """Handles runtime encryption and decryption of function bytecode."""

    def __init__(self, crypto_manager: 'CryptoManager', key: Optional[bytes] = None):
        """
        Initialize runtime encryption.

        Args:
            crypto_manager: Instance of CryptoManager for encryption operations
            key: Optional encryption key. If not provided, generates a new one
        """
        self.crypto_manager = crypto_manager
        self._key = key or crypto_manager.generate_key('aes', 32)
        self._decrypted_functions = {}

    def encrypt_function(self, func: Callable) -> bytes:
        """
        Encrypt a function's bytecode.

        Args:
            func: Function to encrypt

        Returns:
            bytes: Encrypted function bytecode
        """
        # Serialize function's code object
        code_bytes = marshal.dumps(func.__code__)

        # Encrypt the serialized bytecode
        return self.crypto_manager.encrypt_bytes(code_bytes, self._key, 'aes')

    def decrypt_function(self, encrypted_bytes: bytes, func_globals: dict) -> Callable:
        """
        Decrypt and reconstruct a function from encrypted bytecode.

        Args:
            encrypted_bytes: Encrypted function bytecode
            func_globals: Global namespace for the function

        Returns:
            Callable: Decrypted function
        """
        try:
            # Decrypt the bytecode
            decrypted_bytes = self.crypto_manager.decrypt_bytes(
                encrypted_bytes, 
                self._key, 
                'aes'
            )

            # Reconstruct code object
            code_obj = marshal.loads(decrypted_bytes)

            # Rebuild function
            return types.FunctionType(code_obj, func_globals)

        except Exception as e:
            logging.error(f"Function decryption failed: {str(e)}")
            raise

    def cleanup_function(self, func_id: str):
        """
        Clean up a decrypted function.

        Args:
            func_id: Identifier for the decrypted function
        """
        if func_id in self._decrypted_functions:
            del self._decrypted_functions[func_id]

def encrypted_function(runtime_encryption: RuntimeEncryption):
    """
    Decorator for runtime function encryption.

    Args:
        runtime_encryption: RuntimeEncryption instance for encryption/decryption

    Returns:
        Callable: Decorator function
    """
    def decorator(func: Callable) -> Callable:
        # Encrypt the function's bytecode
        encrypted_code = runtime_encryption.encrypt_function(func)
        func_name = func.__name__
        func_globals = func.__globals__

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Generate unique ID for this function instance
            func_id = f"{func_name}_{id(func)}"

            try:
                # Decrypt function if not already decrypted
                if func_id not in runtime_encryption._decrypted_functions:
                    runtime_encryption._decrypted_functions[func_id] = \
                        runtime_encryption.decrypt_function(encrypted_code, func_globals)

                # Execute decrypted function
                result = runtime_encryption._decrypted_functions[func_id](*args, **kwargs)

                return result

            finally:
                # Clean up decrypted function
                runtime_encryption.cleanup_function(func_id)

        return wrapper
    return decorator