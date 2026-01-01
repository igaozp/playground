# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project for exploring the Claude AI Agent SDK. It's a learning/experimental project that demonstrates basic usage of the `claude-agent-sdk` package to interact with Claude models programmatically.

## Environment Setup

This project uses **uv** for Python package management and requires **Python 3.12+**.

### Initial Setup

```bash
# Install dependencies
uv sync

# Activate virtual environment (if needed manually)
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Environment Variables

The project uses a `.env` file for configuration. Key variables:

- `ANTHROPIC_BASE_URL` - API base URL (currently configured for DeepSeek compatibility)
- `ANTHROPIC_AUTH_TOKEN` - API authentication token
- `ANTHROPIC_MODEL` - Model identifier to use
- `ANTHROPIC_SMALL_FAST_MODEL` - Fallback model for simpler tasks
- `API_TIMEOUT_MS` - API request timeout in milliseconds
- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` - Disable telemetry

**Important:** The `.env` file contains API credentials. Never commit actual tokens to git.

## Running the Project

```bash
# Run the main script
uv run main

# Or with Python directly (after activating venv)
python main.py
```

## Project Structure

- `main.py` - Single entry point demonstrating `claude-agent-sdk` usage
- `pyproject.toml` - Project metadata and dependencies
- `uv.lock` - Locked dependency versions
- `.env` - Environment configuration (not committed)

## Key Dependencies

- **claude-agent-sdk** (>=0.1.17) - Official SDK for building Claude agents

## Development Notes

### API Configuration

The project is currently configured to use DeepSeek's API endpoint as an Anthropic-compatible alternative. The `ClaudeAgentOptions` in `main.py` configures:

- Custom system prompts
- Permission modes for file operations
- Working directory context

### Permission Modes

When using the SDK, `permission_mode="acceptEdits"` automatically accepts file edits without prompting. Other modes may require user confirmation.

## Architecture

This is a minimal implementation demonstrating the async query pattern:

1. Initialize `ClaudeAgentOptions` with configuration
2. Call `query()` with a prompt and options
3. Stream responses asynchronously using `async for`

The SDK handles the underlying API communication, streaming, and file operation permissions.