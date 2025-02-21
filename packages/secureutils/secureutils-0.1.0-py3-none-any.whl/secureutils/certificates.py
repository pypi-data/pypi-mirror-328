"""
Certificate management utility for creating and signing certificates.
"""

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from datetime import datetime, timedelta
import logging
from typing import Optional, Tuple
from pathlib import Path
import hashlib

logger = logging.getLogger(__name__)

class CertificateManager:
    def __init__(self):
        """Initialize CertificateManager."""
        self.key_size = 2048
        self.public_exponent = 65537

    def generate_private_key(self) -> rsa.RSAPrivateKey:
        """
        Generate a new RSA private key.

        Returns:
            RSAPrivateKey: Generated private key
        """
        return rsa.generate_private_key(
            public_exponent=self.public_exponent,
            key_size=self.key_size
        )

    def create_certificate(
        self,
        private_key: rsa.RSAPrivateKey,
        common_name: str,
        country: str,
        state: str,
        locality: str,
        organization: str,
        valid_days: int = 365,
        code_signing: bool = False
    ) -> x509.Certificate:
        """
        Create a self-signed certificate.

        Args:
            private_key: RSA private key
            common_name: Certificate common name
            country: Country code
            state: State or province
            locality: Locality
            organization: Organization name
            valid_days: Certificate validity in days
            code_signing: Whether to create a code signing certificate

        Returns:
            Certificate: Generated certificate
        """
        try:
            public_key = private_key.public_key()

            # Create certificate subject and issuer
            subject = issuer = x509.Name([
                x509.NameAttribute(NameOID.COMMON_NAME, common_name),
                x509.NameAttribute(NameOID.COUNTRY_NAME, country),
                x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state),
                x509.NameAttribute(NameOID.LOCALITY_NAME, locality),
                x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
            ])

            # Set validity period
            now = datetime.utcnow()
            cert_builder = x509.CertificateBuilder().subject_name(
                subject
            ).issuer_name(
                issuer
            ).public_key(
                public_key
            ).serial_number(
                x509.random_serial_number()
            ).not_valid_before(
                now
            ).not_valid_after(
                now + timedelta(days=valid_days)
            )

            # Add Basic Constraints extension
            cert_builder = cert_builder.add_extension(
                x509.BasicConstraints(ca=True if code_signing else False, path_length=None),
                critical=True
            )

            # Add Key Usage extension
            key_usage = x509.KeyUsage(
                digital_signature=True,
                content_commitment=False,
                key_encipherment=False if code_signing else True,
                data_encipherment=False,
                key_agreement=False,
                key_cert_sign=code_signing,
                crl_sign=code_signing,
                encipher_only=False,
                decipher_only=False
            )
            cert_builder = cert_builder.add_extension(key_usage, critical=True)

            # Add Extended Key Usage extension for code signing
            if code_signing:
                cert_builder = cert_builder.add_extension(
                    x509.ExtendedKeyUsage([x509.oid.ExtendedKeyUsageOID.CODE_SIGNING]),
                    critical=True
                )

            # Sign the certificate with SHA256
            certificate = cert_builder.sign(
                private_key=private_key,
                algorithm=hashes.SHA256()
            )

            return certificate

        except Exception as e:
            logger.error(f"Failed to create certificate: {str(e)}")
            raise

    def sign_executable(
        self,
        executable_path: str,
        certificate: x509.Certificate,
        private_key: rsa.RSAPrivateKey,
        signature_path: Optional[str] = None
    ) -> Path:
        """
        Sign an executable file with a code signing certificate.

        Args:
            executable_path: Path to the executable file
            certificate: Code signing certificate
            private_key: Private key associated with the certificate
            signature_path: Optional path to save the signature

        Returns:
            Path: Path to the signature file
        """
        try:
            # Read executable file
            with open(executable_path, 'rb') as f:
                executable_data = f.read()

            # Calculate file hash
            file_hash = hashlib.sha256(executable_data).digest()

            # Sign the hash
            signature = private_key.sign(
                file_hash,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )

            # Generate default signature path if not provided
            if signature_path is None:
                signature_path = f"{executable_path}.sig"

            # Save signature
            sig_path = Path(signature_path)
            with open(sig_path, 'wb') as f:
                f.write(signature)

            return sig_path

        except Exception as e:
            logger.error(f"Failed to sign executable: {str(e)}")
            raise

    def verify_executable(
        self,
        executable_path: str,
        signature_path: str,
        certificate: x509.Certificate
    ) -> bool:
        """
        Verify an executable's signature using a certificate.

        Args:
            executable_path: Path to the executable file
            signature_path: Path to the signature file
            certificate: Certificate used for verification

        Returns:
            bool: True if signature is valid
        """
        try:
            # Read executable file
            with open(executable_path, 'rb') as f:
                executable_data = f.read()

            # Calculate file hash
            file_hash = hashlib.sha256(executable_data).digest()

            # Read signature
            with open(signature_path, 'rb') as f:
                signature = f.read()

            # Verify signature
            public_key = certificate.public_key()
            try:
                public_key.verify(
                    signature,
                    file_hash,
                    padding.PSS(
                        mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH
                    ),
                    hashes.SHA256()
                )
                return True
            except Exception:
                return False

        except Exception as e:
            logger.error(f"Signature verification failed: {str(e)}")
            return False

    def save_certificate(
        self,
        cert: x509.Certificate,
        private_key: rsa.RSAPrivateKey,
        cert_path: str,
        key_path: str,
        key_password: Optional[bytes] = None
    ) -> Tuple[Path, Path]:
        """
        Save certificate and private key to files.

        Args:
            cert: Certificate to save
            private_key: Private key to save
            cert_path: Certificate file path
            key_path: Private key file path
            key_password: Optional password to encrypt the private key

        Returns:
            Tuple[Path, Path]: Paths to saved certificate and key files
        """
        try:
            # Save certificate
            cert_bytes = cert.public_bytes(serialization.Encoding.PEM)
            cert_path_obj = Path(cert_path)
            with open(cert_path_obj, 'wb') as f:
                f.write(cert_bytes)

            # Save private key
            encryption = (
                serialization.BestAvailableEncryption(key_password)
                if key_password else serialization.NoEncryption()
            )
            key_bytes = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=encryption
            )
            key_path_obj = Path(key_path)
            with open(key_path_obj, 'wb') as f:
                f.write(key_bytes)

            return cert_path_obj, key_path_obj

        except Exception as e:
            logger.error(f"Failed to save certificate: {str(e)}")
            raise