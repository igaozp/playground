import asyncio
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions

# Load environment variables from .env file
load_dotenv()


async def main():
    options = ClaudeAgentOptions(
        system_prompt="You are a ai assisant",
        allowed_tools=["Read", "Edit", "Glob"],
        permission_mode="acceptEdits",
        cwd="./",
    )

    async for message in query(prompt="Try to fix README.md file content use current project infomation", options=options):
        print(message)


asyncio.run(main())
