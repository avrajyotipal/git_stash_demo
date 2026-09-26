tasks = []


def add_task(task, priority="Medium"):
    tasks.append({
        "task": task,
        "priority": priority
    })

    print(f"Task added: {task} | Priority: {priority}")


def show_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nTasks:")

    for index, task in enumerate(tasks, start=1):
        print(
            f"{index}. {task['task']} "
            f"[Priority: {task['priority']}]"
        )



def main():
    print("Task Manager implemented")

    while True:
        print("\n1. Add Task")
        print("2. Show Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()