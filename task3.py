#num1 = int (input ("insert your first number except from 1-4 " ))
#num2 = int (input("insert the second number except from 1 -4 ")) 
num1 = 32
num2 = 55
ch = int (input("input from 1 - 4 to chose your operation"))
result = 0 
if ch == 1:
    result = num1 + num2
elif ch == 2:
    result = num1 - num2
elif ch == 3:
    result = num1 * num2
elif ch == 4:
    result = num1 / num2
else:
    print("out of operators") 
print(num1, ch , num2, ":", result) 
if result <0:
    print("negative") 

#first = 8
#second = 7 
#ch = int (input("input 5 to get the average number")) 
#result = 0 
#if ch == 5: 
    #result = (first + second) / 2
#else:
    #print("out of operators")
#print(first, ch, second, ":" , result)