tasks = []

def add_task():
    input_task = input("Enter the task to add: ")
    tasks.append(input_task)
    print(f"task '{input_task}' added.")

def view_tasks():
    if not tasks:
        print("no tasks available.")
    else:
      print("\n--- Current tasks: ---")
      for index, task in enumerate(tasks, start=1):
          print(f"{index}. {task}")
          print("-----------------------")

def complete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to complete: "))
        if 1 <= task_number <= len(tasks):
            done_task = tasks.pop(task_number -1)
            print(f"Task '{done_task}' completed and removed from the list.")
            view_tasks()
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


while True:
    print("\nTo-Do List:")
    print("options:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")
    if choice == '1':
        print("\nAdd Task:")
        add_task()
    elif choice == '2':
        print("\nView Tasks:")
        view_tasks()
    elif choice == '3':
        print("\nComplete Task:")
        complete_task()
    elif choice == '4':
        print("Exiting the To-Do List application.")
        break
    else:
        print("Invalid choice. Please try again.")
        continue
