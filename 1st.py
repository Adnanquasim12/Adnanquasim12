# Simple To-Do List Application

# Initialize an empty list to store tasks
tasks = []

def display_tasks():
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} - {'Completed' if task['completed'] else 'Not Completed'}")

def add_task():
    task_name = input("Enter a new task: ")
    tasks.append({'name': task_name, 'completed': False})
    print(f"Task '{task_name}' added successfully!")

def mark_task_completed():
    display_tasks()
    task_number = int(input("Enter the task number to mark as completed: "))
    try:
        tasks[task_number - 1]['completed'] = True
        print(f"Task {task_number} marked as completed!")
    except IndexError:
        print("Invalid task number. Please try again.")

def remove_task():
    display_tasks()
    task_number = int(input("Enter the task number to remove: "))
    try:
        del tasks[task_number - 1]
        print(f"Task {task_number} removed successfully!")
    except IndexError:
        print("Invalid task number. Please try again.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task_completed()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
