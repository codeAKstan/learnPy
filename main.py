import requests

url = 'https://jsonplaceholder.typicode.com/posts'


new_post = {
    'title': "project",
    'body': "this is my project body",
    'userId': 2
}
response = requests.post(url, json=new_post)

if response.status_code == 201:
    print("this is a new post")
    print(response.json())

else:
    print("failed")