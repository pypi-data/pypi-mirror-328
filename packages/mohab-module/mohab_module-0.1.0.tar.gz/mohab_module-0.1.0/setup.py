from setuptools import setup, find_packages

setup(
    name="mohab_module",  # Package name (should be unique on PyPI)
    version="0.1.0",  # Package version
    packages=find_packages(),  # Automatically finds modules
    install_requires=[],  # Dependencies (if any)
    author="mohab youssef",
    author_email="your.email@example.com",
    description="A simple greeting module",
    long_description=open("README.md").read(),  # Read from README
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_module",  # GitHub repo
    python_requires=">=3.6",  # Minimum Python version
)
