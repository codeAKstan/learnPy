def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nList of Tasks:")
        for task in tasks:
            print(f"ID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}\n")
