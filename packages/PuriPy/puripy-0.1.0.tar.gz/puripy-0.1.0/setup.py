from setuptools import setup, find_packages

setup(
    name="PyPurify",
    version="0.1.0",
    author="Nicholas Davidson",
    author_email="nicholas@purify-ai.com",
    description="A secure Python sandbox validation library for AI/ML playgrounds that purifies code.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ndavidson19/PyPurify",
    packages=find_packages(),
    install_requires=[
        "bandit",
        "flake8",
        "mypy",
        "pylint",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.9',
)
