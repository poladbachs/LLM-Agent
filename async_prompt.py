import asyncio
from magentic import prompt
from time import time
from typing import AsyncIterable
from dotenv import load_dotenv
load_dotenv()

@prompt("List three high-growth stocks.")
async def iter_growth_stocks() -> AsyncIterable[str]: ...

@prompt("Briefly describe {stock_symbol} in 2-3 sentences.")
async def tell_me_more_about(stock_symbol: str) -> str: ...

async def main():
    print("\n⚡ Starting async LLM streaming demo...\n")
    start_time = time()

    tasks = []
    async for stock in await iter_growth_stocks():
        print(f"Found: {stock}")
        task = asyncio.create_task(tell_me_more_about(stock))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    print(f"\nDone in {time() - start_time:.2f}s\n")

    for desc in results:
        print(f"— {desc}\n")

if __name__ == "__main__":
    asyncio.run(main())
