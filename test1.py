def trianglePattern(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print(" ")
trianglePattern(3)

def fibonacciNumber(num):
    start = 0
    end = 1
    print(start,end=" ")
    print(end,end=" ")
    for i in range(num-1):
        temp = start+end
        print(temp,end=" ")
        start = end
        end = temp
fibonacciNumber(10)

def countTheVowels(str):
    count = 0
    for i in str:
        if "a" == i or "e" == i or "i" == i or "o" == i or "u" == i:
            count = count+1
    return count
print()
print(countTheVowels("hello world"))

def armstrongNumber(num):
    a = 0
    b = 0
    sum = 0
    temp = num
    while(num > 0):
        a = num%10
        b = a**3
        sum = sum+b
        num = num//10
    if temp == sum:
        return "Armstrong"
    else:
        return "Not Armstrong"
print(armstrongNumber(153)) 

def angram(a,b):
    c = {}
    if len(a) != len(b):
        return "Not Anagram"
    for i in a:
        if i in c:
            c[i] = c[i]+1
        else:
            c[i] = 1
    for i in b:
        if i in c:
            c[i] = c[i]-1
        else:
            return "Not Anagram"
    for i in c:
        if c[i] != 0:
            return "Not anagram"
    return "Anagram"
print(angram("siilent","liisten"))

def dic(str):
    a = {}
    for i in str:
        if i in a:
            a[i] = a[i]+1
        else:
            a[i] = 1
    return a
print(dic("programming"))
