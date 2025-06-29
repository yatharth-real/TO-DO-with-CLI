import os

TODO_FILE = 'todo.txt'

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {task}")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        print("5. Help")
        print("By Yatharth-Real and VSCode")

        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            task = input("Enter new task: ").strip()
            if task:
                add_task(task)
            else:
                print("Task cannot be empty.")
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            try:
                index = int(input("Enter task number to delete: ").strip())
                delete_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye!")
            
        elif choice == '5':
            print("Type :1 or 2 or 3 or 4 or 5 ;for your prefered task")

        else:            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

