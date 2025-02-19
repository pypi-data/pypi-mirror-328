# HealthScribe

A Python package for medical scribing using AWS Transcribe Medical service.

## Overview

HealthScribe is a package focused on the healthcare domain. It enables medical scribing by transcribing audio files (e.g., doctor-patient conversations) using AWS Transcribe Medical service. The package uploads the provided audio file to an S3 bucket, starts a transcription job, and retrieves a summary from the job's JSON output.

## Installation

Clone the repository and install using pip:

```bash
pip install .
```

## Usage

You can use the command-line interface:

```bash
healthscribe-cli <audio_file> <job_name> <s3_bucket> [--s3_key <s3_key>]
```

For example:

```bash
healthscribe-cli conversation.wav myJob my-s3-bucket
```

## AWS Authentication

HealthScribe uses boto3 for AWS interactions. It supports AWS credential configuration via environment variables. Set the following environment variables as needed:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_SESSION_TOKEN (optional)
- AWS_REGION (default is us-east-1)

If the credentials are not provided, boto3 will use the default AWS credential provider chain.

## Folder Structure

The project has the following structure:

```
workspace/
├── setup.py
├── README.md
└── healthscribe/
    ├── __init__.py
    ├── cli.py
    ├── transcribe.py
    └── aws_auth.py
```

## License

This project is licensed under the MIT License.
