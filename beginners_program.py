# def checkIfANumberIsEvenOrOdd(num): #01
#     if num%2 != 0:
#         return "Odd"
#     else:
#         return "Even"
# print(checkIfANumberIsEvenOrOdd(7))

# def checkIfANumberIsPrime(num): #02
#     count = 0
#     for i in range(2,num):
#         if num%i == 0:
#             return "Not prime"
#             break
#     return "Prime"
# print(checkIfANumberIsPrime(7))

# def findThefactorialOfANumber(num): #03
#     factorial = 1
#     for i in range(1,num+1):
#         factorial = factorial*i
#     return factorial
# print(findThefactorialOfANumber(5))

# def reverseAString(str): #04
#     reverse = ""
#     for i in range(len(str)):
#         reverse = str[i]+reverse
#     return reverse
# print(reverseAString("hello"))

# def checkIfAstringIsAPalindrome(str): #05
#     reverse = ""
#     for i in range(len(str)):
#         reverse = str[i]+reverse
#     if reverse == str:
#         return "Palindrome"
#     else:
#         return "Notpalindrome"
# print(checkIfAstringIsAPalindrome("madam"))

# def findTheSumOfDigitsOfANumber(num): #06
#     sum = 0
#     while(num > 0):
#         sum = num%10+sum
#         num = num//10
#     return sum
# print(findTheSumOfDigitsOfANumber(1234))

def prindTheMultiplictionTableOfANumber(num): #07

    for i in range(1,num+1):
        print(num,"*",i,"=",i*num)
prindTheMultiplictionTableOfANumber(5)

def findTheLargestOf3Numbers(num): #08
    max = -9999999999
    for i in range(len(num)):
        if num[i] > max:
            max = num[i]
    return max
print(findTheLargestOf3Numbers([10,20,15]))

def swapTwoNumbersWithoutUsingATemporaryVarable(a,b): #09
    temp = a
    a = b
    b = temp
    print("a","=",a,",","b","=",b)
swapTwoNumbersWithoutUsingATemporaryVarable(5,7)

def countTheVowelsInAString(str): #10
    count = 0
    for i in str:
        if "a" == i or "e" == i or "i" == i or "o" == i or "u" == i:
            count = count+1
    return count
print(countTheVowelsInAString("hello world"))

def findTheLargestelemendInAnArray(num): #11
    max = -9999999999
    for i in range(len(num)):
        if num[i] > max:
            max = num[i]
    return max
print(findTheLargestelemendInAnArray([5,12,7,21,3]))

def countTheFrequencyOfeachCharacterInAString(str): #12
    b = {}
    for i in str:
        if i in b:
            b[i] = b[i]+1
        else:
            b[i] = 1
    return b
print(countTheFrequencyOfeachCharacterInAString('programming'))

def checkIfTwostringAreAnagrams(a,b): #13
    c = {}
    temp=True
    for i in a:
        if i in c:
            c[i] = c[i]+1
        else:
            c[i] = 1
    for i in b:
        if i in c:
            c[i] = c[i]-1
        else:
            temp = False
            break 
    for i in c:
        if c[i] != 0:
            return False
    if temp == True:
        return "Anagrame"
    else:
        return "Not Anagrame"
print(checkIfTwostringAreAnagrams("listen","ssilent"))

def sortAnArrayInAscendingOrder(num): #14
    for i in range(len(num)):
        temp = 0
        temps = True
        for j in range(len(num)-1):
            if num[j] > num[j+1]:
                temps = False
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
        if temps == True:
             break
    return num
print(sortAnArrayInAscendingOrder([10,40,4,20]))

def countTheNumberOfWordsInASentence(str): #15
    list = (str.split())
    return len(list)
print(countTheNumberOfWordsInASentence("flutter is awesome"))

def checkWhetheraNumberIsAPalindrome(num): #16
    b = 0
    temp = num
    while(num > 0):
        b = b*10+num%10
        num = num//10
    if temp == b:
        return "Palindrome"
    else:
        "Not Plaindrome"
print(checkWhetheraNumberIsAPalindrome(121))

def reverseAnInteger(num): #17
    b = 0
    temp = num
    while(num > 0):
        b = b*10+num%10
        num = num//10
    return b
print(reverseAnInteger(1234))

def printaRightangledtrianglePattern(num): #18
    for i in range(1,num+1):
        for j in range(1,i+1):
            print("*",end="")
        print(" ")
printaRightangledtrianglePattern(3)

def checkIfANumberIsAnArmstrongNumber(num): #19
    sum = 0
    a = 0
    b = 0
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
print(checkIfANumberIsAnArmstrongNumber(153))

def checkThefibnosisNumber(num): #20
    start = 0
    end = 1
    print(start,end= " ")
    print(end, end= " ")
    for i in range(num-1):
        temp = start+end
        print(start+end,end= " ")
        start = end
        end = temp
checkThefibnosisNumber(10)





 





    












