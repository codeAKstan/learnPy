import json

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved to file.")

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            content = file.read().strip()
            return json.loads(content) if content else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: The tasks.json file contains invalid JSON.")
        return []
