from langchain_anthropic import ChatAnthropic
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")

async def main():
    agent = Agent(
        task="Go to https://data.gov/, find an interesting dataset, and download it.",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())

