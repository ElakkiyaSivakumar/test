def largestElementInAnArray(num):
    max = -9999999999
    for i in range(len(num)):
        if num[i] > max:
            max = num[i]
    return max
print(largestElementInAnArray([10,40,50,70,20]))

def checkIfTheArrayIssorted(num):
    for i in range(len(num)-1):
        if num[i] < num[i+1]:
            continue
        else:
            return False
    return True
print(checkIfTheArrayIssorted([10,40,50,70]))

def linearSearch(num,tar):
    for i in range(len(num)):
        if num[i] == tar:
            return True
    return False
print(linearSearch([10,40,50,70,20],70))

def secontLargestElementInAnArray(num):
    first = -9999999999
    secont = -9999999999
    for i in range(len(num)):
        if num[i] > first:
            secont = first
            first = num[i]
        elif num[i] > secont and num[i] < first:
            secont = num[i]
    return secont
print(secontLargestElementInAnArray([10,40,50,70,20]))

def rotatedArrayByNplace(n,arr):
    num = n%len(arr)
    
    for i in range(num+1):
        temp = arr[0]
        for j in range(1,len(arr)):
            arr[j-1] = arr[j]
        arr[len(arr)-1] = temp
    
            
    return arr
print(rotatedArrayByNplace(7,[1,2,3,4,5]))

def rotatedArray(n,arr):
    for i in range(n):
        temp = arr[len(arr)-1]
        for j in range(len(arr)-2,-1,-1):
            arr[j+1] = arr[j]
        arr[0] = temp
    return arr    
        
print(rotatedArray(3,[1,2,3,4,5,6,7]))

def leftRotateInArray(start,end,arr):
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start+1
        end = end-1

def rotate(arr,t):
    d = t%len(arr)
    leftRotateInArray(0,len(arr)-1,arr)
    leftRotateInArray(len(arr)-d,len(arr)-1,arr)
    leftRotateInArray(0,(len(arr))-(d+1),arr)
    return arr
print(rotate([1,2,3,4,5],7))

def rightRotate(start,end,arr):
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start+1
        end = end-1
def rotate(arr,t):
    d = t%len(arr)
    print(d)
    rightRotate(0,len(arr)-1,arr)
    print(arr)
    rightRotate(0,(len(arr)-1)-(d+1),arr)
    print(arr)
    rightRotate(len(arr)-(d+1),len(arr)-1,arr)
    print(arr)
    return arr
print(rotate([1,2,3,4,5],7))
        