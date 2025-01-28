task = []

while True:
    print("\nMenu:")
    print("1. Add a task") 
    print("2. View a task")
    print("3. Remove a task")
    print("4. Exit from task")
 
    choice = input("Enter your choice")

    if choice=="1":
        addTask = input("Enter the task") 
        task.append(addTask)
        print("task added")
    elif choice=="2":
            print("2\nYour tasks:")
            for i, task in enumerate(task, 1):
                print(f"{i}. {task}")
    elif choice=="3":
       if task:
            print("\nYour tasks:")
            for i, task in enumerate(task, 1):
                print(f"{i}. {task}")
            remove_choice = int(input("Enter the task number to remove: "))
            if 1 <= remove_choice <= len(task):
                removed_task = task.pop(remove_choice - 1)
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Invalid task number.")
    else:
        print("Enter proper choice")
   
https://colorlib.com/etc/regform/colorlib-regform-17/