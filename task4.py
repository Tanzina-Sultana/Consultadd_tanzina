#1. Write a program to reverse a string. Sample data: “1234abcd” Expected Output: “dcba4321” 
def reverse(str):
    while True:
        print("Enter x to exit")
        string = input("Enter your string")
        if string == 'x':
            break
        else:
            reverse = string[::-1]
            print("reversing ", reverse)
print(reverse(str))

#2. Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters. Expected Output:
#No. of Upper case characters : 3
#No. of Lower case Characters : 12
def upper_lower(str):
    upper = 0
    lower = 0
    for i in str:
        if i.isupper():
            upper +=1
        elif i.islower():
            lower +=1
        else:
            pass
        
    print("upper case letter :", upper)
    print("lower case letter :", lower)
    return(upper,lower)
print(upper_lower('ARGTUhrnatl'))

#3.  Create a function that takes a list and returns a new list with unique elements of the first list. 
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 

# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
def rain():
 items=[n for n in input().split('-')] 
 items.sort()
 return('-'.join(items))
print(rain()) 
#5.Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Sample input:
#Hello world
#Practice makes perfect 

def upper():
 x = input("enter your string")
 y = input("enter your second string")
 res = x.upper()
 ress2 = y.upper()
 return(res,ress2)
print(upper())

#6.Define a function that can receive two integral numbers in string form and compute their sum and print it in console. 
def sum(x,y): 
    s = int(x) + int(y)
    return(s)
input1 = "5"
input2 = "7"

result = sum(input1,input2)

print("Final Result",result) 

#7.Define a function that can accept two strings as input and print the string with maximum length in console. 
# If two strings have the same length, then the function should print all strings line by line. 
def stringprint(str1, str2):
    if (len(str1) < len(str2)):
        print("Larger string: ", str2)         
    elif(len(str1) == len(str2)):
        print(str1,str2)
    else:
        print("Larger string is : ", str1) 

stringprint("Rio","dejario")

#8.Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20. 
def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l)
		
printValues()


#9.         Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
#Example: If the limit is 3 , it should print:
#0 EVEN
#1 ODD
#2 EVEN
#3 ODD
def showNumbers(limit):
    for i in range(0,limit +1): 
        if i % 2 == 0:
            print(str(i) + ":" +'EVEN')
        else:
            print(str(i) + ":"+ 'ODD')




limit = int(input("Give me a number. "))

showNumbers(limit)











