"""
This is the utils module for the kvell_extraction package.
"""

import importlib


def import_package(name, package=None):
    """
    Import a package.
    """
    try:
        module = importlib.import_module(name, package=package)
        return module
    except ModuleNotFoundError:
        return None
