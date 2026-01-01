# Dive into Claude Agent

A Python project for exploring the Claude AI Agent SDK. This is a learning/experimental project that demonstrates basic usage of the `claude-agent-sdk` package to interact with Claude models programmatically.

## Project Overview

This project provides a minimal implementation of the Claude Agent SDK, showcasing how to:
- Initialize and configure a Claude agent
- Set up custom system prompts and permission modes
- Stream responses asynchronously
- Interact with the file system through allowed tools

## Features

- **Async Query Pattern**: Uses Python's async/await for streaming responses
- **Environment Configuration**: Loads configuration from `.env` file using `python-dotenv`
- **Customizable Options**: Configurable system prompts, permission modes, and working directories
- **File Operations**: Demonstrates file reading, editing, and glob pattern matching capabilities

## Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd dive-into-claude-agent
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

3. Activate the virtual environment:
   ```bash
   # On Unix/macOS
   source .venv/bin/activate

   # On Windows
   .venv\Scripts\activate
   ```

4. Copy the example environment file and configure your API credentials:
   ```bash
   cp example.env .env
   ```

   Edit `.env` with your actual API credentials:
   ```bash
   export ANTHROPIC_BASE_URL=your_custom_anthropic_base_url
   export ANTHROPIC_AUTH_TOKEN=your_custom_anthropic_auth_token
   export ANTHROPIC_MODEL=your_custom_anthropic_model
   export ANTHROPIC_SMALL_FAST_MODEL=your_custom_anthropic_model
   export API_TIMEOUT_MS=600000
   export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
   ```

## Usage

Run the main script:

```bash
uv run main
```

Or with Python directly (after activating the virtual environment):

```bash
python main.py
```

## Project Structure

```
dive-into-claude-agent/
├── main.py                 # Main entry point demonstrating Claude Agent SDK usage
├── pyproject.toml          # Project metadata and dependencies
├── README.md               # This file
├── CLAUDE.md               # Claude Code guidance for this repository
├── example.env             # Example environment configuration
├── .env                    # Environment configuration (not committed to git)
├── uv.lock                 # Locked dependency versions
├── .gitignore              # Git ignore rules
├── .python-version         # Python version specification
└── .venv/                  # Python virtual environment
```

## Configuration

### ClaudeAgentOptions

The main script configures the agent with the following options:

```python
options = ClaudeAgentOptions(
    system_prompt="You are a ai assistant",
    allowed_tools=["Read", "Edit", "Glob"],
    permission_mode="acceptEdits",
    cwd="./",
)
```

- **system_prompt**: Custom system prompt for the agent
- **allowed_tools**: List of tools the agent can use (file operations)
- **permission_mode**: Controls file operation permissions (`"acceptEdits"` auto-accepts edits)
- **cwd**: Working directory for file operations

### Environment Variables

The project uses the following environment variables (configured in `.env`):

| Variable | Description | Example |
|----------|-------------|---------|
| `ANTHROPIC_BASE_URL` | API base URL | `https://api.deepseek.com` |
| `ANTHROPIC_AUTH_TOKEN` | API authentication token | `your-api-token` |
| `ANTHROPIC_MODEL` | Primary model identifier | `claude-3-5-sonnet-20241022` |
| `ANTHROPIC_SMALL_FAST_MODEL` | Fallback model for simpler tasks | `claude-3-haiku-20240307` |
| `API_TIMEOUT_MS` | API request timeout in milliseconds | `600000` |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | Disable telemetry | `1` |

## Dependencies

- **claude-agent-sdk** (>=0.1.17): Official SDK for building Claude agents
- **python-dotenv**: Loads environment variables from `.env` file

## Development

### Adding New Features

1. Extend the `allowed_tools` list in `ClaudeAgentOptions` to grant additional capabilities
2. Modify the `system_prompt` to change the agent's behavior
3. Update the query prompt in `main.py` to test different interactions

### Testing Different Permission Modes

The SDK supports different permission modes:
- `"acceptEdits"`: Automatically accepts file edits
- `"prompt"`: Prompts for user confirmation before file operations
- `"rejectEdits"`: Rejects all file edits

### Async Pattern

The project uses Python's async/await pattern for streaming responses:

```python
async for message in query(prompt="Your prompt here", options=options):
    print(message)
```

## Security Notes

- **Never commit `.env` files** containing actual API credentials to git
- Use `.gitignore` to exclude sensitive files
- The `example.env` file provides a template without real credentials

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Ensure the virtual environment is activated and dependencies are installed with `uv sync`
2. **API Authentication Errors**: Verify your `.env` file contains correct API credentials
3. **Permission Errors**: Check the `permission_mode` setting in `ClaudeAgentOptions`

### Debugging

- Check that environment variables are loaded correctly
- Verify the API endpoint is accessible
- Ensure you have sufficient API credits/quota

## License

This project is for educational purposes. See the repository for license information.

## Contributing

This is a learning project. Feel free to fork and experiment with different configurations and use cases.

## Acknowledgments

- [Claude AI Agent SDK](https://github.com/anthropics/claude-agent-sdk) for providing the SDK
- [uv](https://github.com/astral-sh/uv) for fast Python package management