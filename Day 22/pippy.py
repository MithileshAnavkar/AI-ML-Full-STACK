import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("Name:", data["name"])
print("Username:", data["username"])
print("Email:", data["email"])