"""
A simple application
"""
from __future__ import annotations

import sys
from . import app

# TODO: use try/except ImportError when
# https://github.com/python/mypy/issues/1393 is fixed
if sys.version_info < (3, 10):
    # compatibility for python <3.10
    import importlib_metadata as metadata
else:
    from importlib import metadata


module_metadata = metadata.metadata("anymailer")

__author__ = f"{module_metadata['Author']} <{module_metadata['Author-email']}>"
__version__ = module_metadata["Version"]
__version_info__ = tuple([int(num) for num in __version__.split(".")])


all = [app]

# # email_provider_switcher/__init__.py
# # from email_provider_switcher.mailer import Mailer
# # from email_provider_switcher.config import load_config

# # config = load_config()


# def send_email(to: str, subject: str, body: str, provider: str | None = None) -> None:
#     if not property:
#         # if provider is None:
#         return None
#         # provider = config['email_provider']

#     # mailer = Mailer(provider=provider)
#     # mailer.send_email(to, subject, body)
