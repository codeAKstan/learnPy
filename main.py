import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
json_data = json.dumps(data)
print(json_data)
