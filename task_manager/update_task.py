def update_task(tasks):
    task_id = int(input("Enter the task ID to update: "))
    
    for task in tasks:
        if task["id"] == task_id:
            print(f"Current Title: {task['title']}")
            task["title"] = input("Enter new title (leave blank to keep current): ") or task["title"]
            
            print(f"Current Description: {task['description']}")
            task["description"] = input("Enter new description (leave blank to keep current): ") or task["description"]
            
            print(f"Current Due Date: {task['due_date']}")
            task["due_date"] = input("Enter new due date (YYYY-MM-DD, leave blank to keep current): ") or task["due_date"]
            
            print("Task updated successfully.")
            return

    print("Task ID not found.")
