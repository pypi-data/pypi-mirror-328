import unittest
from secureutils.certificates import CertificateManager
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509 import oid
import tempfile
import os

class TestCertificateManager(unittest.TestCase):
    def setUp(self):
        self.cert_manager = CertificateManager()
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)

    def test_generate_private_key(self):
        key = self.cert_manager.generate_private_key()
        self.assertIsInstance(key, rsa.RSAPrivateKey)
        self.assertEqual(key.key_size, 2048)

    def test_create_certificate(self):
        private_key = self.cert_manager.generate_private_key()
        cert = self.cert_manager.create_certificate(
            private_key=private_key,
            common_name="test.example.com",
            country="US",
            state="California",
            locality="San Francisco",
            organization="Test Org"
        )

        self.assertIsInstance(cert, x509.Certificate)

    def test_create_code_signing_certificate(self):
        private_key = self.cert_manager.generate_private_key()
        cert = self.cert_manager.create_certificate(
            private_key=private_key,
            common_name="Code Signing Cert",
            country="US",
            state="California",
            locality="San Francisco",
            organization="Test Org",
            code_signing=True
        )

        self.assertIsInstance(cert, x509.Certificate)

        # Verify code signing extension
        ext = cert.extensions.get_extension_for_oid(oid.ExtendedKeyUsageOID.CODE_SIGNING)
        self.assertIsNotNone(ext)
        self.assertTrue(ext.critical)

    def test_sign_and_verify_executable(self):
        # Create a dummy executable file
        exe_path = os.path.join(self.temp_dir, "test.exe")
        with open(exe_path, "wb") as f:
            f.write(b"#!/usr/bin/env python\nprint('Hello, World!')")

        # Create signing certificate
        private_key = self.cert_manager.generate_private_key()
        cert = self.cert_manager.create_certificate(
            private_key=private_key,
            common_name="Code Signing Cert",
            country="US",
            state="California",
            locality="San Francisco",
            organization="Test Org",
            code_signing=True
        )

        # Sign executable
        sig_path = self.cert_manager.sign_executable(
            executable_path=exe_path,
            certificate=cert,
            private_key=private_key
        )

        self.assertTrue(sig_path.exists())

        # Verify signature
        is_valid = self.cert_manager.verify_executable(
            executable_path=exe_path,
            signature_path=str(sig_path),
            certificate=cert
        )

        self.assertTrue(is_valid)

    def test_save_certificate(self):
        private_key = self.cert_manager.generate_private_key()
        cert = self.cert_manager.create_certificate(
            private_key=private_key,
            common_name="test.example.com",
            country="US",
            state="California",
            locality="San Francisco",
            organization="Test Org"
        )

        cert_path = os.path.join(self.temp_dir, "cert.pem")
        key_path = os.path.join(self.temp_dir, "key.pem")

        saved_cert_path, saved_key_path = self.cert_manager.save_certificate(
            cert,
            private_key,
            cert_path,
            key_path
        )

        self.assertTrue(saved_cert_path.exists())
        self.assertTrue(saved_key_path.exists())

if __name__ == '__main__':
    unittest.main()