import requests

url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    for user in users:
        print(f'name: {user["name"]}')
        print(f"email: {user['email']}")

else:
    print("error")
