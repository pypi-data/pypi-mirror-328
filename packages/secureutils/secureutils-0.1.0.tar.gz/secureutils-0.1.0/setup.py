from setuptools import setup, find_packages

setup(
    name="secureutils",
    version="1.0.0",
    packages=find_packages(),
    author="zxc4we",
    author_email="zxc4we028@gmail.com",
    install_requires=[
        'cryptography',
        'requests',
        'urllib3'
    ],
    description="A Python utility module for secure requests, file operations, certificate management, and SQLite handling",
    python_requires='>=3.7',
)
