

import asyncio
import requests
import httpx

from utils import async_timed


@async_timed
async def delay(delay_seconds: int) -> int:
    print(f'sleeping for {delay_seconds} second(s)')
    await asyncio.sleep(delay_seconds)
    print(f'finished sleeping for {delay_seconds} second(s)')
    return delay_seconds



@async_timed
async def get_example_status() -> int:
    async with httpx.AsyncClient() as client:
        r = await client.get('http://www.example.com')
        return  r
    # return requests.get('http://www.example.com').status_code


@async_timed
async def main():
    task_1 = asyncio.create_task(get_example_status())
    task_2 = asyncio.create_task(get_example_status())
    task_3 = asyncio.create_task(get_example_status())

    await task_1
    await task_2
    await task_3


asyncio.run(main())
