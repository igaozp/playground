import asyncio

from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage, ToolUseBlock
from dotenv import load_dotenv

from todo_tracker import TodoTracker

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


# When Todos Are Used
# The SDK automatically creates todos for:
# Complex multi-step tasks requiring 3 or more distinct actions
# User-provided task lists when multiple items are mentioned
# Non-trivial operations that benefit from progress tracking
# Explicit requests when users ask for todo organization
async def plan():
    options = ClaudeAgentOptions(
        system_prompt="You are a ai assisant",
        allowed_tools=["Read", "Write", "Edit", "Glob", "Grep", "TodoWrite", "ExitPlanMode"],
        permission_mode="acceptEdits",
        max_turns=100,
        cwd="./",
    )
    async for message in query(prompt="Please plan a learning plan for Python with todos. Write in py-learn.md file",
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
                print(f"Tool🛠️: {block.name}")
            if isinstance(block, ToolUseBlock) and block.name == "TodoWrite":
                todos = block.input["todos"]
                print("Todo Status Update:")
                for i, todo in enumerate(todos):
                    status = "✅" if todo["status"] == "completed" else \
                        "🔧" if todo["status"] == "in_progress" else "❌"
                    print(f"{i + 1}. {status} {todo['content']}")
    elif isinstance(message, ResultMessage):
        # Final result
        print(f"Done: {message.subtype}")


todo_tracker = TodoTracker()
asyncio.run(todo_tracker.track_query("Please put an elephant into a refrigerator with todos"))
