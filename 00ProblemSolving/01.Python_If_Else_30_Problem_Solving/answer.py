# #1
# num = float(input("Enter a number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


# #2

# num = int(input("Enter a number: "))

# if num == 0:
#     print("Zero")
# elif num > 0:
#     if num % 2 == 0:
#         print("Positive Even")
#     else:
#         print("Positive Odd")
# else:
#     if num % 2 == 0:
#         print("Negative Even")
#     else:
#         print("Negative Odd")


# #3

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# if a > b:
#     print(a, "is larger")
# elif b > a:
#     print(b, "is larger")
# else:
#     print("Both are equal")


# #4

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# if a <= b and a <= c:
#     print(a, "is the smallest")
# elif b <= a and b <= c:
#     print(b, "is the smallest")
# else:
#     print(c, "is the smallest")


# #5

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# if a >= b and a >= c:
#     print(a, "is the largest")
# elif b >= a and b >= c:
#     print(b, "is the largest")
# else:
#     print(c, "is the largest")


# #6

# num = int(input("Enter a number: "))

# if num % 5 == 0 and num % 11 == 0:
#     print("Divisible by both 5 and 11")
# elif num % 5 == 0:
#     print("Divisible only by 5")
# elif num % 11 == 0:
#     print("Divisible only by 11")
# else:
#     print("Divisible by neither")


# #7.

# num = int(input("Enter a number: "))

# if num % 3 == 0 and num % 7 == 0:
#     print("Divisible by both 3 and 7")
# elif num % 3 == 0:
#     print("Divisible only by 3")
# elif num % 7 == 0:
#     print("Divisible only by 7")
# else:
#     print("Divisible by neither")


# #8

# marks = float(input("Enter marks: "))

# if marks < 0 or marks > 100:
#     print("Invalid marks")
# elif marks >= 40:
#     print("Pass")
# else:
#     print("Fail")


# #9.

# marks = float(input("Enter marks: "))

# if marks < 0 or marks > 100:
#     print("Invalid marks")
# elif marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# elif marks >= 60:
#     print("Grade D")
# elif marks >= 40:
#     print("Grade E")
# else:
#     print("Fail")


# #10.

# age = int(input("Enter your age: "))

# if age < 0 or age > 120:
#     print("Invalid age")
# elif age < 18:
#     print("Cannot vote")
# else:
#     print("Can vote")


# #11

# year = int(input("Enter year: "))

# if year <= 0:
#     print("Invalid year")
# elif year % 400 == 0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("Not a leap year")
# elif year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")


# #12

# ch = input("Enter one character: ")

# if len(ch) != 1:
#     print("Invalid input")
# elif ch >= 'A' and ch <= 'Z':
#     print("Uppercase alphabet")
# elif ch >= 'a' and ch <= 'z':
#     print("Lowercase alphabet")
# elif ch >= '0' and ch <= '9':
#     print("Digit")
# else:
#     print("Special character")


# #13

# ch = input("Enter one character: ")

# if len(ch) != 1:
#     print("Invalid input")
# elif (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
#     if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
#         print("Vowel")
#     elif ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
#         print("Vowel")
#     else:
#         print("Consonant")
# else:
#     print("Invalid input")


# #14

# cp = float(input("Enter cost price: "))
# sp = float(input("Enter selling price: "))

# if cp < 0 or sp < 0:
#     print("Invalid price")
# elif sp > cp:
#     print("Profit =", sp - cp)
# elif cp > sp:
#     print("Loss =", cp - sp)
# else:
#     print("No profit and no loss")


# #15

# cp = float(input("Enter cost price: "))
# sp = float(input("Enter selling price: "))

# if cp <= 0 or sp < 0:
#     print("Invalid price")
# elif sp > cp:
#     profit = sp - cp
#     percentage = (profit / cp) * 100
#     print("Profit =", profit)
#     print("Profit percentage =", percentage, "%")
# elif cp > sp:
#     loss = cp - sp
#     percentage = (loss / cp) * 100
#     print("Loss =", loss)
#     print("Loss percentage =", percentage, "%")
# else:
#     print("No profit and no loss")


# #16

# units = float(input("Enter electricity units: "))

# if units < 0:
#     print("Invalid units")
# elif units <= 100:
#     bill = units * 5
#     print("Electricity bill =", bill)
# elif units <= 200:
#     bill = (100 * 5) + ((units - 100) * 7)
#     print("Electricity bill =", bill)
# else:
#     bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
#     print("Electricity bill =", bill)


# #17

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# operator = input("Enter operator (+, -, *, /): ")

# if operator == '+':
#     print("Result =", a + b)
# elif operator == '-':
#     print("Result =", a - b)
# elif operator == '*':
#     print("Result =", a * b)
# elif operator == '/':
#     if b == 0:
#         print("Cannot divide by zero")
#     else:
#         print("Result =", a / b)
# else:
#     print("Invalid operator")


# #18

# temp = float(input("Enter temperature in Celsius: "))

# if temp < 0:
#     print("Freezing")
# elif temp <= 15:
#     print("Very Cold")
# elif temp <= 25:
#     print("Cold")
# elif temp <= 35:
#     print("Normal")
# else:
#     print("Hot")


# #19

# num = float(input("Enter a number: "))

# if num < 0:
#     print("Negative")
# elif num <= 10:
#     print("Number is between 0 and 10")
# elif num <= 50:
#     print("Number is between 11 and 50")
# elif num <= 100:
#     print("Number is between 51 and 100")
# else:
#     print("Above 100")


# #20

# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))

# if a <= 0 or b <= 0 or c <= 0:
#     print("Invalid triangle")
# elif a + b > c and a + c > b and b + c > a:
#     print("Valid triangle")
# else:
#     print("Invalid triangle")


# #21

# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))

# if a <= 0 or b <= 0 or c <= 0:
#     print("Invalid triangle")
# elif a + b <= c or a + c <= b or b + c <= a:
#     print("Invalid triangle")
# elif a == b and b == c:
#     print("Equilateral triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")


# #22

# balance = float(input("Enter account balance: "))
# amount = float(input("Enter withdrawal amount: "))

# if balance < 0:
#     print("Invalid balance")
# elif amount <= 0:
#     print("Invalid withdrawal amount")
# elif amount % 100 != 0:
#     print("Amount must be divisible by 100")
# elif amount > balance:
#     print("Insufficient balance")
# elif balance - amount < 500:
#     print("Minimum Rs.500 balance must remain")
# else:
#     balance = balance - amount
#     print("Withdrawal successful")
#     print("Remaining balance:", balance)


# #23

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username != "admin":
#     print("User not found")
# elif password != "python123":
#     print("Wrong password")
# else:
#     print("Login successful")


# #24

# amount = float(input("Enter purchase amount: "))

# if amount < 0:
#     print("Invalid amount")
# else:
#     if amount < 500:
#         discount_percent = 0
#     elif amount < 1000:
#         discount_percent = 5
#     elif amount < 2000:
#         discount_percent = 10
#     elif amount < 5000:
#         discount_percent = 15
#     else:
#         discount_percent = 20

#     discount = amount * discount_percent / 100
#     final_amount = amount - discount

#     print("Original amount:", amount)
#     print("Discount:", discount_percent, "%")
#     print("Discount amount:", discount)
#     print("Final amount:", final_amount)


# #25

# m1 = float(input("Enter marks in subject 1: "))
# m2 = float(input("Enter marks in subject 2: "))
# m3 = float(input("Enter marks in subject 3: "))

# if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100 or m3 < 0 or m3 > 100:
#     print("Invalid marks")
# elif m1 < 35 or m2 < 35 or m3 < 35:
#     print("Fail")
# else:
#     average = (m1 + m2 + m3) / 3
#     print("Average:", average)

#     if average >= 75:
#         print("Distinction")
#     elif average >= 60:
#         print("First Class")
#     elif average >= 50:
#         print("Second Class")
#     else:
#         print("Pass")


# #26

# day = int(input("Enter day: "))
# month = int(input("Enter month: "))
# year = int(input("Enter year: "))

# if year <= 0:
#     print("Invalid date")
# elif month < 1 or month > 12:
#     print("Invalid date")
# else:
#     if year % 400 == 0:
#         leap = True
#     elif year % 100 == 0:
#         leap = False
#     elif year % 4 == 0:
#         leap = True
#     else:
#         leap = False

#     if month == 2:
#         if leap:
#             max_days = 29
#         else:
#             max_days = 28
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         max_days = 30
#     else:
#         max_days = 31

#     if day >= 1 and day <= max_days:
#         print("Valid date")
#     else:
#         print("Invalid date")


# #27

# hours = int(input("Enter hours: "))
# minutes = int(input("Enter minutes: "))
# seconds = int(input("Enter seconds: "))

# if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and seconds >= 0 and seconds <= 59:
#     print("Valid time")
# else:
#     print("Invalid time")


# #28

# name1 = input("Enter first person's name: ")
# age1 = int(input("Enter first person's age: "))

# name2 = input("Enter second person's name: ")
# age2 = int(input("Enter second person's age: "))

# name3 = input("Enter third person's name: ")
# age3 = int(input("Enter third person's age: "))

# if age1 < 0 or age2 < 0 or age3 < 0:
#     print("Invalid age")
# elif age1 == age2 and age2 == age3:
#     print("All three are of the same age")
# elif age1 == age2 and age1 < age3:
#     print(name1, "and", name2, "are the youngest")
# elif age1 == age3 and age1 < age2:
#     print(name1, "and", name3, "are the youngest")
# elif age2 == age3 and age2 < age1:
#     print(name2, "and", name3, "are the youngest")
# elif age1 < age2 and age1 < age3:
#     print(name1, "is the youngest")
# elif age2 < age1 and age2 < age3:
#     print(name2, "is the youngest")
# else:
#     print(name3, "is the youngest")


# #29

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a == b or b == c or a == c:
#     print("Please enter three different numbers")
# elif (a > b and a < c) or (a < b and a > c):
#     print(a, "is the second largest")
# elif (b > a and b < c) or (b < a and b > c):
#     print(b, "is the second largest")
# else:
#     print(c, "is the second largest")


# #30

# age = int(input("Enter age: "))
# marks = float(input("Enter marks: "))
# income = float(input("Enter family income: "))
# attendance = float(input("Enter attendance percentage: "))

# eligible = True

# if age < 0 or age > 120:
#     print("Invalid age")
#     eligible = False
# elif age < 18 or age > 25:
#     print("Failed: Age must be between 18 and 25")
#     eligible = False

# if marks < 0 or marks > 100:
#     print("Invalid marks")
#     eligible = False
# elif marks < 85:
#     print("Failed: Marks below 85")
#     eligible = False

# if income < 0:
#     print("Invalid family income")
#     eligible = False
# elif income > 300000:
#     print("Failed: Family income above Rs.300000")
#     eligible = False

# if attendance < 0 or attendance > 100:
#     print("Invalid attendance")
#     eligible = False
# elif attendance < 75:
#     print("Failed: Attendance below 75%")
#     eligible = False

# if eligible:
#     print("Scholarship Approved")
# else:
#     print("Scholarship Rejected")
