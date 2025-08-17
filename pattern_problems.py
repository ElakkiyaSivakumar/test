def printARightAngledTrianglePattern(num): #01
    for i in range(1,num+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print("")
    print("   ")
printARightAngledTrianglePattern(3)

def printAnInvertedRightAngledTrianglePattern(num): #02
    for i in range(1,num+1):
        for j in range(1,num+2-i):
            print("*",end=" ")
        print("")
    print("   ")
printAnInvertedRightAngledTrianglePattern(3)

def printASquarePatternOfsstars(num): #03
    for i in range(1,num+1):
        for j in range(1,num+1):
            print("*",end=" ")
        print("")
    print("   ")
printASquarePatternOfsstars(3)

def printAPyramidPattern(num):
    for i in range(1,num+1):
        for j in range(1,num+1-i):
            print(" ",end=" ")
        for z in range(1,i+i):
            print("*",end=" ")
        print("")
printAPyramidPattern(3)
         

    