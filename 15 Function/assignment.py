# def addition(a,b):
#     a=int(input("enter ur first number"))
#     b=int(input("enter ur second number"))
#     return a+b
# print(addition(5,5))

# def sub(a,b):
#     a=int(input("enter ur first number"))
#     b=int(input("enter ur second number"))
#     return a-b
# print(sub(5,5))

# def mul(a,b):
#     a=int(input("enter ur first number"))
#     b=int(input("enter ur second number"))
#     return a*b
# print(mul(5,5))

# def div(a,b):
#     a=int(input("enter ur first number"))
#     b=int(input("enter ur second number"))
#     return a/b
# print(div(5,5))

# def floor(a,b):
#     a=int(input("enter ur first number"))
#     b=int(input("enter ur second number"))
#     return a//b
# print(floor(5,5))


# def loop(n):
#     digits = []
#     for ch in str(n):
#         digits.append(int(ch))
#     return digits

# print(loop(1234))
# for i in range(10):
#     print(loop(12345678))

# def isnumber(a):
#     if a%2==0:
#         return 'even'
#     else:
#         return 'odd'
# print(isnumber(a=int(input("enter a number"))))


# def prime(n):
#     if n <= 1:
#         return "Not Prime"
#     for i in range(2, n):
#         if n % i == 0:
#             return "Not Prime"
#     return "Prime"
# print(prime(n=int(input("enter ur number"))))



# def firstunique(arr):
#     for i in range(len(arr)):
#         unique = True
#         for j in range(len(arr)):
#             if i != j and arr[i]==arr[j]:
#                 unique = False
#                 break
#         if unique:
#             return arr[i]
#     return
# print(firstunique([4, 5, 1,2, 1, 4, 5]))

# def count(arr):
#     even_c=0
#     odd_c=0
#     for i in range(len(arr)):
#         if arr[i]%2==0:
#             even_c+=1
#         else:
#             odd_c+=1
#     return even_c,odd_c
# print(count([7,7,5,2,1,3,6]))



# def check_balance(balance):
#     print("Current Balance: ₹", balance)
#     return balance

# def credit(balance):
#     amount = int(input("Enter credit amount: "))

#     if amount > 0:
#         balance += amount
#         print("Amount credited successfully")
#         print("balance",balance)
#     else:
#         print("Invalid amount")
#     return balance

# def withdraw(balance):
#     amount = int(input("Enter withdrawal amount: "))
#     if amount <= 0:
#         print("Invalid amount")
#     elif amount > balance:
#         print("Insufficient balance")
#     else:
#         balance -= amount
#         print("Amount withdrawn successfully")
#         print("balance",balance)
#     return balance

# def main():
#     balance = 30000 
#     while True:
#         print("1. Credit")
#         print("2. Withdraw")
#         print("3. Check Balance")
#         print("4. Exit")
#         choice = int(input("Choose an option: "))
#         if choice == 1:
#             balance = credit(balance)


#         elif choice == 2:
#             balance = withdraw(balance)
#         elif choice == 3:
#             check_balance(balance)

#         elif choice == 4:
#             print("Thank you!")
#             break
#         else:
#             print("Invalid choice")
# main() 

# a=10
# b=20
# c=40
# def add(a,b):
#     c=a+b
#     return c
# def sub(a,b):
#     return a-b

# print(sub(add(a,b),c))

# def cal(a, b):
#     total = a + b
#     diff = a - b
#     return total, diff

# answer = cal(10, 4)
# print(answer)

# def cal(a, b):
#     total = a + b
#     diff = a - b
#     return total, diff

# total, diff = cal(10, 4)
# print(total, diff)

# def firstunique(arr):
#     for i in range(len(arr)):
#         unique = True
#         for j in range(len(arr)):
#             if i != j and arr[i]==arr[j]:
#                 unique = False
#                 break
#         if unique:
#             return arr[i]
#     return
# print(firstunique([4, 5, 1,2, 1, 4, 5]))

# arr = [12, 35, 1, 35, 20, 25]

# def second_largest(arr):
#     l=0
#     s_l=0
#     u=0
#     for i in range(len(arr)):
#         count=0
#         for j in range(len(arr)):
#             if arr[i]>l:
#                 s_l=l
#                 l=arr[i]
#             elif arr[i]>s_l and arr[i]<l:
#                 s_l=arr[i]
#     return s_l
# print(second_largest([12, 35, 1, 35, 20, 25, 25]))
# def s_u(arr1):
#     u=0
#     for  i in range(len(arr1)):
#         c=0
#         for j in range(len(arr1)):
#             if arr1[i]==arr1[j]:
#                 c+=1
#         if c==1:
#             u+=1
#     return u
# print(s_u([12, 35, 1, 35, 20, 25]))
# def c(b):
#     b+=1
#     if(b==7):
#         return b
#     c(b)
# print(c(1))

# def moveZeros(arr):
#     for i in range(len(arr)):
#         if arr[i]==0:
#             arr.remove(0)
#             arr.append(0)
#     return arr
# print(moveZeros([0, 0, 1, 2, 0, 3]))

# def missingNumber(arr):
#     n = len(arr) + 1
#     total = n * (n + 1) // 2
#     t_m = 0
#     for j in range(len(arr)):
#         t_m += arr[j]
#     miss = total - t_m
#     return miss
# print(missingNumber([2, 3, 1, 5]))


# def majorityElement(arr):
#     c=0
#     n=len(arr)//2
#     for i in range(len(arr)):
         

# def count(a):
#     a=a+1
#     if(a==1110):
#         return a
#     return count(a)
# print(count(4))

# n = 5
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
# print(fact)

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n - 1)
# print(factorial(5))

# def addd(*,a,b):
#     return a+b
# print(addd(a=8,b=3))                           

# c=0 
# for i in range(1,3):
#     c+=1
# print(c)
# def calculate(a, b, /, operation="add"):
#     if operation == "add":
#         return a + b
#     if operation == "multiply":
#         return a * b
#     return None

# print(calculate(3, 4))                 # 7
# print(calculate(3, 4, operation="multiply"))  # 12 

# def book_ticket(source, destination, /, *, passenger, seat="regular"):
#     print(source, "to", destination)
#     print("Passenger:", passenger)
#     print("Seat:", seat)

# book_ticket("Pune", "Mumbai", passenger="Asha", seat="window")
# book_ticket("Pune", "Mumbai", passenger="Asha")

# def add(*args):
#     t=0
#     for i in args:
#         t*=i
#     return t
# print(add(1,3,4,5))

# def add(a,b,*args):
#     print(type(args))
#     print(a,b)
#     print(args)
# print(add(1,3,4,5))
 
# def add(a,b,c):
#     print(a+b+c)
# num={'a':1,'b':3,'c':4}
# add(**num)


# s = input("Enter a string: ")
# for i in range(len(s)):
#     if s.index(s[i]) == i:
#         print(s[i], "=", s.count(s[i]))


s = input("Enter a string: ")
for i in range(len(s)): 
    c = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            c += 1
    repeat = False
    for k in range(i):
        if s[i] == s[k]:
            repeat = True
            break
    if repeat == False:
        print(s[i], "=", c)