import asyncio


async def download_file():
    print("Downloading file...")
    await asyncio.sleep(2)
    print("Download complete")


async def process_file():
    print("Processing file...")
    await asyncio.sleep(2)
    print("Processing complete")


async def main():
    await asyncio.gather(
        download_file(),
        process_file()
    )


asyncio.run(main())