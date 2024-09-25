import requests

url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'My Post',
    'body': 'This is the body of the post',
    'userId': 1
}

response = requests.post(url, json=data)

# Check if the POST request was successful
if response.status_code == 201:
    print("Data successfully sent!")
    print(response.json())  
else:
    print("Failed to send data")
