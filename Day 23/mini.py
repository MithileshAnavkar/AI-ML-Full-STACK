import requests

url = "https://jsonplaceholder.typicode.com/users/5"

try:
    response = requests.get(url)
    response.raise_for_status()

    user = response.json()

    print("===== USER INFORMATION =====")
    print("Name:", user["name"])
    print("Username:", user["username"])
    print("Email:", user["email"])
    print("Phone:", user["phone"])
    print("Website:", user["website"])
    print("City:", user["address"]["city"])
    print("Company:", user["company"]["name"])

except requests.exceptions.RequestException as e:
    print("API Error:", e)