def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("\nNo tasks found.")
            return

        print("\n===== YOUR TASKS =====")

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

    except FileNotFoundError:
        print("\nNo tasks found.")


def add_task():
    task = input("Enter a new task: ")

    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

    print("Task added successfully.")


def delete_task():
    show_tasks()

    try:
        task_number = int(input("Enter task number to delete: "))

        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        tasks.pop(task_number - 1)

        with open("tasks.txt", "w") as file:
            file.writelines(tasks)

        print("Task deleted successfully.")

    except ValueError:
        print("Please enter a valid number.")


while True:

    print("\n===== TO-DO LIST =====")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
