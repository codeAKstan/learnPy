tasks = []

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter task due date (YYYY-MM-DD): ")
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "due_date": due_date
    }
    tasks.append(task)
    print("Task added successfully.")
