from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple, Set
from enum import Enum
import ast
import concurrent.futures
import logging
from pathlib import Path
import tempfile

from .security import (
    SecurityConfig, 
    ExecutionPolicy,
    analyze_code_security,
    UnifiedSecurityVisitor
)
from .security_api import CodeValidator, SecurityLevel, SecurityFinding, ExternalToolConfig

class ValidationResult(Enum):
    ALLOWED = "allowed"
    ALLOWED_WITH_MONITORING = "allowed_with_monitoring"
    BLOCKED = "blocked"
    SYNTAX_ERROR = "syntax_error"

@dataclass
class CodeValidationResponse:
    result: ValidationResult
    message: str
    details: Optional[List[str]] = None
    line_numbers: Optional[List[int]] = None
    execution_policy: Optional[ExecutionPolicy] = None

class FastSecurityAPI:
    """
    Fast API for code security validation combining CodeValidator and SecurityConfig checks.
    """
    
    # Essential tools for quick validation
    FAST_CHECK_TOOLS = {
        "bandit",  # For security checks
        "flake8"   # For quick syntax and style checks
    }
    
    ALLOWED_IMPORTS = {
        'pandas', 'numpy', 'math', 'statistics', 'datetime',
        'json', 'csv', 'random', 'typing', 'collections',
        'itertools', 'functools', 're', 'string', 'pytorch',
        'tensorflow', 'sklearn', 'keras', 'torch', 'torchvision',
        'transformers', 'nltk', 'spacy', 'gensim', 'fastai',
        'xgboost', 'lightgbm', 'catboost', 'cv2', 'pillow',
        'matplotlib', 'seaborn', 'plotly', 'dash'
    }

    def __init__(self):
        self.validator = CodeValidator()
        self.security_config = SecurityConfig()
        self.security_visitor = UnifiedSecurityVisitor(self.security_config)
        self.external_tools = ExternalToolConfig()

        self._configure_logging()

    def _configure_logging(self):
        """Configure minimal logging for essential messages only."""
        logging.basicConfig(
            level=logging.WARNING,
            format='%(levelname)s: %(message)s'
        )

    def _is_safe_import(self, node: ast.AST) -> bool:
        """Check if import is in the allowed list."""
        if isinstance(node, ast.Import):
            return all(alias.name.split('.')[0] in self.ALLOWED_IMPORTS 
                      for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            return node.module and node.module.split('.')[0] in self.ALLOWED_IMPORTS
        return False

    def _map_execution_policy_to_result(self, policy: ExecutionPolicy) -> ValidationResult:
        """Map ExecutionPolicy to ValidationResult."""
        policy_mapping = {
            ExecutionPolicy.ALLOW: ValidationResult.ALLOWED,
            ExecutionPolicy.ALLOW_WITH_FALCO: ValidationResult.ALLOWED_WITH_MONITORING,
            ExecutionPolicy.DENY: ValidationResult.BLOCKED
        }
        return policy_mapping.get(policy, ValidationResult.BLOCKED)

    def _check_immediate_security_violations(self, code: str) -> Optional[Tuple[ValidationResult, str, List[str], List[int]]]:
        """Perform quick security checks using SecurityConfig rules."""
        try:
            tree = ast.parse(code)
            self.security_visitor.visit(tree)
            issues = self.security_visitor.issues

            # Filter out issues for safe imports
            filtered_issues = []
            for issue in issues:
                if isinstance(issue.node, (ast.Import, ast.ImportFrom)):
                    if not self._is_safe_import(issue.node):
                        filtered_issues.append(issue)
                else:
                    filtered_issues.append(issue)

            # Check for immediate security violations
            high_severity_issues = [i for i in filtered_issues if i.severity == 'high']
            print(high_severity_issues)
            if high_severity_issues:
                return (
                    ValidationResult.BLOCKED,
                    "Code contains critical security violations",
                    ["Code contains restricted operations"],
                    [issue.line_number for issue in high_severity_issues]
                )
            return None
            
        except Exception as e:
            logging.error(f"Security check error: {e}")
            return None

    def _get_critical_findings(self, findings: Dict[str, List[SecurityFinding]]) -> List[SecurityFinding]:
        """Filter only critical and high-severity findings."""
        critical_findings = []
        for tool_findings in findings.values():
            for finding in tool_findings:
                if finding.level in {SecurityLevel.CRITICAL, SecurityLevel.HIGH}:
                    critical_findings.append(finding)
        return critical_findings

    def _process_style_findings(self, findings: Dict[str, List[SecurityFinding]]) -> List[str]:
        """Process and format style-related findings."""
        style_messages = []
        for tool, tool_findings in findings.items():
            if tool in {'flake8', 'pylint'}:
                for finding in tool_findings:
                    if finding.line_number:
                        style_messages.append(f"Line {finding.line_number}: {finding.message}")
                    else:
                        style_messages.append(finding.message)
        return style_messages if style_messages else None


    def _create_error_message(self, findings: List[SecurityFinding]) -> Tuple[str, List[str], List[int]]:
        """Create appropriate error messages based on finding type."""
        messages = []
        line_numbers = []
        
        syntax_findings = [f for f in findings if f.tool == "syntax"]
        if syntax_findings:
            # Detailed syntax error messages
            main_message = "Syntax validation failed"
            messages = [f"Line {f.line_number}: {f.message}" for f in syntax_findings if f.line_number]
            line_numbers = [f.line_number for f in syntax_findings if f.line_number]
        else:
            # Vague security messages
            main_message = "Code validation failed due to security concerns"
            messages = ["Code contains restricted operations"]
            line_numbers = [f.line_number for f in findings if f.line_number]
            
        return main_message, messages, line_numbers

    def validate_code(self, code: str, fast_mode: bool = True) -> CodeValidationResponse:
        """
        Validate code for syntax and security issues.
        
        Args:
            code: String containing Python code to analyze
            fast_mode: If True, only runs essential security checks
            
        Returns:
            CodeValidationResponse with validation result and appropriate messages
        """
        try:
            # First, quick syntax validation
            syntax_findings = self.validator.validate_python_code(code)
            if syntax_findings:
                main_msg, details, lines = self._create_error_message(syntax_findings)
                return CodeValidationResponse(
                    result=ValidationResult.SYNTAX_ERROR,
                    message=main_msg,
                    details=details,
                    line_numbers=lines
                )

            # Quick security check using SecurityConfig rules
            immediate_violation = self._check_immediate_security_violations(code)
            if immediate_violation:
                result, msg, details, lines = immediate_violation
                return CodeValidationResponse(
                    result=result,
                    message=msg,
                    details=details,
                    line_numbers=lines
                )

            # Run security analysis from security.py
            security_issues = analyze_code_security(code)
            policy = ExecutionPolicy.DENY if any(
                issue.severity in ['HIGH', 'CRITICAL'] for issue in security_issues
            ) else ExecutionPolicy.ALLOW
            result = self._map_execution_policy_to_result(policy)
            
            if result == ValidationResult.BLOCKED:
                return CodeValidationResponse(
                    result=result,
                    message="Code execution blocked due to security concerns",
                    details=["Code contains restricted operations"],
                    line_numbers=[issue.line_number for issue in security_issues],
                    execution_policy=policy
                )

            # Run essential tool checks if code passed initial security check
            if fast_mode:
                # Modify validator's required tools for fast checking
                original_tools = self.external_tools.REQUIRED_TOOLS.copy()
                self.external_tools.REQUIRED_TOOLS = {
                    tool: desc for tool, desc in original_tools.items()
                    if tool in self.FAST_CHECK_TOOLS
                }

            findings = self.validator.run_security_checks(code)
            style_details = self._process_style_findings(findings)

            # Restore original tools configuration if modified
            if fast_mode:
                self.external_tools.REQUIRED_TOOLS = original_tools

            # Check for critical findings
            critical_findings = self._get_critical_findings(findings)
            if critical_findings:
                main_msg, details, lines = self._create_error_message(critical_findings)
                return CodeValidationResponse(
                    result=ValidationResult.BLOCKED,
                    message=main_msg,
                    details=details,
                    line_numbers=lines,
                    execution_policy=ExecutionPolicy.DENY
                )

            return CodeValidationResponse(
                result=result,
                message="Code validation successful",
                details=style_details,
                execution_policy=policy
            )
            
        except Exception as e:
            return CodeValidationResponse(
                result=ValidationResult.BLOCKED,
                message=f"Validation error: {str(e)}",
                details=None,
                execution_policy=ExecutionPolicy.DENY
            )

def validate_code_file(file_path: str, fast_mode: bool = True) -> CodeValidationResponse:
    """Convenience function to validate code from a file."""
    try:
        with open(file_path, 'r') as f:
            code = f.read()
        api = FastSecurityAPI()
        return api.validate_code(code, fast_mode)
    except Exception as e:
        return CodeValidationResponse(
            result=ValidationResult.BLOCKED,
            message=f"File reading error: {str(e)}",
            details=None,
            execution_policy=ExecutionPolicy.DENY
        )

# Example usage
if __name__ == "__main__":
    sample_code = """
import os
import requests

def risky_function():
    os.system("echo hello")
    requests.get("http://example.com")
    """
    
    api = FastSecurityAPI()
    result = api.validate_code(sample_code)
    print(f"Validation Result: {result.result}")
    print(f"Message: {result.message}")
    print(f"Execution Policy: {result.execution_policy}")
    if result.details:
        print("Details:", "\n".join(result.details))
    if result.line_numbers:
        print("Line Numbers:", result.line_numbers)