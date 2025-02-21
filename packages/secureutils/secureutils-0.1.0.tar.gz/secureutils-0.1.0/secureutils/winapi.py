"""
Windows API integration module with secure wrappers and platform compatibility checks.
"""

import sys
import os
import logging
import ctypes
from typing import Optional, Union, Dict, List, Tuple, Any, BinaryIO
from pathlib import Path
import struct

logger = logging.getLogger(__name__)

# Define required Windows constants
PROCESS_ALL_ACCESS = 0x1F0FFF
MEM_COMMIT = 0x1000
PAGE_EXECUTE_READWRITE = 0x40
PAGE_READWRITE = 0x04
MEM_RELEASE = 0x8000
INFINITE = 0xFFFFFFFF

class WinAPIError(Exception):
    """Exception raised for Windows API specific errors."""
    pass

class PEError(WinAPIError):
    """Exception raised for PE file handling errors."""
    pass

class InjectionError(WinAPIError):
    """Exception raised for injection-related errors."""
    pass

class PEFileManager:
    """Handles Portable Executable (PE) file operations and injection capabilities."""

    DOS_MAGIC = b'MZ'
    PE_MAGIC = b'PE\x00\x00'

    def __init__(self):
        """Initialize PE file manager with proper kernel32 function definitions."""
        self._is_windows = sys.platform.startswith('win32')
        if not self._is_windows:
            logger.warning("PEFileManager initialized on non-Windows platform. Injection features not available.")
            return

        self._kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

        # Define function prototypes
        self._kernel32.GetCurrentProcess.restype = ctypes.c_void_p
        self._kernel32.GetCurrentProcess.argtypes = []

        self._kernel32.VirtualAllocEx.restype = ctypes.c_void_p
        self._kernel32.VirtualAllocEx.argtypes = [
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_size_t,
            ctypes.c_ulong,
            ctypes.c_ulong
        ]

        self._kernel32.WriteProcessMemory.restype = ctypes.c_bool
        self._kernel32.WriteProcessMemory.argtypes = [
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_size_t,
            ctypes.POINTER(ctypes.c_size_t)
        ]

        self._kernel32.VirtualFreeEx.restype = ctypes.c_bool
        self._kernel32.VirtualFreeEx.argtypes = [
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_size_t,
            ctypes.c_ulong
        ]

        self._kernel32.CreateThread.restype = ctypes.c_void_p
        self._kernel32.CreateThread.argtypes = [
            ctypes.c_void_p,
            ctypes.c_size_t,
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_ulong,
            ctypes.POINTER(ctypes.c_ulong)
        ]

        self._kernel32.OpenProcess.restype = ctypes.c_void_p
        self._kernel32.OpenProcess.argtypes = [
            ctypes.c_ulong,
            ctypes.c_bool,
            ctypes.c_ulong
        ]

        self._kernel32.CreateRemoteThread.restype = ctypes.c_void_p
        self._kernel32.CreateRemoteThread.argtypes = [
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_size_t,
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_ulong,
            ctypes.POINTER(ctypes.c_ulong)
        ]

        self._kernel32.CloseHandle.restype = ctypes.c_bool
        self._kernel32.CloseHandle.argtypes = [ctypes.c_void_p]

        self._kernel32.GetProcAddress.restype = ctypes.c_void_p
        self._kernel32.GetProcAddress.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

        self._kernel32.WaitForSingleObject.restype = ctypes.c_ulong
        self._kernel32.WaitForSingleObject.argtypes = [ctypes.c_void_p, ctypes.c_ulong]

        self._kernel32.GetExitCodeThread.restype = ctypes.c_bool
        self._kernel32.GetExitCodeThread.argtypes = [
            ctypes.c_void_p,
            ctypes.POINTER(ctypes.c_ulong)
        ]

    def _check_platform(self) -> None:
        """Verify platform compatibility for Windows-specific operations."""
        if not self._is_windows:
            raise PEError("This operation requires Windows platform")

    def inject_self(self, target_pid: int, payload_path: str) -> bool:
        """
        Inject the current process with a payload DLL or executable.

        This method performs self-injection by:
        1. Loading the payload into the current process memory
        2. Creating a remote thread to execute the payload
        3. Handling proper memory cleanup and error cases

        Args:
            target_pid: Process ID to inject into (usually current process)
            payload_path: Path to the DLL or executable to inject

        Returns:
            bool: True if injection succeeded

        Raises:
            InjectionError: If injection fails or platform is unsupported
        """
        self._check_platform()
        try:
            # Get current process handle
            process_handle = self._kernel32.GetCurrentProcess()

            # Allocate memory in current process
            payload_size = os.path.getsize(payload_path)
            memory_ptr = self._kernel32.VirtualAllocEx(
                process_handle,
                None,
                payload_size,
                MEM_COMMIT,  # MEM_COMMIT
                PAGE_EXECUTE_READWRITE     # PAGE_EXECUTE_READWRITE
            )

            if not memory_ptr:
                raise InjectionError(f"Memory allocation failed: {ctypes.get_last_error()}")

            # Read and write payload
            with open(payload_path, 'rb') as f:
                payload_data = f.read()

            bytes_written = ctypes.c_size_t(0)
            success = self._kernel32.WriteProcessMemory(
                process_handle,
                memory_ptr,
                payload_data,
                len(payload_data),
                ctypes.byref(bytes_written)
            )

            if not success:
                self._kernel32.VirtualFreeEx(process_handle, memory_ptr, 0, MEM_RELEASE)  # MEM_RELEASE
                raise InjectionError(f"Failed to write payload: {ctypes.get_last_error()}")

            # Create thread to execute payload
            thread_handle = self._kernel32.CreateThread(
                None,
                0,
                memory_ptr,
                None,
                0,
                None
            )

            if not thread_handle:
                self._kernel32.VirtualFreeEx(process_handle, memory_ptr, 0, MEM_RELEASE)
                raise InjectionError(f"Thread creation failed: {ctypes.get_last_error()}")

            return True

        except Exception as e:
            raise InjectionError(f"Self-injection failed: {str(e)}")

    def inject_process(self, target_pid: int, payload_path: str) -> bool:
        """
        Inject a payload into a target process.

        This method performs process injection by:
        1. Opening the target process
        2. Allocating memory in the target process
        3. Writing the payload to the allocated memory
        4. Creating a remote thread to execute the payload

        Args:
            target_pid: Process ID to inject into
            payload_path: Path to the payload to inject

        Returns:
            bool: True if injection succeeded

        Raises:
            InjectionError: If injection fails or platform is unsupported
        """
        self._check_platform()
        try:
            # Open target process
            process_handle = self._kernel32.OpenProcess(
                PROCESS_ALL_ACCESS,  # PROCESS_ALL_ACCESS
                False,
                target_pid
            )

            if not process_handle:
                raise InjectionError(f"Failed to open process {target_pid}")

            try:
                # Allocate memory in target process
                payload_size = os.path.getsize(payload_path)
                memory_ptr = self._kernel32.VirtualAllocEx(
                    process_handle,
                    None,
                    payload_size,
                    MEM_COMMIT,  # MEM_COMMIT
                    PAGE_EXECUTE_READWRITE     # PAGE_EXECUTE_READWRITE
                )

                if not memory_ptr:
                    raise InjectionError(f"Memory allocation failed: {ctypes.get_last_error()}")

                # Read and write payload
                with open(payload_path, 'rb') as f:
                    payload_data = f.read()

                bytes_written = ctypes.c_size_t(0)
                success = self._kernel32.WriteProcessMemory(
                    process_handle,
                    memory_ptr,
                    payload_data,
                    len(payload_data),
                    ctypes.byref(bytes_written)
                )

                if not success:
                    self._kernel32.VirtualFreeEx(process_handle, memory_ptr, 0, MEM_RELEASE)
                    raise InjectionError(f"Failed to write payload: {ctypes.get_last_error()}")

                # Create remote thread
                thread_handle = self._kernel32.CreateRemoteThread(
                    process_handle,
                    None,
                    0,
                    memory_ptr,
                    None,
                    0,
                    None
                )

                if not thread_handle:
                    self._kernel32.VirtualFreeEx(process_handle, memory_ptr, 0, MEM_RELEASE)
                    raise InjectionError(f"Remote thread creation failed: {ctypes.get_last_error()}")

                return True

            finally:
                self._kernel32.CloseHandle(process_handle)

        except Exception as e:
            raise InjectionError(f"Process injection failed: {str(e)}")

    def inject_dll(self, target_pid: int, dll_path: str) -> bool:
        """
        Inject a DLL into a target process using LoadLibrary.

        This method performs DLL injection by:
        1. Opening the target process
        2. Allocating memory for the DLL path
        3. Writing the DLL path to the allocated memory
        4. Creating a remote thread that calls LoadLibrary

        Args:
            target_pid: Process ID to inject the DLL into
            dll_path: Full path to the DLL file

        Returns:
            bool: True if DLL injection succeeded

        Raises:
            InjectionError: If injection fails or platform is unsupported
        """
        self._check_platform()
        try:
            # Verify DLL exists
            if not os.path.exists(dll_path):
                raise InjectionError(f"DLL not found: {dll_path}")

            # Get LoadLibrary address
            kernel32_handle = self._kernel32._handle
            loadlib_addr = self._kernel32.GetProcAddress(
                kernel32_handle,
                b"LoadLibraryA"
            )

            if not loadlib_addr:
                raise InjectionError("Failed to get LoadLibrary address")

            # Open target process
            process_handle = self._kernel32.OpenProcess(
                PROCESS_ALL_ACCESS,  # PROCESS_ALL_ACCESS
                False,
                target_pid
            )

            if not process_handle:
                raise InjectionError(f"Failed to open process {target_pid}")

            try:
                # Allocate memory for DLL path
                dll_path_bytes = dll_path.encode('ascii') + b'\x00'
                memory_ptr = self._kernel32.VirtualAllocEx(
                    process_handle,
                    None,
                    len(dll_path_bytes),
                    MEM_COMMIT,  # MEM_COMMIT
                    PAGE_READWRITE     # PAGE_READWRITE
                )

                if not memory_ptr:
                    raise InjectionError(f"Memory allocation failed: {ctypes.get_last_error()}")

                # Write DLL path
                bytes_written = ctypes.c_size_t(0)
                success = self._kernel32.WriteProcessMemory(
                    process_handle,
                    memory_ptr,
                    dll_path_bytes,
                    len(dll_path_bytes),
                    ctypes.byref(bytes_written)
                )

                if not success:
                    self._kernel32.VirtualFreeEx(process_handle, memory_ptr, 0, MEM_RELEASE)
                    raise InjectionError(f"Failed to write DLL path: {ctypes.get_last_error()}")

                # Create remote thread to load DLL
                thread_handle = self._kernel32.CreateRemoteThread(
                    process_handle,
                    None,
                    0,
                    loadlib_addr,
                    memory_ptr,
                    0,
                    None
                )

                if not thread_handle:
                    self._kernel32.VirtualFreeEx(process_handle, memory_ptr, 0, MEM_RELEASE)
                    raise InjectionError(f"Remote thread creation failed: {ctypes.get_last_error()}")

                # Wait for thread completion
                self._kernel32.WaitForSingleObject(thread_handle, INFINITE)

                # Get thread exit code
                exit_code = ctypes.c_ulong(0)
                self._kernel32.GetExitCodeThread(thread_handle, ctypes.byref(exit_code))

                # Cleanup
                self._kernel32.CloseHandle(thread_handle)
                self._kernel32.VirtualFreeEx(process_handle, memory_ptr, 0, MEM_RELEASE)

                if exit_code.value == 0:
                    raise InjectionError("DLL load failed in remote process")

                return True

            finally:
                self._kernel32.CloseHandle(process_handle)

        except Exception as e:
            raise InjectionError(f"DLL injection failed: {str(e)}")

    def read_dos_header(self, file_handle: BinaryIO) -> Dict[str, Any]:
        """
        Read DOS header from PE file.

        Args:
            file_handle: Open file handle in binary mode

        Returns:
            Dict[str, Any]: DOS header fields

        Raises:
            PEError: If header is invalid or incomplete
        """
        try:
            # Read complete DOS header (64 bytes)
            dos_header = file_handle.read(64)
            if len(dos_header) < 64:
                raise PEError("Incomplete DOS header")

            if dos_header[:2] != self.DOS_MAGIC:
                raise PEError("Invalid DOS header - not a valid PE file")

            # Return the magic bytes directly instead of converting to int
            e_magic = dos_header[:2]  # Keep as bytes
            e_lfanew = struct.unpack('<I', dos_header[60:64])[0]  # e_lfanew is at offset 60

            return {
                'e_magic': e_magic,
                'e_lfanew': e_lfanew  # Offset to PE header
            }
        except struct.error as e:
            raise PEError(f"Failed to parse DOS header: {str(e)}")
        except Exception as e:
            raise PEError(f"Unexpected error reading DOS header: {str(e)}")

    def read_pe_header(self, file_handle: BinaryIO, pe_offset: int) -> Dict[str, Any]:
        """
        Read PE header from file.

        Args:
            file_handle: Open file handle
            pe_offset: Offset to PE header

        Returns:
            Dict[str, Any]: PE header information
        """
        try:
            file_handle.seek(pe_offset)
            signature = file_handle.read(4)

            if signature != self.PE_MAGIC:
                raise PEError("Invalid PE signature")

            # Read COFF header (20 bytes)
            coff_header = file_handle.read(20)
            machine, num_sections, time_date_stamp, ptr_symbol_table, \
            num_symbols, size_opt_header, characteristics = struct.unpack(
                '<HHIIIHH', coff_header
            )

            return {
                'Machine': machine,
                'NumberOfSections': num_sections,
                'TimeDateStamp': time_date_stamp,
                'Characteristics': characteristics,
                'SizeOfOptionalHeader': size_opt_header
            }
        except struct.error as e:
            raise PEError(f"Failed to parse PE header: {str(e)}")

    def calculate_checksum(self, file_path: Union[str, Path]) -> int:
        """
        Calculate PE file checksum.

        Args:
            file_path: Path to PE file

        Returns:
            int: Calculated checksum
        """
        try:
            file_path = Path(file_path)
            checksum = 0

            with open(file_path, 'rb') as f:
                # Read file in 64KB chunks
                while chunk := f.read(65536):
                    # Process each WORD (2 bytes)
                    for i in range(0, len(chunk), 2):
                        if i + 1 < len(chunk):
                            word = struct.unpack('<H', chunk[i:i+2])[0]
                        else:
                            word = chunk[i]
                        checksum = (checksum & 0xFFFF) + word + (checksum >> 16)

            checksum = (checksum & 0xFFFF) + (checksum >> 16)
            checksum = checksum & 0xFFFF

            return checksum
        except Exception as e:
            raise PEError(f"Checksum calculation failed: {str(e)}")

    def verify_checksum(self, file_path: Union[str, Path]) -> bool:
        """
        Verify PE file checksum.

        Args:
            file_path: Path to PE file

        Returns:
            bool: True if checksum is valid
        """
        try:
            file_path = Path(file_path)
            with open(file_path, 'rb') as f:
                dos_header = self.read_dos_header(f)
                pe_header = self.read_pe_header(f, dos_header['e_lfanew'])

                # Read stored checksum
                f.seek(dos_header['e_lfanew'] + 88)  # Checksum offset in Optional Header
                stored_checksum = struct.unpack('<I', f.read(4))[0]

                # Calculate actual checksum
                calculated = self.calculate_checksum(file_path)

                return stored_checksum == calculated
        except Exception as e:
            raise PEError(f"Checksum verification failed: {str(e)}")

    def is_pe_file(self, file_path: Union[str, Path]) -> bool:
        """
        Check if file is a valid PE file.

        Args:
            file_path: Path to check

        Returns:
            bool: True if file is PE format
        """
        try:
            file_path = Path(file_path)
            with open(file_path, 'rb') as f:
                # Check DOS header
                if len(dos_magic := f.read(2)) != 2 or dos_magic != self.DOS_MAGIC:
                    return False

                # Find PE header offset
                f.seek(60)
                pe_offset = struct.unpack('<I', f.read(4))[0]

                # Check PE signature
                f.seek(pe_offset)
                return f.read(4) == self.PE_MAGIC
        except Exception:
            return False

    def read_sections(self, file_path: Union[str, Path]) -> List[Dict[str, Any]]:
        """
        Read PE file sections.

        Args:
            file_path: Path to PE file

        Returns:
            List[Dict[str, Any]]: List of section information
        """
        try:
            file_path = Path(file_path)
            sections = []

            with open(file_path, 'rb') as f:
                dos_header = self.read_dos_header(f)
                pe_header = self.read_pe_header(f, dos_header['e_lfanew'])

                # Skip to section headers
                f.seek(dos_header['e_lfanew'] + 24 + pe_header.get('SizeOfOptionalHeader', 0))

                # Read each section
                for _ in range(pe_header['NumberOfSections']):
                    section_header = f.read(40)  # Size of section header

                    name, virtual_size, virtual_address, size_of_raw_data, \
                    pointer_to_raw_data, pointer_to_relocations, pointer_to_linenumbers, \
                    number_of_relocations, number_of_linenumbers, characteristics = \
                        struct.unpack('<8sIIIIIIHHI', section_header)

                    sections.append({
                        'Name': name.decode('utf-8').rstrip('\x00'),
                        'VirtualSize': virtual_size,
                        'VirtualAddress': virtual_address,
                        'SizeOfRawData': size_of_raw_data,
                        'PointerToRawData': pointer_to_raw_data,
                        'Characteristics': characteristics
                    })

            return sections
        except Exception as e:
            raise PEError(f"Failed to read sections: {str(e)}")

    def read_imports(self, file_path: Union[str, Path]) -> Dict[str, List[str]]:
        """
        Read PE file import directory.

        Args:
            file_path: Path to PE file

        Returns:
            Dict[str, List[str]]: Dictionary of DLL names and their imported functions
        """
        try:
            file_path = Path(file_path)
            imports = {}

            with open(file_path, 'rb') as f:
                dos_header = self.read_dos_header(f)
                pe_header = self.read_pe_header(f, dos_header['e_lfanew'])

                # Read Optional Header to find import directory
                f.seek(dos_header['e_lfanew'] + 24)  # Skip to Optional Header
                optional_header = f.read(96 if pe_header['Machine'] == 0x14c else 112)

                # Find import directory RVA
                import_dir_rva = struct.unpack('<I', optional_header[80:84])[0]

                if import_dir_rva:
                    # Read sections to find the right section containing imports
                    sections = self.read_sections(file_path)
                    for section in sections:
                        if (section['VirtualAddress'] <= import_dir_rva <
                            section['VirtualAddress'] + section['VirtualSize']):

                            offset = import_dir_rva - section['VirtualAddress']
                            f.seek(section['PointerToRawData'] + offset)

                            while True:
                                import_desc = f.read(20)
                                if not any(import_desc):  # All zeros means end of imports
                                    break

                                dll_name_rva = struct.unpack('<I', import_desc[12:16])[0]

                                # Read DLL name
                                f.seek(dll_name_rva)
                                dll_name = ''
                                while True:
                                    char = f.read(1)
                                    if char == b'\x00':
                                        break
                                    dll_name += char.decode('ascii')

                                imports[dll_name] = []

            return imports
        except Exception as e:
            raise PEError(f"Failed to read imports: {str(e)}")

    def read_exports(self, file_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Read PE file export directory.

        Args:
            file_path: Path to PE file

        Returns:
            Dict[str, Any]: Export directory information
        """
        if not self._is_windows:
            logger.warning("Export directory analysis may be limited on non-Windows platform")
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                raise PEError(f"File not found: {file_path}")

            exports = {}
            with open(file_path, 'rb') as f:
                dos_header = self.read_dos_header(f)
                pe_header = self.read_pe_header(f, dos_header['e_lfanew'])

                # Read Optional Header to find export directory
                f.seek(dos_header['e_lfanew'] + 24)
                optional_header = f.read(96 if pe_header['Machine'] == 0x14c else 112)

                # Find export directory RVA
                export_dir_rva = struct.unpack('<I', optional_header[96:100])[0]

                if export_dir_rva:
                    # Find section containing exports
                    sections = self.read_sections(file_path)
                    for section in sections:
                        if (section['VirtualAddress'] <= export_dir_rva <
                            section['VirtualAddress'] + section['VirtualSize']):

                            offset = export_dir_rva - section['VirtualAddress']
                            f.seek(section['PointerToRawData'] + offset)

                            # Read export directory
                            export_dir = f.read(40)
                            characteristics, time_date_stamp, major_version, \
                            minor_version, name_rva, ordinal_base, num_functions, \
                            num_names, functions_rva, names_rva, ordinals_rva = \
                                struct.unpack('<10I', export_dir)

                            exports.update({
                                'Characteristics': characteristics,
                                'TimeDateStamp': time_date_stamp,
                                'MajorVersion': major_version,
                                'MinorVersion': minor_version,
                                'NameRVA': name_rva,
                                'OrdinalBase': ordinal_base,
                                'NumberOfFunctions': num_functions,
                                'NumberOfNames': num_names,
                                'FunctionsRVA': functions_rva,
                                'NamesRVA': names_rva,
                                'OrdinalsRVA': ordinals_rva
                            })

            return exports
        except FileNotFoundError:
            raise PEError(f"File not found: {file_path}")
        except PermissionError:
            raise PEError(f"Permission denied accessing file: {file_path}")
        except Exception as e:
            raise PEError(f"Failed to read exports: {str(e)}")

    def read_resources(self, file_path: Union[str, Path]) -> List[Dict[str, Any]]:
        """
        Read PE file resource directory.

        Args:
            file_path: Path to PE file

        Returns:
            List[Dict[str, Any]]: List of resource entries
        """
        if not self._is_windows:
            logger.warning("Resource directory analysis may be limited on non-Windows platform")
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                raise PEError(f"File not found: {file_path}")

            resources = []
            with open(file_path, 'rb') as f:
                dos_header = self.read_dos_header(f)
                pe_header = self.read_pe_header(f, dos_header['e_lfanew'])

                # Find resource directory RVA
                f.seek(dos_header['e_lfanew'] + 24)
                optional_header = f.read(96 if pe_header['Machine'] == 0x14c else 112)
                resource_dir_rva = struct.unpack('<I', optional_header[112:116])[0]

                if resource_dir_rva:
                    # Find section containing resources
                    sections = self.read_sections(file_path)
                    for section in sections:
                        if section['Name'].startswith('.rsrc'):
                            f.seek(section['PointerToRawData'])

                            # Read resource directory header
                            res_dir = f.read(16)
                            characteristics, time_date_stamp, major_version, \
                            minor_version, num_named, num_id = struct.unpack(
                                '<IIHHHH', res_dir
                            )

                            resources.append({
                                'Characteristics': characteristics,
                                'TimeDateStamp': time_date_stamp,
                                'MajorVersion': major_version,
                                'MinorVersion': minor_version,
                                'NumberOfNamedEntries': num_named,
                                'NumberOfIdEntries': num_id
                            })

            return resources
        except FileNotFoundError:
            raise PEError(f"File not found: {file_path}")
        except PermissionError:
            raise PEError(f"Permission denied accessing file: {file_path}")
        except Exception as e:
            raise PEError(f"Failed to read resources: {str(e)}")

    def read_relocations(self, file_path: Union[str, Path]) -> List[Dict[str, Any]]:
        """
        Read PE file base relocations.

        Args:
            file_path: Path to PE file

        Returns:
            List[Dict[str, Any]]: List of relocation blocks
        """
        try:
            file_path = Path(file_path)
            relocations = []

            with open(file_path, 'rb') as f:
                dos_header = self.read_dos_header(f)
                pe_header = self.read_pe_header(f, dos_header['e_lfanew'])

                # Find relocation directory RVA
                f.seek(dos_header['e_lfanew'] + 24)
                optional_header = f.read(96 if pe_header['Machine'] == 0x14c else 112)
                reloc_dir_rva = struct.unpack('<I', optional_header[136:140])[0]

                if reloc_dir_rva:
                    sections = self.read_sections(file_path)
                    for section in sections:
                        if (section['VirtualAddress'] <= reloc_dir_rva <
                            section['VirtualAddress'] + section['VirtualSize']):

                            offset = reloc_dir_rva - section['VirtualAddress']
                            f.seek(section['PointerToRawData'] + offset)

                            while True:
                                block_header = f.read(8)
                                if not block_header or len(block_header) < 8:
                                    break

                                page_rva, block_size = struct.unpack('<II', block_header)
                                if not page_rva or not block_size:
                                    break

                                entries = []
                                num_entries = (block_size - 8) // 2
                                for _ in range(num_entries):
                                    entry = struct.unpack('<H', f.read(2))[0]
                                    entries.append({
                                        'Type': (entry >> 12),
                                        'Offset': (entry & 0x0FFF)
                                    })

                                relocations.append({
                                    'PageRVA': page_rva,
                                    'BlockSize': block_size,
                                    'Entries': entries
                                })

            return relocations
        except Exception as e:
            raise PEError(f"Failed to read relocations: {str(e)}")


class WindowsAPIManager:
    """Manages Windows API operations with security considerations."""

    def __init__(self):
        """Initialize the Windows API manager with platform checks."""
        self._is_windows = sys.platform.startswith('win32')
        self.pe = PEFileManager()
        if not self._is_windows:
            logger.warning("WindowsAPIManager initialized on non-Windows platform")

    def _check_platform(self) -> None:
        """Verify Windows platform availability."""
        if not self._is_windows:
            raise WinAPIError("This operation requires Windows platform")

    def create_registry_key(
        self,
        key_path: str,
        value_name: str,
        value_data: Union[str, int],
        key_type: str = "REG_SZ"
    ) -> bool:
        """
        Securely create or modify a registry key.

        Args:
            key_path: Registry key path
            value_name: Name of the registry value
            value_data: Data to store (string or integer)
            key_type: Registry value type

        Returns:
            bool: Success status

        Raises:
            WinAPIError: If platform is not Windows or operation fails
        """
        self._check_platform()
        try:
            import winreg
            root_key = winreg.HKEY_CURRENT_USER

            # Sanitize and validate inputs
            if not isinstance(key_path, str) or not isinstance(value_name, str):
                raise ValueError("Invalid key_path or value_name type")

            # Map registry types
            type_map = {
                "REG_SZ": winreg.REG_SZ,
                "REG_DWORD": winreg.REG_DWORD,
            }

            reg_type = type_map.get(key_type.upper())
            if reg_type is None:
                raise ValueError(f"Unsupported registry type: {key_type}")

            # Create or open key with secure permissions
            key = winreg.CreateKeyEx(root_key, key_path, 0,
                                   winreg.KEY_WRITE | winreg.KEY_WOW64_64KEY)

            # Set value with appropriate type
            winreg.SetValueEx(key, value_name, 0, reg_type, value_data)
            winreg.CloseKey(key)
            return True

        except ImportError:
            raise WinAPIError("Failed to import winreg module")
        except Exception as e:
            logger.error(f"Registry operation failed: {str(e)}")
            raise WinAPIError(f"Registry operation failed: {str(e)}")

    def read_registry_key(
        self,
        key_path: str,
        value_name: str
    ) -> Tuple[str, Any]:
        """
        Securely read a registry key value.

        Args:
            key_path: Registry key path
            value_name: Name of the registry value

        Returns:
            Tuple[str, Any]: Registry type and value

        Raises:
            WinAPIError: If platform is not Windows or operation fails
        """
        self._check_platform()
        try:
            import winreg
            root_key = winreg.HKEY_CURRENT_USER

            # Open key with minimal required permissions
            key = winreg.OpenKey(root_key, key_path, 0,
                               winreg.KEY_READ | winreg.KEY_WOW64_64KEY)

            value_data, value_type = winreg.QueryValueEx(key, value_name)
            winreg.CloseKey(key)

            # Map registry type to string representation
            type_map = {
                winreg.REG_SZ: "REG_SZ",
                winreg.REG_DWORD: "REG_DWORD",
            }

            return type_map.get(value_type, "UNKNOWN"), value_data

        except ImportError:
            raise WinAPIError("Failed to import winreg module")
        except Exception as e:
            logger.error(f"Registry read failed: {str(e)}")
            raise WinAPIError(f"Registry read failed: {str(e)}")

    def create_named_pipe(
        self,
        pipe_name: str,
        buffer_size: int = 4096
    ) -> Any:
        """
        Create a secure named pipe for IPC.

        Args:
            pipe_name: Name of the pipe
            buffer_size: Buffer size for the pipe

        Returns:
            Any: Pipe handle object

        Raises:
            WinAPIError: If platform is not Windows or operation fails
        """
        self._check_platform()
        try:
            import win32pipe
            import win32security

            # Create security attributes with restricted access
            sa = win32security.SECURITY_ATTRIBUTES()
            sa.bInheritHandle = False

            # Sanitize pipe name
            if not pipe_name.startswith(r"\\.\pipe\\"):
                pipe_name = r"\\.\pipe\\" + pipe_name

            # Create pipe with secure defaults
            pipe_handle = win32pipe.CreateNamedPipe(
                pipe_name,
                win32pipe.PIPE_ACCESS_DUPLEX,
                win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE,
                1,  # Maximum instances
                buffer_size,
                buffer_size,
                0,  # Default timeout
                sa
            )

            return pipe_handle
        except ImportError:
            raise WinAPIError("Failed to import win32pipe/win32security modules")
        except Exception as e:
            logger.error(f"Named pipe creation failed: {str(e)}")
            raise WinAPIError(f"Named pipe creation failed: {str(e)}")

    def create_file_mapping(
        self,
        file_path: Optional[Union[str, Path]] = None,
        map_name: Optional[str] = None,
        size: int = 4096
    ) -> Tuple[Any, Any]:
        """
        Create a secure file mapping object for shared memory.

        Args:
            file_path: Optional path to back the mapping with a file
            map_name: Optional name for the mapping
            size: Size of the mapping in bytes

        Returns:
            Tuple[Any, Any]: File mapping handle and view handle

        Raises:
            WinAPIError: If platform is not Windows or operation fails
        """
        self._check_platform()
        try:
            import mmap
            import win32file
            import win32security

            # Set up security attributes
            sa = win32security.SECURITY_ATTRIBUTES()
            sa.bInheritHandle = False

            # Create file mapping
            if file_path:
                file_handle = win32file.CreateFile(
                    str(file_path),
                    win32file.GENERIC_READ | win32file.GENERIC_WRITE,
                    0,  # No sharing
                    sa,
                    win32file.OPEN_ALWAYS,
                    win32file.FILE_ATTRIBUTE_NORMAL,
                    None
                )
            else:
                file_handle = -1  # INVALID_HANDLE_VALUE

            # Create file mapping object using mmap for better compatibility
            if file_handle != -1:
                mapping = mmap.mmap(file_handle.handle, size)
            else:
                mapping = mmap.mmap(-1, size)

            return file_handle, mapping

        except ImportError:
            raise WinAPIError("Failed to import required modules")
        except Exception as e:
            logger.error(f"File mapping creation failed: {str(e)}")
            raise WinAPIError(f"File mapping creation failed: {str(e)}")

    def delete_registry_key(
        self,
        key_path: str,
        value_name: Optional[str] = None
    ) -> bool:
        """
        Securely delete a registry key or value.

        Args:
            key_path: Registry key path
            value_name: Optional value name to delete (if None, deletes entire key)

        Returns:
            bool: Success status
        """
        self._check_platform()
        try:
            import winreg
            root_key = winreg.HKEY_CURRENT_USER

            if value_name:
                # Delete specific value
                key = winreg.OpenKey(root_key, key_path, 0,
                                   winreg.KEY_SET_VALUE | winreg.KEY_WOW64_64KEY)
                winreg.DeleteValue(key, value_name)
            else:
                # Delete entire key
                winreg.DeleteKey(root_key, key_path)

            return True

        except ImportError:
            raise WinAPIError("Failed to import winreg module")
        except Exception as e:
            logger.error(f"Registry deletion failed: {str(e)}")
            raise WinAPIError(f"Registry deletion failed: {str(e)}")

    def virtual_alloc(
        self,
        size: int,
        allocation_type: str = "commit",
        protection: str = "read_write"
    ) -> Any:
        """
        Allocate virtual memory with security considerations.

        Args:
            size: Size of memory to allocate
            allocation_type: Type of allocation ("reserve" or "commit")
            protection: Memory protection ("read_write", "read_only", "execute")

        Returns:
            Any: Memory buffer object
        """
        self._check_platform()
        try:
            import ctypes
            from ctypes import wintypes

            # Map allocation types
            alloc_types = {
                "reserve": 0x2000,  # MEM_RESERVE
                "commit": 0x1000    # MEM_COMMIT
            }

            # Map protection flags
            protect_flags = {
                "read_only": 0x02,  # PAGE_READONLY
                "read_write": 0x04, # PAGE_READWRITE
                "execute": 0x20     # PAGE_EXECUTE
            }

            alloc_type = alloc_types.get(allocation_type.lower())
            protect = protect_flags.get(protection.lower())

            if not alloc_type or not protect:
                raise ValueError("Invalid allocation type or protection")

            # Allocate memory
            kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
            kernel32.VirtualAlloc.restype = wintypes.LPVOID
            kernel32.VirtualAlloc.argtypes = (
                wintypes.LPVOID,
                ctypes.c_size_t,
                wintypes.DWORD,
                wintypes.DWORD
            )

            address = kernel32.VirtualAlloc(
                None,
                size,
                alloc_type,
                protect
            )

            if not address:
                raise WinAPIError(f"Memory allocation failed: {ctypes.get_last_error()}")

            return address

        except ImportError:
            raise WinAPIError("Failed to import required modules")
        except Exception as e:
            logger.error(f"Memory allocation failed: {str(e)}")
            raise WinAPIError(f"Memory allocation failed: {str(e)}")