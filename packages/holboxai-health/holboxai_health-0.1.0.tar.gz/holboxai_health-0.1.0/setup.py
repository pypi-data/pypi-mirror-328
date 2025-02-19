from setuptools import setup, find_packages

setup(
    name="holboxai_health",
    version="0.1.0",
    author="saurabh",
    author_email="saurabh.patil@holbox.ai",
    description="A package for medical scribing using AWS Transcribe for the healthcare domain",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "healthscribe-cli=holboxai_health.cli:main"
        ]
    }
)
