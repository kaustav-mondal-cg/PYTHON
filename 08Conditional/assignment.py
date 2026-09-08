#task 1

a=int(input("Enter a number: "))
if a>10:
    print("greater then 10")

#task 2

a=int(input("Enter age: "))
if a>18:
    print("Adult")

#task 3

a=int(input("Enter a number : "))
if a>0:
    print("positive")

#task 4

marks=int(input("enter a number :"))
if marks>=40:
    print("pass")

#task 5

a=int(input("Enter a number : "))
if a==0:
    print(0)

#task 6

a=int(input("Enter a number : "))
if a>0:
    print("Positive")
else:
    print("not positive")

#task 7

age=int(input("Enter a number : "))
if age>=18:
    print("Adult")
else:
    print("minor")

#task 8

numbers=int(input("Enter a number"))

if numbers%2==0:
    print("Even")
else:
    print("Odd")

#task 9

marks=int(input("Enter marks : "))

if marks>=40:
    print("pass")
else:
    print("fail")

#task 10   

a=int(input("Enter a number : "))
b=int(input("Enter a number : "))

if a>b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")
    
#task 11

marks = int(input("Enter your score (out of 100): "))

if marks > 100:
    print("Enetr a valid score.")
elif marks >= 90:
    print("You have recived A")
elif marks >= 75:
    print("You have recived B")
elif marks >= 60:
    print("You have recived C") 
elif marks >= 40:
    print("You have recived D")       
elif marks >= 0:
    print("You have recived F")
else :
    print ("Enetr a valid score.")   

#task12

number = int(input("Enter your number: "))

if number > 0 :
    print("The number is positive")
elif number == 0:
     print("The number is zero")
else:
     print("The number is negative")

#task 13

q = Monday
w = Tuesday
e = Wednesday
r = Thursday
t = Friday
print('''1 = Monday
2 = Tuesday
3 = Wednesday
4 = Thursday
5 = Friday''')

a = int(input("Enter your number according to the day: "))

if a == 1:
    print(q)
elif a == 2:
    print(w)
elif a == 3:
    print(e)
elif a == 4:
    print(r)
elif a == 5:
    print(t)    
else:
    print("Enter valid number.")        

#task 14

marks = int(input("Enter your score (out of 100): "))

if marks > 100:
    print("Enetr a valid score.")
elif marks >= 90:
    print("You have recived Excellent")
elif marks >= 75:
    print("You have recived Good") 
elif marks >= 33:
    print("You have recived Pass")       
elif marks >= 0:
    print("You have recived Fail")
else :
    print ("Enetr a valid score.")     

#task 15

a = int(input("Enter your number: "))
if a==1:
    print("1")
elif a==2:
    print("2")
elif a==3:
    print("3")
else:
    print("Other")         

#task 16

a = int(input("Enter your age: "))       
if a>=18 and a<=60:
    print("You are eligible")

#task 17

marks = int(input("Enter your score (out of 100):  "))    

if marks>=75:
    print("Good")
elif marks>=40:
    print("passed")
else:
    print("FAIL")

#task 18

a = int(input("Enter ur no.: "))

if a>100:
    print("Greater than 100 and it is positive")
elif a>0 :
    print("The no is positive")   
elif a == 0:
    print("it is zero")
else:
    peint("it is negative")        

#task 19

x = int(input("Enter your age: "))       
if x == 18:
    print("congrats u r 18 and will recieve an offer")
elif x>18 and x<60:
    print("You are eligible")
elif x == 60: 
    print("congrats u r 60 and will recieve an offer")   
else:
    print("you r not eligible")

#task 20  

number = int(input("Number: "))

if number != 0:
    if number > 0:
        print("The number is positive.")
    else:
        print("The number is negative.")
else:
    print("The number is zero.")

#task 21

age = int(input("Enter ur age: "))
marks = int(input("Enter your marks: "))
if age >= 18 and marks >= 40:
    print("Eligible")

#task 22

num = int(input("Enter ur number:"))
if num < 10 or num > 100:
    print("Special")

# task 23

age = int(input())
has_id = input() == "True"
if age >= 18 and has_id:
    print("Allowed")

#task 24

a = int(input())
b = int(input())
if a > 10 and b > 10:
    print("Both are greater than 10")

#task 25

num = int(input("Enter ur no.: "))
if num < 0 or num > 100:
    print("Outside range")

#task 26

is_closed = False
if not is_closed:
    print("Open")

#task 27

num = int(input())
if num >= 10 and num <= 50:
    print("Between 10 and 50")

#task 28

num = int(input())
if num < 10 or num > 50:
    print("Outside 10 to 50")

#task 29

is_student = input() == "True"
has_id = input() == "True"
has_ticket = input() == "True"
if is_student and has_id and has_ticket:
    print("Allowed")

#task 30

age = int(input())
marks = int(input())
has_id = input() == "True"
if age >= 18 and marks >= 40 and has_id:
    print("Eligible")
else:
    print("Not eligible")  