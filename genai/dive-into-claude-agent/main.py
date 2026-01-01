import asyncio
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage

# Load environment variables from .env file
load_dotenv()


async def main():
    options = ClaudeAgentOptions(
        system_prompt="You are a ai assisant",
        allowed_tools=["Read", "Edit", "Glob"],
        permission_mode="acceptEdits",
        cwd="./",
    )

    async for message in query(prompt="Summary this README.md file content",
                               options=options):
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


asyncio.run(main())
