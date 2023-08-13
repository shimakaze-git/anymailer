"""Sphinx configuration."""
project = "anymailer"
author = "shimakaze-git"
copyright = "2023, shimakaze-git"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
