from concurrent.futures import ThreadPoolExecutor
import time


def fetch_user(user_id):
    print("Fetching user", user_id)

    time.sleep(1)

    return f"User {user_id} received"


users = [101, 102, 103, 104, 105]


with ThreadPoolExecutor(max_workers=5) as executor:

    results = executor.map(fetch_user, users)

    for result in results:
        print(result)