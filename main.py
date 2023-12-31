from datetime import datetime


class Task:
    def __init__(self, description) -> None:
        self.id = len(all_tasks) + 1
        self.description = description
        self.status = "pending"
        self.start_time = datetime.now()


def view_tasks():
    if all_tasks != []:
        print("\nAll tasks.")
        for task in all_tasks:
            print(f"Id: {task.id}\t Description: {
                task.description}\t Status: {task.status}")
        print("")   # for a new line after all the records are printed
    else:
        print("No tasks found.\n")


def add_task():
    # Creating and adding new task object to the all_tasks list
    description = input("Description: ")
    try:
        task = Task(description)
    except:
        print("Task creation failed.")
    else:
        all_tasks.append(task)
        print("\nTask added succesfully.")
        print(f"Id: {task.id}\t Description: {
            task.description}\t Status: {task.status}\n")


def mark_completed():
    task_id = int(input("Id: "))
    for task in all_tasks:
        if task.id == task_id:
            task.status = "completed"
            print("Status changed!")
            print(f"Completed in {
                (datetime.now() - task.start_time)} time\n")
            return

    else:
        print(f"We couldn't find task with '{task_id}' id\n")


def delete_task():
    task_id = int(input("Id: "))
    for task in all_tasks:
        if task.id == task_id:
            all_tasks.remove(task)
            print("Task deleted successfully.\n")
            return

    else:
        print(f"We couldn't find task with '{task_id}' id\n")


def edit_task():
    task_id = int(input("Id: "))
    for task in all_tasks:
        if task.id == task_id:
            task_desc = input("Description: ")
            task.description = task_desc
            print("Description changed successfully.\n")
            return

    else:
        print(f"We couldn't find task with '{task_id}' id\n")


def show_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Edit Task Description")
    print("6. Quit")


all_tasks = []
choice = 0
while choice != 6:
    show_menu()
    choice = int(input("\nChoice: "))

    if choice == 1:
        add_task()

    elif choice == 2:
        view_tasks()

    elif choice == 3:
        mark_completed()

    elif choice == 4:
        delete_task()

    elif choice == 5:
        edit_task()

    else:
        print("Bad choice!\n")


print("Have a good night ⏾\n")
