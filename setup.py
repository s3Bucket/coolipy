from setuptools import setup, find_packages

setup(
    name="coolipy",
    version="0.4.9",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author="Colin Schmidt",
    description="Python SDK for Coolify API",
    python_requires=">=3.8",
)
