import subprocess
import tempfile
import os
import sys
import json
import ast
from typing import List, Dict, Any, Optional, Set
from dataclasses import dataclass
from pathlib import Path
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from enum import Enum
import shutil
import time

# Import our custom security logic from security.py
from .security import analyze_code_security
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SecurityLevel(Enum):
    """Security level classifications for findings."""
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"
    ERROR = "ERROR"  # For tool execution or parsing errors

@dataclass
class SecurityFinding:
    """Represents a security finding from any tool."""
    tool: str
    level: SecurityLevel
    message: str
    line_number: Optional[int] = None
    code_snippet: Optional[str] = None
    recommendation: Optional[str] = None

class ExternalToolConfig:
    """Configuration for external security tools."""
    
    # Required external tools
    REQUIRED_TOOLS = {
        "bandit": "Security scanner for Python code",
        "flake8": "Code style and error checker",
        "mypy": "Static type checker",
        "pylint": "Code analysis tool",
    }
    
    # Command timeouts in seconds
    TOOL_TIMEOUTS = {
        "bandit": 30,
        "flake8": 20,
        "mypy": 30,
        "pylint": 30,
        "safety": 20
    }
    
    # Tool-specific arguments
    TOOL_ARGS = {
        "bandit": ["-f", "json", "-q", "-ll"],
        "flake8": [],
        "mypy": ["--no-error-summary", "--show-error-codes"],
        "pylint": ["--output-format=json"],
    }

class CodeValidator:
    """Handles validation and security checking of Python code."""
    
    def __init__(self, max_code_length: int = 50000):
        self.temp_dir: Optional[Path] = None
        self.requirements_file: Optional[Path] = None
        self.max_code_length = max_code_length
        self.verify_dependencies()

    def verify_dependencies(self) -> None:
        """Verify all required external tools are installed."""
        missing_tools = []
        for tool in ExternalToolConfig.REQUIRED_TOOLS:
            if not shutil.which(tool):
                missing_tools.append(tool)
        
        if missing_tools:
            tools_str = ", ".join(missing_tools)
            raise EnvironmentError(
                f"Required tools not found: {tools_str}. Please install missing dependencies."
            )

    def validate_python_code(self, code: str) -> List[SecurityFinding]:
        """Check if the provided code is valid Python syntax and within size limits."""
        findings = []
        if len(code) > self.max_code_length:
            findings.append(SecurityFinding(
                tool="validator",
                level=SecurityLevel.CRITICAL,
                message=f"Code length exceeds maximum allowed size ({self.max_code_length} characters)."
            ))
            return findings

        try:
            compile(code, "<string>", "exec")
        except SyntaxError as e:
            findings.append(SecurityFinding(
                tool="validator",
                level=SecurityLevel.CRITICAL,
                message=f"Syntax error: {e.msg}",
                line_number=e.lineno,
                code_snippet=str(e.text).strip() if e.text else None,
                recommendation="Fix the syntax error before submission."
            ))
        return findings

    def create_temp_environment(self, code: str) -> Path:
        """Create a temporary environment for code analysis."""
        self.temp_dir = Path(tempfile.mkdtemp(prefix="security_check_"))
        code_file = self.temp_dir / "code_to_check.py"
        requirements_file = self.temp_dir / "requirements.txt"
        
        # Write code to file
        code_file.write_text(code)
        
        # Extract and write requirements if present
        self._extract_requirements(code, requirements_file)
        if requirements_file.exists() and requirements_file.stat().st_size > 0:
            self.requirements_file = requirements_file
        else:
            self.requirements_file = None
        
        return code_file

    def _extract_requirements(self, code: str, requirements_file: Path) -> None:
        """Extract import statements and create a requirements.txt file."""
        try:
            tree = ast.parse(code)
            imports: Set[str] = set()
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for name in node.names:
                        imports.add(name.name.split('.')[0])
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.add(node.module.split('.')[0])
            
            # Filter out standard library modules
            imports = {imp for imp in imports if not self._is_stdlib_module(imp)}
            
            if imports:
                requirements_file.write_text('\n'.join(sorted(imports)))
        except Exception as e:
            logger.warning(f"Failed to extract requirements: {e}")

    @staticmethod
    def _is_stdlib_module(module_name: str) -> bool:
        """Check if a module is part of the Python standard library."""
        try:
            module_spec = __import__(module_name).__spec__
            return module_spec is not None and 'site-packages' not in str(module_spec.origin)
        except (ImportError, AttributeError):
            return False

    def cleanup(self) -> None:
        """Clean up temporary files and directories."""
        if self.temp_dir and self.temp_dir.exists():
            try:
                shutil.rmtree(self.temp_dir)
            except Exception as e:
                logger.error(f"Failed to cleanup temporary directory: {e}")

    def _run_tool(self, command: List[str], timeout: int) -> subprocess.CompletedProcess:
        """Run an external tool with timeout and error handling."""
        try:
            logger.info(f"Running command: {' '.join(command)}")
            return subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=timeout,
                check=False
            )
        except subprocess.TimeoutExpired:
            raise TimeoutError(f"Tool execution timed out after {timeout} seconds")

    def run_security_checks(self, code: str) -> Dict[str, List[SecurityFinding]]:
        """
        Run comprehensive security checks using multiple tools in parallel.
        Returns a dictionary mapping tool names to their SecurityFindings.
        """
        findings: Dict[str, List[SecurityFinding]] = {}

        # First, validate syntax and code length
        syntax_findings = self.validate_python_code(code)
        if syntax_findings:
            findings["syntax"] = syntax_findings
            # If critical syntax issues exist, skip further analysis.
            return findings

        # Create temporary environment
        code_file = self.create_temp_environment(code)
        
        # Run external tools concurrently
        with ThreadPoolExecutor() as executor:
            future_to_tool = {
                executor.submit(self._run_tool_checks, tool, code_file): tool
                for tool in ExternalToolConfig.REQUIRED_TOOLS
            }
            for future in as_completed(future_to_tool):
                tool = future_to_tool[future]
                try:
                    findings[tool] = future.result()
                except Exception as e:
                    logger.error(f"Error running {tool}: {e}")
                    findings[tool] = [
                        SecurityFinding(
                            tool=tool,
                            level=SecurityLevel.ERROR,
                            message=f"Tool execution failed: {str(e)}"
                        )
                    ]
        
        # Instead of internal custom checks, import and run our custom logic from security.py
        findings["custom"] = self._run_external_custom_checks(code)
        
        self.cleanup()
        return findings

    def _run_tool_checks(self, tool: str, code_file: Path) -> List[SecurityFinding]:
        """Run a specific security tool and parse its output."""
        # For safety, if a requirements file exists, use that.
        file_to_check = code_file
        if tool == "safety" and self.requirements_file:
            file_to_check = self.requirements_file
        elif tool == "safety" and not self.requirements_file:
            return [SecurityFinding(
                tool=tool,
                level=SecurityLevel.INFO,
                message="No external dependencies found; skipping safety check."
            )]
        
        command = [tool] + ExternalToolConfig.TOOL_ARGS.get(tool, []) + [str(file_to_check)]
        timeout = ExternalToolConfig.TOOL_TIMEOUTS.get(tool, 30)
        
        result = self._run_tool(command, timeout)
        return self._parse_tool_output(tool, result.stdout, result.stderr)

    def _parse_tool_output(self, tool: str, stdout: str, stderr: str) -> List[SecurityFinding]:
        """Parse tool output into SecurityFindings."""
        findings = []
        try:
            if tool == "bandit":
                findings.extend(self._parse_bandit_output(stdout))
            elif tool == "flake8":
                findings.extend(self._parse_flake8_output(stdout))
            elif tool == "mypy":
                findings.extend(self._parse_mypy_output(stdout))
            elif tool == "pylint":
                findings.extend(self._parse_pylint_output(stdout))
            elif tool == "safety":
                findings.extend(self._parse_safety_output(stdout))
            # Log any stderr as an informational finding.
            if stderr.strip():
                findings.append(SecurityFinding(
                    tool=tool,
                    level=SecurityLevel.INFO,
                    message=f"Stderr: {stderr.strip()}"
                ))
        except Exception as e:
            logger.error(f"Error parsing {tool} output: {e}")
            findings.append(
                SecurityFinding(
                    tool=tool,
                    level=SecurityLevel.ERROR,
                    message=f"Failed to parse tool output: {str(e)}"
                )
            )
        return findings

    def _parse_bandit_output(self, stdout: str) -> List[SecurityFinding]:
        findings = []
        try:
            data = json.loads(stdout)
            for item in data.get("results", []):
                findings.append(SecurityFinding(
                    tool="bandit",
                    level=SecurityLevel[item.get("issue_severity", "LOW").upper()] 
                        if item.get("issue_severity", "LOW").upper() in SecurityLevel.__members__ 
                        else SecurityLevel.LOW,
                    message=item.get("issue_text", "No message provided"),
                    line_number=item.get("line_number"),
                    recommendation=item.get("more_info")
                ))
        except Exception as e:
            raise ValueError(f"Bandit output parsing error: {e}")
        return findings

    def _parse_flake8_output(self, stdout: str) -> List[SecurityFinding]:
        if not stdout.strip():
            return []  # No issues found.
        findings = []
        try:
            # Add debug logging
            logger.debug(f"Raw flake8 output: {stdout[:200]}...")  # Log first 200 chars
            
            # Try to handle both JSON and text output formats
            if stdout.startswith('[') or stdout.startswith('{'):
                data = json.loads(stdout)
                if isinstance(data, dict):
                    for filename, errors in data.items():
                        for error in errors:
                            findings.append(SecurityFinding(
                                tool="flake8",
                                level=SecurityLevel.LOW,
                                message=error.get("text", "No message provided"),
                                line_number=error.get("line_number")
                            ))
                elif isinstance(data, list):
                    for error in data:
                        findings.append(SecurityFinding(
                            tool="flake8",
                            level=SecurityLevel.LOW,
                            message=error.get("text", "No message provided"),
                            line_number=error.get("line_number")
                        ))
            else:
                # Handle text format if JSON parsing fails
                for line in stdout.splitlines():
                    if line.strip():
                        # Parse flake8's default format: "file:line:col: error_code error_message"
                        parts = line.split(':', 3)
                        if len(parts) >= 4:
                            findings.append(SecurityFinding(
                                tool="flake8",
                                level=SecurityLevel.LOW,
                                message=parts[3].strip(),
                                line_number=int(parts[1]) if parts[1].strip().isdigit() else None
                            ))
        except Exception as e:
            logger.error(f"flake8 output parsing error: {e}\nOutput was: {stdout[:200]}")
            raise ValueError(f"flake8 output parsing error: {e}")
        return findings

    def _parse_safety_output(self, stdout: str) -> List[SecurityFinding]:
        if not stdout.strip():
            return []  # No issues found
        findings = []
        try:
            # Add debug logging
            logger.debug(f"Raw safety output: {stdout[:200]}...")  # Log first 200 chars
            
            # Try to handle both JSON and text output formats
            if stdout.startswith('[') or stdout.startswith('{'):
                data = json.loads(stdout)
                for vuln in data.get("vulnerabilities", []):
                    findings.append(SecurityFinding(
                        tool="safety",
                        level=SecurityLevel.HIGH,
                        message=vuln.get("advisory", "No advisory provided"),
                        recommendation=vuln.get("suggested_remediation")
                    ))
            else:
                # Handle text format if JSON parsing fails
                for line in stdout.splitlines():
                    if line.strip() and not line.startswith(('╭', '╰', '│')):  # Skip safety's ASCII art borders
                        findings.append(SecurityFinding(
                            tool="safety",
                            level=SecurityLevel.HIGH,
                            message=line.strip()
                        ))
        except Exception as e:
            logger.error(f"Safety output parsing error: {e}\nOutput was: {stdout[:200]}")
            raise ValueError(f"Safety output parsing error: {e}")
        return findings


    def _parse_mypy_output(self, stdout: str) -> List[SecurityFinding]:
        findings = []
        try:
            # Mypy output might be JSON; if not, fallback to line-oriented messages.
            data = json.loads(stdout)
            for error in data.get("errors", []):
                findings.append(SecurityFinding(
                    tool="mypy",
                    level=SecurityLevel.MEDIUM,
                    message=error.get("message", "No message provided"),
                    line_number=error.get("line")
                ))
        except Exception:
            for line in stdout.splitlines():
                if line.strip():
                    findings.append(SecurityFinding(
                        tool="mypy",
                        level=SecurityLevel.MEDIUM,
                        message=line.strip()
                    ))
        return findings

    def _parse_pylint_output(self, stdout: str) -> List[SecurityFinding]:
        findings = []
        try:
            data = json.loads(stdout)
            for msg in data:
                findings.append(SecurityFinding(
                    tool="pylint",
                    level=SecurityLevel[msg.get("type", "info").upper()] 
                        if msg.get("type", "info").upper() in SecurityLevel.__members__ 
                        else SecurityLevel.INFO,
                    message=msg.get("message", "No message provided"),
                    line_number=msg.get("line")
                ))
        except Exception as e:
            raise ValueError(f"pylint output parsing error: {e}")
        return findings

    def _run_external_custom_checks(self, code: str) -> List[SecurityFinding]:
        """
        Run custom security analysis by importing our logic from security.py.
        Converts SecurityIssue objects into SecurityFinding objects.
        """
        issues = analyze_code_security(code)
        # Map custom severity strings to our SecurityLevel enum.
        severity_mapping = {
            'high': SecurityLevel.CRITICAL,
            'medium': SecurityLevel.HIGH,
            'low': SecurityLevel.LOW
        }
        findings = [
            SecurityFinding(
                tool="custom",
                level=severity_mapping.get(issue.severity.lower(), SecurityLevel.LOW),
                message=issue.message,
                line_number=issue.line_number
            )
            for issue in issues
        ]
        return findings

    def generate_report(self, findings: Dict[str, List[SecurityFinding]]) -> str:
        """Generate a comprehensive security report from all findings."""
        report = ["Security Analysis Report", "=" * 50, ""]
        
        # Group findings by severity
        severity_groups: Dict[SecurityLevel, List[SecurityFinding]] = {
            level: [] for level in SecurityLevel
        }
        
        for tool_findings in findings.values():
            for finding in tool_findings:
                severity_groups[finding.level].append(finding)
        
        # Generate report sections by severity
        for level in SecurityLevel:
            level_findings = severity_groups[level]
            if level_findings:
                report.append(f"\n{level.value} Findings:")
                report.append("-" * 20)
                
                for finding in level_findings:
                    report.append(f"Tool: {finding.tool}")
                    report.append(f"Message: {finding.message}")
                    if finding.line_number:
                        report.append(f"Line: {finding.line_number}")
                    if finding.code_snippet:
                        report.append(f"Code: {finding.code_snippet}")
                    if finding.recommendation:
                        report.append(f"Recommendation: {finding.recommendation}")
                    report.append("")
        
        return "\n".join(report)

def main():
    """Main function for command-line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Enterprise Python Code Security Checker")
    parser.add_argument("file", help="Python file to check")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    args = parser.parse_args()
    
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            code = f.read()
        
        validator = CodeValidator()
        findings = validator.run_security_checks(code)
        
        if args.json:
            # Custom JSON serialization for SecurityFinding objects
            def serialize(o):
                if isinstance(o, Enum):
                    return o.value
                if hasattr(o, '__dict__'):
                    return o.__dict__
                return str(o)
            print(json.dumps(findings, default=serialize, indent=2))
        else:
            print(validator.generate_report(findings))
            
    except Exception as e:
        logger.error(f"Error during security check: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
