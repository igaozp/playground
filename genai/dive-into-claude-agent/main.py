import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions


async def main():
    options = ClaudeAgentOptions(
        system_prompt="You are a ai assisant",
        permission_mode="acceptEdits",
        cwd="/",
    )

    async for message in query(prompt="Which model are you?", options=options):
        print(message)


asyncio.run(main())
