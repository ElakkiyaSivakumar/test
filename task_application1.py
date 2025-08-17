temp = True
tasks = [ ]
while(temp):
    print("------------------------------------------")
    print("Enter to 1 add task")
    print("Enter to 2 delete task")
    print("Enter to 3 see task")
    print("Enter to 4 excite task")
    print("------------------------------------------")

    choice = int(input("Enter a your choice : "))
    
    if choice == 1:
        a = input("Enter a your task : ")
        tasks.append(a)
    elif choice == 2:
        b = input("Enter a your task : ")
        tasks.remove(b)
    elif choice == 3:
        print("------------------------------------------")
        print(tasks)
    elif choice == 4:
        temp = False
    else:
        print("pls enter num : 1,2,3,4 ")



