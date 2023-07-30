# anymailer

Email Provider Switcher is a library designed to make it easy to migrate between different email delivery systems and services.

A simple application

## Developing

Run `make` for help

    make install             # Run `poetry install`
    make showdeps            # run poetry to show deps
    make lint                # Runs bandit and black in check mode
    make format              # Formats you code with Black
    make test                # run pytest with coverage
    make build               # run `poetry build` to build source distribution and wheel

make pyinstaller # Create a binary executable using pyinstaller

## Installation

```bash
$ pip install email-provider-switcher
```

## Usage

Here's an example of how to use Email Migrator:

```python
from email_provider_switcher import send_email

send_email("to@example.com", "test mail subject", "test mail content")
```

## Configuration Options

- option1: Description
- option2: Description

## Supported Email Services

- Service 1
- Service 2
- Service 3

## For Developers

Please refer to the following links for contribution guidelines and developer information:

- Contribution Guidelines
- Development Guide

## License

This project is licensed under the MIT License.

## Authors and Contributors

- Author1 (email@example.com)
- Author2 (email@example.com)

Please customize the contents according to your project's features and settings. Use this template as a starting point to create an English README and publish it on GitHub.
