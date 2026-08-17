tasks = []
def show_tasks():
    """to show all function"""
    if not tasks:
        print("\nTo-Do list is empty!")
    else:
        print("\n--- To-Do list ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
def add_task():
    """function to add new task"""
    task = input("\nwrite new task: ").strip()
    if task:
        tasks.append(task)
        print(f"'{task}' task added to list!")
    else:
        print("empty task not added.")


def delete_task():
    """function to delete task"""
    show_tasks()
    if tasks:
        try:
            task_num = int(
                input("\nwrite number to delete task: ")
            )
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"'{removed_task}' removed from list!")
            else:
                print("wrong task!")
        except ValueError:
            print("enter correct number!")


# Main Loop
while True:
    print("\n=========================")
    print("      TO-DO LIST")
    print("=========================")
    print("1.  View Task(View Tasks)")
    print("2. Add new task ")
    print("3. Task Deleted")
    print("4. Exit (close program)")

    choice = input("choose your option (1-4): ").strip()

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("\nprogram closing. good bye!")
        break
    else:
        print("\nwrong option! only enter 1, 2, 3, or 4 .")