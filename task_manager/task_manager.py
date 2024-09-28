from add_task import add_task, tasks
from save_task import save_tasks, load_tasks
from view_tasks import view_tasks
from update_task import update_task
from delete_task import delete_task

# Load existing tasks
tasks.extend(load_tasks())

def main_menu():
    print("\nTask Management System")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Save Tasks to File")
    print("6. Exit")

if __name__ == "__main__":
    while True:
        main_menu()
        
        # Input validation
        while True:
            try:
                choice = int(input("Enter your choice (1-6): "))
                if 1 <= choice <= 6:
                    break
                else:
                    print("Your choice should be between 1 to 6.")
            except ValueError:
                print("Please enter a valid number.")

        if choice == 6:
            print("Exiting Task Manager...")
            break
        elif choice == 1:
            add_task()
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            update_task(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            save_tasks(tasks)
