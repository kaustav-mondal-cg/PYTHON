for i in range(1,6):
    print("Hello")

for i in range(0,10):
    print(i, end=" ")

for i in range(1,11):
    print(i)

for i in range(10,0,-1):
    print(i)

for i in range(5,51,5):
      print(i)

for i in range(2,21,2):
    print(i)

for i in range(1,20,2):
    print(i)

for i in range(3,19,3):
    print(i)

for i in range(20,1,-2):
    print(i)

n=int(input("enter a positive number..."))
for n in range(1,n):
        print(n)

n=int(input("enter a even number..."))
if n%2==0:
    for n in range(2,n,2):
        print(n)
else:
    print("please enter a even number!") 

n=int(input("enter a odd number..."))
if n%2!=0:
    for n in range(1,n,2):
        print(n)
else:
    print("please enter a odd number!") 

n=int(input("enter a number..."))
for n in range(1,n):
    if n%3==0:
        print(n)

n=int(input("enter a number..."))
for n in range(1,n):
    if n%3==0 and n%2==0:
        print(n)

n=int(input("enter a number..."))
count=0
for n in range(2,n,2):
    count=count+1 
print(count) 
   
n=int(input("enter a number..."))
add=0
for n in range(1,n+1):
    add=add+n
print(add)

n=int(input("enter a number..."))
sum=0
for n in range(2,n,2):
    sum=sum+1 
print(sum) 

n=int(input("enter a number..."))
sum=0
for n in range(1,n,2):
    sum=sum+1 
print(sum) 

a=int(input("enter a number.."))
for i in range(1,11):
    print(f"{a} * {i} = {a*i}")

n=int(input("enter a number..."))
mul=1
for n in range(1,n+1):
    mul=mul*n
print(mul)

n=input("enter yorr string...")
for ch in n:
     print(ch)

n=input("enter yorr string...")
for ch in n:
     print(ch, end=" ")

n=input("enter a num...")
count=0
for ch in n:
     count=count+1
     print(count)

n=input("enter a string...")
print(n.count("a"))


n=input("enter your string...")
count=0
for i in n:
     if i>="A" and i<="Z":
         count=count+1
         print("uppercase")