tasks = []

def show_tasks():
    if tasks:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
    else:
        print("\nNo tasks yet!")

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    
    choice = input("Choose an option (1/2/3): ")
    
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again!")
