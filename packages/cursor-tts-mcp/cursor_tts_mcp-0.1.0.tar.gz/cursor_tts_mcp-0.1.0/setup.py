from setuptools import setup, find_packages

setup(
    name="cursor-tts-mcp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Flask>=3.0.2",
        "gTTS>=2.5.1",
        "pygame>=2.5.2",
        "python-dotenv>=1.0.1",
    ],
    entry_points={
        "console_scripts": [
            "cursor-tts-mcp=cursor_tts_mcp.server:main",
        ],
    },
    author="Cursor Community",
    description="A Text-to-Speech MCP server for Cursor IDE",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cursor-community/cursor-tts-mcp",
    include_package_data=True,
    package_data={
        "cursor_tts_mcp": ["templates/*"],
    },
) 