# TO DO LIST Python
print("Hello! Welcome to To-Do List App")
# it will help us arranging our works accordingly to our routine
tasks = []

while True:
    print("\nMenu Options:")
    print("(1) Add a Task")
    print("(2) Delete a Task")
    print("(3) View all Tasks")
    print("(4) Update a Task")
    print("(5) Exit")

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        task_name = input("Enter the task you want to perform: ").strip()# strip used for avoiding unnecessary spaces
        tasks.append(task_name)
        print(f"Task '{task_name}' added successfully.")

    elif user_choice == 2:
        if tasks == []:
            print("No tasks found.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_number = int(input("Enter the task number you want to delete: "))
            if 1 <= task_number <= len(tasks):
                delete_task = tasks.pop(task_number - 1)
                print(f"Task '{delete_task}' removed successfully.")
            else:
                print("Invalid task number.")

    elif user_choice == 3:
        if tasks == []:
            print("No tasks found.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif user_choice == 4:
        if tasks == []:
            print("No tasks to update.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_number = int(input("Enter the task number you want to update: "))
            if 1 <= task_number <= len(tasks):
                new_task = input("Enter the new task: ").strip()
                tasks[task_number - 1] = new_task
                print("Task updated successfully.")
            else:
                print("Invalid task number.")

    elif user_choice == 5:
        print("Goodbye! Thank you for using To-Do List App.")
        break

    else:
        print("Invalid choice! Please choose between 1, 2, 3, 4, or 5.")
