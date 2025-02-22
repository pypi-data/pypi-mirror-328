# __init__.py
from .cli import main


def cli():
    """CLI entry point for neatoo"""
    main()


__all__ = ["cli"]
