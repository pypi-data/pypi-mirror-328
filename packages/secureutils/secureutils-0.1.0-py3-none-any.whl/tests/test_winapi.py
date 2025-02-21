"""
Test cases for Windows API operations with platform compatibility checks.
"""

import unittest
import sys
import os
import tempfile
from pathlib import Path
import struct
from secureutils.winapi import WindowsAPIManager, WinAPIError, PEError, InjectionError, PEFileManager

class TestWindowsAPIManager(unittest.TestCase):
    """Test Windows API operations."""

    def setUp(self):
        """Set up test cases."""
        self.winapi = WindowsAPIManager()
        self.pe_manager = PEFileManager()
        self.is_windows = sys.platform.startswith('win32')
        self.test_dll_path = None

        # Create test DLL if on Windows
        if self.is_windows:
            self.test_dll_path = self.create_test_dll()

    def tearDown(self):
        """Clean up after tests."""
        if self.test_dll_path and os.path.exists(self.test_dll_path):
            try:
                os.remove(self.test_dll_path)
            except Exception:
                pass

    def create_test_dll(self) -> str:
        """Create a test DLL for injection tests."""
        dll_path = os.path.join(tempfile.gettempdir(), "test_injection.dll")
        if os.path.exists(dll_path):
            return dll_path

        # In a real environment, we would compile the DLL here
        # For testing, we'll create a minimal PE file
        with open(dll_path, 'wb') as f:
            # Write minimal PE header
            f.write(b'MZ')  # DOS header
            f.write(b'\x00' * 58)  # Padding
            f.write(struct.pack('<I', 0x40))  # e_lfanew
            f.write(b'PE\x00\x00')  # PE signature

        return dll_path

    def test_injection_non_windows(self):
        """Test injection operations on non-Windows platforms."""
        if self.is_windows:
            self.skipTest("Windows-specific test")

        with self.assertRaises(PEError):
            self.pe_manager.inject_self(os.getpid(), "dummy.dll")

        with self.assertRaises(PEError):
            self.pe_manager.inject_process(os.getpid(), "dummy.dll")

        with self.assertRaises(PEError):
            self.pe_manager.inject_dll(os.getpid(), "dummy.dll")

    @unittest.skipUnless(sys.platform.startswith('win32'), "Windows-only test")
    def test_self_injection(self):
        """Test self-injection capabilities."""
        if not self.test_dll_path:
            self.skipTest("Test DLL not available")

        # Test with invalid DLL path
        with self.assertRaises(InjectionError):
            self.pe_manager.inject_self(os.getpid(), "nonexistent.dll")

        # Test with valid DLL
        try:
            result = self.pe_manager.inject_self(os.getpid(), self.test_dll_path)
            self.assertTrue(result)
        except InjectionError as e:
            if "access denied" in str(e).lower():
                self.skipTest("Test requires elevated privileges")

    @unittest.skipUnless(sys.platform.startswith('win32'), "Windows-only test")
    def test_process_injection(self):
        """Test process injection capabilities."""
        if not self.test_dll_path:
            self.skipTest("Test DLL not available")

        # Test with invalid process ID
        with self.assertRaises(InjectionError):
            self.pe_manager.inject_process(99999, self.test_dll_path)

        # Test with current process
        try:
            result = self.pe_manager.inject_process(os.getpid(), self.test_dll_path)
            self.assertTrue(result)
        except InjectionError as e:
            if "access denied" in str(e).lower():
                self.skipTest("Test requires elevated privileges")

    @unittest.skipUnless(sys.platform.startswith('win32'), "Windows-only test")
    def test_dll_injection(self):
        """Test DLL injection capabilities."""
        if not self.test_dll_path:
            self.skipTest("Test DLL not available")

        # Test with nonexistent DLL
        with self.assertRaises(InjectionError):
            self.pe_manager.inject_dll(os.getpid(), "nonexistent.dll")

        # Test with current process
        try:
            result = self.pe_manager.inject_dll(os.getpid(), self.test_dll_path)
            self.assertTrue(result)
        except InjectionError as e:
            if "access denied" in str(e).lower():
                self.skipTest("Test requires elevated privileges")

    def test_pe_file_validation(self):
        """Test PE file format validation."""
        test_file = self.create_test_pe_file()
        try:
            # Test valid PE file
            self.assertTrue(self.winapi.pe.is_pe_file(test_file))

            # Test invalid file
            with open(test_file, 'wb') as f:
                f.write(b'Not a PE file')
            self.assertFalse(self.winapi.pe.is_pe_file(test_file))

        finally:
            if test_file.exists():
                test_file.unlink()

    def test_pe_header_reading(self):
        """Test PE header parsing."""
        test_file = self.create_test_pe_file()
        try:
            with open(test_file, 'rb') as f:
                # Test DOS header reading
                dos_header = self.winapi.pe.read_dos_header(f)
                self.assertEqual(dos_header['e_magic'], b'MZ')
                self.assertEqual(dos_header['e_lfanew'], 128)

                # Test PE header reading
                pe_header = self.winapi.pe.read_pe_header(f, dos_header['e_lfanew'])
                self.assertEqual(pe_header['Machine'], 0x14C)  # i386
                self.assertEqual(pe_header['NumberOfSections'], 2)

        finally:
            if test_file.exists():
                test_file.unlink()

    def test_pe_error_handling(self):
        """Test PE error handling."""
        test_file = Path(tempfile.mktemp())
        try:
            # Test with empty file
            with open(test_file, 'wb') as f:
                f.write(b'')

            with self.assertRaises(PEError):
                with open(test_file, 'rb') as f:
                    self.winapi.pe.read_dos_header(f)

            # Test with invalid PE signature
            with open(test_file, 'wb') as f:
                f.write(b'MZ' + b'\0' * 58 + struct.pack('<I', 64))
                f.write(b'XX\0\0')  # Invalid PE signature

            with self.assertRaises(PEError):
                with open(test_file, 'rb') as f:
                    dos_header = self.winapi.pe.read_dos_header(f)
                    self.winapi.pe.read_pe_header(f, dos_header['e_lfanew'])

        finally:
            if test_file.exists():
                test_file.unlink()

    def test_platform_check(self):
        """Test platform detection and error handling."""
        if not self.is_windows:
            with self.assertRaises(WinAPIError):
                self.winapi.create_registry_key(
                    "Software\\TestKey",
                    "TestValue",
                    "TestData"
                )

    @unittest.skipUnless(sys.platform.startswith('win32'), "Windows-only test")
    def test_registry_operations(self):
        """Test registry operations on Windows."""
        test_path = "Software\\SecureUtilsTest"
        test_name = "TestValue"
        test_data = "TestData123"

        # Test creating registry key
        success = self.winapi.create_registry_key(
            test_path,
            test_name,
            test_data
        )
        self.assertTrue(success)

        # Test reading registry key
        reg_type, value = self.winapi.read_registry_key(
            test_path,
            test_name
        )
        self.assertEqual(reg_type, "REG_SZ")
        self.assertEqual(value, test_data)

    @unittest.skipUnless(sys.platform.startswith('win32'), "Windows-only test")
    def test_named_pipe(self):
        """Test named pipe creation on Windows."""
        pipe_name = "SecureUtilsTestPipe"
        pipe_handle = None

        try:
            pipe_handle = self.winapi.create_named_pipe(pipe_name)
            self.assertIsNotNone(pipe_handle)
        finally:
            if pipe_handle:
                try:
                    pipe_handle.Close()
                except AttributeError:
                    # Handle case where Close method might not be available
                    pass

    @unittest.skipUnless(sys.platform.startswith('win32'), "Windows-only test")
    def test_file_mapping(self):
        """Test file mapping operations on Windows."""
        mapping_handle = None
        view_handle = None

        try:
            mapping_handle, view_handle = self.winapi.create_file_mapping(
                map_name="SecureUtilsTestMapping",
                size=4096
            )
            self.assertIsNotNone(mapping_handle)
            self.assertIsNotNone(view_handle)
        finally:
            if view_handle:
                try:
                    view_handle.close()
                except Exception:
                    pass
            if mapping_handle and hasattr(mapping_handle, 'Close'):
                try:
                    mapping_handle.Close()
                except Exception:
                    pass

    def create_test_pe_file(self) -> Path:
        """Create a minimal test PE file."""
        temp_file = Path(tempfile.mktemp())

        with open(temp_file, 'wb') as f:
            # DOS Header (64 bytes)
            dos_header = bytearray([
                0x4D, 0x5A,  # e_magic 'MZ'
                0x90, 0x00,  # e_cblp
                0x03, 0x00,  # e_cp
                0x00, 0x00,  # e_crlc
                0x04, 0x00,  # e_cparhdr
                0x00, 0x00,  # e_minalloc
                0xFF, 0xFF,  # e_maxalloc
                0x00, 0x00,  # e_ss
                0xB8, 0x00,  # e_sp
                0x00, 0x00,  # e_csum
                0x00, 0x00,  # e_ip
                0x00, 0x00,  # e_cs
                0x40, 0x00,  # e_lfarlc
                0x00, 0x00,  # e_ovno
            ] + [0] * 32)  # e_res[4], e_oemid, e_oeminfo, e_res2[10]

            # e_lfanew (offset to PE header)
            dos_header.extend([0x80, 0x00, 0x00, 0x00])  # 128 bytes offset

            f.write(dos_header)

            # PE Header at offset 128
            f.seek(128)
            pe_header = bytearray([
                0x50, 0x45, 0x00, 0x00,  # PE\0\0
                0x4C, 0x01,  # Machine (i386)
                0x02, 0x00,  # NumberOfSections
                0x00, 0x00, 0x00, 0x00,  # TimeDateStamp
                0x00, 0x00, 0x00, 0x00,  # PointerToSymbolTable
                0x00, 0x00, 0x00, 0x00,  # NumberOfSymbols
                0xE0, 0x00,  # SizeOfOptionalHeader
                0x02, 0x01   # Characteristics (executable)
            ])
            f.write(pe_header)

        return temp_file

if __name__ == '__main__':
    unittest.main()