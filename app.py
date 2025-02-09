# app.py

# Simple To-Do List Application

tasks = []

def display_tasks():
    if not tasks:
        print("\nNo tasks to display!")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(task):
    tasks.append(task)
    print(f'Added: "{task}"')

def remove_task(task_index):
    try:
        removed_task = tasks.pop(task_index - 1)
        print(f'Removed: "{removed_task}"')
    except IndexError:
        print("Invalid task number!")

def main():
    while True:
        print("\nSimple To-Do List")
        print("1. Display tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            display_tasks()
        elif choice == 2:
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == 3:
            try:
                task_index = int(input("Enter the task number to remove: "))
                remove_task(task_index)
            except ValueError:
                print("Please enter a valid task number.")
        elif choice == 4:
            print("Exiting the To-Do list. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
