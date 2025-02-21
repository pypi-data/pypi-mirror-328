"""Setup script for manticore-cockroachdb."""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="manticore-cockroachdb",
    version="0.1.0",
    author="Manticore Technologies",
    author_email="dev@manticoretech.com",
    description="High-performance CockroachDB client library with connection pooling, migrations, and transaction management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://manticoretech.com",
    project_urls={
        "Documentation": "https://docs.manticoretech.com/cockroachdb",
        "Source": "https://github.com/manticore-tech/manticore-cockroachdb",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    python_requires=">=3.8",
    install_requires=[
        "psycopg[binary]>=3.1.18",
        "psycopg-pool>=3.2.1",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-asyncio>=0.23.5",
            "pytest-cov>=4.1.0",
            "black>=24.1.0",
            "isort>=5.13.0",
            "mypy>=1.8.0",
            "build>=1.0.0",
            "twine>=4.0.0",
        ],
    },
)
