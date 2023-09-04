import os

# Function to display the to-do list
def show_tasks():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
    if tasks:
        print("To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task.strip()}")
    else:
        print("Your to-do list is empty.")

# Function to add a new task
def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

# Function to remove a task
def delete_task(index):
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        with open("todo.txt", "w") as file:
            file.writelines(tasks)
        print("Task removed successfully!")
    else:
        print("Invalid task index.")

# Main function to run the To-Do List application
def main():
    while True:
        print("\nOptions:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter the option number: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            index = int(input("Enter the task number to remove: "))
            delete_task(index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  # Corrected this line to call the main function
