import asyncio

from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


async def summary():
    options = ClaudeAgentOptions(
        system_prompt="You are a ai assisant",
        allowed_tools=["Read", "Edit", "Glob"],
        permission_mode="acceptEdits",
        max_turns=100,
        cwd="./",
    )

    async for message in query(prompt="Summary this README.md file content",
                               options=options):
        log(message)

# The API must support web search features, similar to the official Claude API
async def web_search():
    options = ClaudeAgentOptions(
        system_prompt="You are a ai assisant",
        allowed_tools=["WebSearch"],
        permission_mode="acceptEdits",
        max_turns=100,
        cwd="./",
    )

    async for message in query(prompt="Get today weather in Beijing",
                               options=options):
        log(message)


def log(message):
    # Print human-readable output
    if isinstance(message, AssistantMessage):
        for block in message.content:
            if hasattr(block, "text"):
                # Claude's reasoning
                print(block.text)
            elif hasattr(block, "name"):
                # Tool being called
                print(f"Tool: {block.name}")
    elif isinstance(message, ResultMessage):
        # Final result
        print(f"Done: {message.subtype}")


asyncio.run(web_search())
