
even=[]
odd=[]
for j in even and odd:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)

given = (1,2,3,4,5,6,7,8,9,10)
print(type(given))
x = list(given)
print(type(x))
even = []
for i in x:
    if i%2 == 0:
        even.append(i)
    else:
        pass
print(even)
result = tuple(even)
print(type(result))
print(result)

str = input("Enter the number")
print("string is",str)
count = {}
for x in str:
    if x in count.keys():
        count[x]+=1
    else:
        count[x] = 1
print(count)
print("Hello world")
