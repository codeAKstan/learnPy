def delete_task(tasks):
    task_id = int(input("Enter the task ID to delete: "))
    
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task deleted successfully.")
            return

    print("Task ID not found.")
