def linearsearch(num,target):
    for i in range(len(num)):
        if num[i] == target:
            return True
    return False
print(linearsearch([10,20,30,50,40],70))
    