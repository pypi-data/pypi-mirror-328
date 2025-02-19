# PuriPy Security Validator

A fast, comprehensive security validation system for Python code, designed to perform pre-execution security checks in cloud environments. This tool helps reduce costs and latency by validating code before spinning up sandbox VMs.

## Overview

The PuriPy Security Validator provides a robust first line of defense for environments that execute arbitrary Python code. It performs quick security and syntax validation before committing resources to full sandbox execution, helping to:

- Reduce costs by catching issues before VM provisioning
- Minimize latency by failing fast on problematic code
- Prevent common security vulnerabilities
- Validate code structure and dependencies

## Key Features

- Fast preliminary security validation
- Comprehensive static code analysis
- Multi-tool security scanning
- Parallel tool execution for speed
- Configurable security policies
- Dependency analysis and validation
- Support for popular data science libraries
- Detailed security reports

## Architecture

The system consists of three main components:

1. **FastSecurityAPI** (`security_api.py`)
   - Quick validation interface
   - Security policy enforcement
   - Execution policy decisions

2. **CodeValidator** (`security_validator.py`)
   - Comprehensive code analysis
   - External tool integration
   - Parallel security scanning
   - Detailed report generation

3. **UnifiedSecurityVisitor** (`security.py`)
   - AST-based code analysis
   - Security rule enforcement
   - Vulnerability detection

## Installation

```bash
pip install puripy
# Install required dependencies
pip install -r requirements.txt
```

**If editing the package, install in editable mode:**

```bash
git clone https://github.com/ndavidson19/PyPurify
pip install -e .
```

## Usage

### Basic Usage

```python
from puripy import FastSecurityAPI

api = FastSecurityAPI()
result = api.validate_code(code)

print(f"Validation Result: {result.result}")
print(f"Message: {result.message}")
print(f"Execution Policy: {result.execution_policy}")
```

### Command Line Usage

```bash
python security_validator.py path/to/code.py --json
```

## Security Checks

The validator performs multiple levels of security checks:

### 1. Quick Checks
- Syntax validation
- Code size limits
- Blocked imports
- Dangerous function calls
- Known vulnerability patterns

### 2. Comprehensive Analysis
- Static code analysis
- Dependency scanning
- Security vulnerability detection
- Style and quality checks
- Custom security rules

### 3. Tool Integration
- Bandit (security scanner)
- Flake8 (style checker)
- MyPy (type checker)
- Pylint (code analysis)
- Custom security tools

## Security Policies

Three levels of execution policies:

1. `ALLOW`: Code passes all security checks
2. `ALLOW_WITH_MONITORING`: Code requires runtime monitoring
3. `BLOCKED`: Code contains security violations

## Allowed Libraries

The system maintains a whitelist of common data science and analysis libraries:
- pandas, numpy, scipy
- sklearn, tensorflow, torch
- matplotlib, seaborn
- nltk, spacy, transformers
- Standard Python libraries

## Configuration

Security rules can be configured through the `SecurityConfig` class:

```python
from security import SecurityConfig

config = SecurityConfig()
config.BLOCKED_IMPORTS.add('dangerous_module')
config.DANGEROUS_FUNCTIONS.add('risky_function')
```

## Response Format

```python
@dataclass
class CodeValidationResponse:
    result: ValidationResult
    message: str
    details: Optional[List[str]]
    line_numbers: Optional[List[int]]
    execution_policy: Optional[ExecutionPolicy]
```

## Best Practices

1. Always run in fast mode first for quick validation
2. Use parallel tool execution for larger codebases
3. Configure security rules based on your environment
4. Monitor and log validation results
5. Update security rules regularly

## Limitations

- Cannot catch all runtime security issues
- Some false positives in security detection
- Limited to Python code analysis
- Requires external tool installation
- May miss sophisticated attack vectors

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Support

For issues and feature requests, please create an issue in the repository.