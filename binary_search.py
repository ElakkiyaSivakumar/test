def binarysearch(num,target):
    num.sort()
    start = 0
    end = len(num)-1
    while(start <= end):
        mid = (start +end)//2
        if target == num[mid]:
            return True
        elif target > num[mid]:
            start = mid+1
        else:
            end = mid-1
    return False
print(binarysearch([10,30,20,40,50,60],20))