from concurrent.futures import ThreadPoolExecutor
import time
import random


def fetch_data(data_type):

    delay = random.randint(1, 3)

    print(f"Fetching {data_type}...")

    time.sleep(delay)

    return f"{data_type} received"


data = [
    "Users",
    "Products",
    "Orders",
    "Payments",
    "Notifications"
]


with ThreadPoolExecutor(max_workers=5) as executor:

    futures = [
        executor.submit(fetch_data, item)
        for item in data
    ]

    for future in futures:
        print(future.result())


print("Dashboard ready!")