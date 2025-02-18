"""
Database Personal Assistant (DBPA) - A natural language interface for database management.
"""

from setuptools import setup, find_packages

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dbpa",
    version="0.2.0",
    author="Achim Dehnert",
    author_email="achim@example.com",
    description="Database Personal Assistant - An AI-powered database management system with advanced text-to-SQL capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/achimdehnert/dbpa",
    project_urls={
        "Homepage": "https://github.com/achimdehnert/dbpa",
        "Documentation": "https://github.com/achimdehnert/dbpa/docs",
        "Repository": "https://github.com/achimdehnert/dbpa.git",
        "Issues": "https://github.com/achimdehnert/dbpa/issues",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={
        "dbpa": ["py.typed"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    python_requires=">=3.8",
    install_requires=[
        "sqlalchemy>=1.4.0",
        "sentence-transformers>=2.3.1",
        "faiss-cpu>=1.7.4",
        "pydantic>=2.6.1",
        "streamlit>=1.32.0",
        "torch>=2.0.0",
        "typing-extensions>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "isort>=5.0",
            "mypy>=0.900",
            "ruff>=0.0.1",
            "robotframework>=6.0",
        ],
    },
    keywords=["database", "sql", "ai", "nlp", "text-to-sql", "schema-analysis"],
)
