temp = True

while(temp):
    print("------------------------------------------")
    print("Enter to 1 add task")
    print("Enter to 2 subtraction task")
    print("Enter to 3 multiplication task")
    print("Enter to 4 division task")
    print("------------------------------------------")

    choice = int(input("Enter a your choice : "))
    
    if choice == 1:
        a = int(input("Enter a your task : "))
        b = int(input("Enter a your task : "))
        print("------------------------------------------")
        print("Add = " + str(a+b)) 
    elif choice == 2:
        c = int(input("Enter a your task : "))
        d = int(input("Enter a your task : "))
        print("------------------------------------------")
        print("Subtraction = " + str(c-d))
    elif choice == 3:
        e = int(input("Enter a your task : "))
        f = int(input("Enter a your task : "))
        print("------------------------------------------")
        print("Multiplication = "+ str(e*f) )
    elif choice == 4:
        g = int(input("Enter a your task : "))
        h = int(input("Enter a your task : "))
        print("------------------------------------------")
        print("divisoin = "+ str(g%h))

    else:
        print("pls enter num : 1,2,3,4 ")



