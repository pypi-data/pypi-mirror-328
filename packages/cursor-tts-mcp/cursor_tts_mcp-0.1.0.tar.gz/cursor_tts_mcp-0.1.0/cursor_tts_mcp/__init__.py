"""
Cursor TTS MCP Server
A Text-to-Speech MCP server for Cursor IDE that converts all AI responses to speech automatically.
"""

from .server import TTSServer, main

__version__ = "0.1.0"
__all__ = ["TTSServer", "main"] 