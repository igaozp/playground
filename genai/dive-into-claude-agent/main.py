import asyncio
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions

# Load environment variables from .env file
load_dotenv()


async def main():
    options = ClaudeAgentOptions(
        system_prompt="You are a ai assisant",
        permission_mode="acceptEdits",
        cwd="/",
    )

    async for message in query(prompt="Which model are you?", options=options):
        print(message)


asyncio.run(main())
