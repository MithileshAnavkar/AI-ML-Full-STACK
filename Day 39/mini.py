import asyncio
import random


async def fetch_data(user_id):
    delay = random.randint(1, 3)

    print(f"Fetching user {user_id}...")

    await asyncio.sleep(delay)

    print(f"User {user_id} data received")


async def main():

    await asyncio.gather(
        fetch_data(101),
        fetch_data(102),
        fetch_data(103),
        fetch_data(104),
        fetch_data(105)
    )


asyncio.run(main())