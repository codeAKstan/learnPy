def search_task(tasks):
    query = input("Enter search keyword: ").lower()
    results = [task for task in tasks if query in task['title'].lower() or query in task['description'].lower()]
    if results:
        for task in results:
            print(f"ID: {task['id']} | Title: {task['title']} | Due Date: {task['due_date']}")
    else:
        print("No matching tasks found.")
