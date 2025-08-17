temp = True
id = 0
tasks = {} 
while(temp):
    print("------------------------------------------")
    print("Enter to 1 add task")
    print("Enter to 2 delete task")
    print("Enter to 3 see task")
    print("Enter to 4 update task")
    print("Enter to 5 excite task")
    print("------------------------------------------")

    choice = int(input("Enter a your choice : "))
    
    if choice == 1:
        a = input("Enter a your task : ")
        tasks[id] = a
        id = id+1
    elif choice == 2:
        b = int(input("Enter a your id : "))
        if b in tasks:
            tasks.pop(b)
        else:
            print("-------------------------------")
            print("Enter your valid id ")
    elif choice == 3:
        print("------------------------------------------")
        print(tasks)
    elif choice == 4:
        c = int(input("Enter a your id : "))
        if c in tasks:

            d = input("Enter a your choice : ")
            tasks[c] = d
        else:
            print("------------------------------------------")
            print("Enter a valid id")
    elif choice == 5:
        temp = False
    else:
        print("pls enter num : 1,2,3,4 ")



