def bubblesort(num):
    tem = 0
    for i in range(len(num)):
        temp = True
        for j in range(0,len(num)-1):
            if num[j] > num[j+1]:
                temp = False
                tem = num[j]
                num[j] = num[j+1]
                num[j+1] = tem
        if temp == True:
            break
    return num
print(bubblesort([1,3,5,2,4]))