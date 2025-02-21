"""
SecureUtils - A comprehensive security and utility module for Python applications.
Provides secure request handling, file operations, certificate management, SQLite operations,
and Windows API integration with PE file analysis capabilities.
"""

from .http import SecureRequest
from .fileops import FileManager
from .certificates import CertificateManager
from .database import DatabaseManager
from .threadpool import ThreadPool
from .obfuscator import Obfuscator, obfuscate_file
from .crypto import CryptoManager, RuntimeEncryption, encrypted_function
from .winapi import WindowsAPIManager, PEFileManager, InjectionError

__version__ = "1.0.0"
__all__ = [
    'SecureRequest',
    'FileManager',
    'CertificateManager',
    'DatabaseManager',
    'ThreadPool',
    'Obfuscator',
    'obfuscate_file',
    'CryptoManager',
    'RuntimeEncryption',
    'encrypted_function',
    'WindowsAPIManager',
    'PEFileManager',
    'InjectionError'
]