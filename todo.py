tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("\nChoose an option (1-5): ")

    if choice == "1":
        if not tasks:
            print("\nYour to-do list is empty!")
        else:
            print("\n--- YOUR TASKS ---")
            for index, task in enumerate(tasks, start=1):
                status = " Done" if task["completed"] else " Pending"
                print(f"{index}. {task['name']} [{status}]")

    elif choice == "2":
        task_name = input("\nEnter the task name: ")
        if task_name.strip():
            tasks.append({"name": task_name, "completed": False})
            print(f"Task '{task_name}' added successfully!")
        else:
            print("Task name cannot be empty.")

    elif choice == "3":
        if not tasks:
            print("\nNo tasks available to complete.")
        else:
            try:
                task_num = int(input("\nEnter task number to complete: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    print(f"Task '{tasks[task_num - 1]['name']}' marked as complete!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if not tasks:
            print("\nNo tasks available to delete.")
        else:
            try:
                task_num = int(input("\nEnter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Deleted task: '{removed['name']}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("\nGoodbye! Have a productive day!")
        break

    else:
        print("Invalid choice! Please select between 1 and 5.")