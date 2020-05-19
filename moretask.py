a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)

x = input("enter the desiderd string")
Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(0,26):
    if i == Alphabet:
        print(x.count(Alphabet[i]))
    else:
        pass

str = input("Enter the string: ")
print("String is " , str)
count = {}
for i in str:
    if i in count.keys():
        count[i]+= 1
    else:
        count = 1
print(count)



