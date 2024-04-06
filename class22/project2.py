# Function to display the menu
def display_menu():
    print("\nSimple To-Do List Application")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Exit")

# Function to add a task to the list
def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to delete a task from the list
def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        index = int(input("Enter the index of the task to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task deleted successfully!")
        else:
            print("Invalid index.")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            delete_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
