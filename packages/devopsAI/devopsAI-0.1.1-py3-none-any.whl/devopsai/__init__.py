"""DevOpsAI - A utility for executing system commands via API."""

from .core import execute_commands, extract_commands, call_api

__version__ = "0.1.1"
__all__ = ["execute_commands", "extract_commands", "call_api"]