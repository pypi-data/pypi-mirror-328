from slidge import entrypoint
from slidge.util.util import get_version  # noqa: F401

# import everything for automatic subclasses discovery by slidge core
from . import command, contact, gateway, group, session


def main():
    entrypoint("matridge")


__all__ = "session", "gateway", "contact", "group", "command", "main"

__version__ = "v0.2.0"
