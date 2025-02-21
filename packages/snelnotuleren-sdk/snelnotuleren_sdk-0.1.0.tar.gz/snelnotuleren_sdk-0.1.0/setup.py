from setuptools import setup, find_packages

setup(
    name="snelnotuleren-sdk",
    version="0.1.0",
    author="Niels van der Werf",
    author_email="niels1214@gmail.com",
    description="Official Python SDK for the Snelnotuleren API",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0"
    ],
    python_requires=">=3.7",
)