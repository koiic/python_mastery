import asyncio

# from app import delay


# async  def main():
#     await asyncio.sleep(1)

#
# loop = asyncio.new_event_loop()
#
# try:
#     loop.run_until_complete(main())
#
# finally:
#     loop.close()

def call_later():
    print("I'm being called in the future!")


async def main():
    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = .250
    loop.call_soon(call_later)
    # await delay(1)

# async def main():
#     loop = asyncio.get_event_loop()
#     loop.slow_callback_duration = .250

asyncio.run(main(), debug=True)

