"""
Test suite for SecureUtils package.
Provides unit tests for HTTP requests, file operations, certificate management, and SQLite handling.
"""

import unittest
import logging

# Configure logging for tests
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Disable overly verbose logging during tests
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('requests').setLevel(logging.WARNING)

def run_all_tests():
    """Run all test cases in the test suite."""
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests')
    test_runner = unittest.TextTestRunner(verbosity=2)
    return test_runner.run(test_suite)

if __name__ == '__main__':
    run_all_tests()
