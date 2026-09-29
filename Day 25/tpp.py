import requests

user_id = int(input("Enter user ID (1-10): "))

url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

try:
    response = requests.get(url)
    response.raise_for_status()

    user = response.json()

    print("\n--- USER DETAILS ---")
    print("Name:", user["name"])
    print("Username:", user["username"])
    print("Email:", user["email"])
    print("City:", user["address"]["city"])
    print("Phone:", user["phone"])
    print("Company:", user["company"]["name"])

except requests.exceptions.RequestException:
    print("Failed to fetch user data!")