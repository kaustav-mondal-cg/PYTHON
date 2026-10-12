# #Q1

# print("Our Menu \n1==> Pizza\n2==> Burger\n3==> Pasta\n4==> Sandwich")
# num = int(input("Enter your choice: "))

# match num:
#     case 1:
#         print("You selected Pizza")
#     case 2:
#         print("You selected Burger")
#     case 3:
#         print("You selected Pasta")
#     case 4:
#         print("You selected Sandwich")
#     case _ :
#         print("Invalid Input")

# #Q2

# print("1 ==> Wif - Fi\n2 ==> Bluetooth\n3 ==> Mobile Data\n4 ==> Airplane Mode\n5 ==> Exit")
# numb = int(input("Enter your choice: "))

# match numb:
#     case 1:
#         print("Wi - Fi selected")
#     case 2:
#         print("Bluetooth selected")
#     case 3:
#         print("Mobile data selected")
#     case 4:
#         print("airplane mode selected")
#     case 5:
#         print("Exited!")
#     case _:
#         print("Invalid Input")

# #Q3

# print("\t1 ==> Check Balance\n\t2 ==> Withdraw Money\n\t3 ==> Deposit Money\n\t4 ==> Change PIN\n\t5 ==> Exit")
# numb = int(input("Enter your choice: "))

# match numb:
#     case 1:
#         print("Checking Balance")
#     case 2:
#         print("Withdrawing Money")
#     case 3:
#         print("Depositing Money")
#     case 4:
#         print("Changing PIN")
#     case 5:
#         print("Exited!")
#     case _:
#         print("Inavlid Input")

# #Q4
# ligth = input("Enter the colour of Ligth at signal: ").lower()

# match ligth:
#     case "red":
#         print("Stop")
#     case "yellow":
#         print("Wait")
#     case "green":
#         print("Go")
#     case _ :
#         print("Invalid Input") 

# #Q5
# numb = 1
# while numb != 5:

#     print("\t1 ==> View Profile\n\t2 ==> View Courses \n\t3 ==> View Marks\n\t4 ==> View Attendance\n\t5 ==> Logout")

#     numb = int(input("Enter your choice: "))

#     match numb:
#         case 1:
#             print("Your Profile:")
#         case 2:
#             print("Courses:")
#         case 3:
#             print("Your Marks:")
#         case 4:
#             print("Your Attendance")
#         case 5:
#             print("Logged Out")
#         case _ :
#             print("Invalid Input")

# #Q6

# print("\t1 ==> Electronics \n\t2 ==> Clothing\n\t3 ==> Books\n\t4 ==> Grocery\n\t5 ==> Exit")
# numb = int(input("Enter your choice: "))

# match numb:
#     case 1:
#         print("Electronics")
#     case 2:
#         print("Clothing")
#     case 3:
#         print("Books")
#     case 4:
#         print("Grocery")
#     case 5:
#         print("Exited!")

# #Q7
# numb = 1
# while numb != 6:

#     print("\t1 ==>Account Balance\n\t2 ==> Mini Statement \n\t3 ==> Fund Transfer\n\t4 ==> Bill Payment\n\t5 ==> Customer Support\n\t6 ==> Exit")

#     numb = int(input("Enter your choice: "))

#     match numb:
#         case 1:
#             print("Balance:")
#         case 2:
#             print("Mini Statement:")
#         case 3:
#             print("Fund Transfer:")
#         case 4:
#             print("Bill Payments")
#         case 5:
#             print("Customer Support")
#         case 6:
#             print("Exited!")
#         case _ :
#             print("Invalid Input")

# #Q8
# numb = 1
# while numb != 5:

#     print("\t1 ==> Morning Show\n\t2 ==> Afternoon Show \n\t3 ==> Evening Show\n\t4 ==> Nigth Show\n\t5 ==> Exit")

#     numb = int(input("Enter your choice: "))

#     match numb:
#         case 1:
#             print("Morning Show Details are as follows:")
#         case 2:
#             print("Afternoon Show Details are as follows:")
#         case 3:
#             print("Evening Show Details are as follows:")
#         case 4:
#             print("Night Show Details are as follows:")
#         case 5:
#             print("Exited!")
#         case _ :
#             print("Invalid Input")

# #Q9

# print("\t1 ==> Sunny \n\t2 ==> Rainy\n\t3 ==> Cloudy\n\t4 ==> Snowy")
# numb = int(input("Enter your Weather: "))

# match numb:
#     case 1:
#         print("Wear Sunglasses")
#     case 2:
#         print("Carry an Umbrella")
#     case 3:
#         print("Weather may Change")
#     case 4:
#         print("Wear warm clothes")
#     case _:
#         print("Unkown Weather")

##Q10

# print("\t1 ==> UPI \n\t2 ==> Card\n\t3 ==> Cash\n\t4 ==> Wallet")
# numb = int(input("Enter your Payment method: "))

# match numb:
#     case 1:
#         print("UPI Payment selected")
#     case 2:
#         print("Card Payment selected")
#     case 3:
#         print("Cash Payment selected")
#     case 4:
#         print("Wallet Payment selected")
#     case _:
#         print("Invalid Payment method ")

##Q11

# print("\t1 : pdf \n\t2 : jpg\n\t3 : png\n\t4 : mp3\n\t5 : mp4")
# num = int(input("Enter your file type: "))

# match num:
#     case 1:
#         print("PDF file selected")
#     case 2:
#         print("JPG file selected")
#     case 3:
#         print("PNG file selected")
#     case 4:
#         print("MP3 file selected")
#     case 5:
#         print("MP4 file selected")
#     case _:
#         print("Invalid file type")


# # Q12. User Role

# choice = int(input("Enter Role Number (1-Admin, 2-Teacher, 3-Student, 4-Guest): "))

# match choice:
#     case 1:
#         print("Full Access")
#     case 2:
#         print("Teacher Dashboard")
#     case 3:
#         print("Student Dashboard")
#     case 4:
#         print("Limited Access")
#     case _:
#         print("Invalid Role")


# # Q13. Weekday or Weekend

# day = int(input("Enter Day Number: "))

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Invalid Day")


# # Q14. Customer Support Priority

# priority = int(input("Enter Priority Number: "))

# match priority:
#     case 1 | 2:
#         print("Normal Priority")
#     case 3 | 4:
#         print("Urgent Priority")
#     case _:
#         print("Invalid Priority")


# # Q15. Store Discount Category

# level = int(input("Enter Membership Number: "))

# match level:
#     case 1 | 2:
#         print("Basic Membership")
#     case 3 | 4:
#         print("Premium Membership")
#     case _:
#         print("Invalid Membership Level")


# # Q16. University Portal

# user_type = int(input("Enter User Type (1-Student, 2-Teacher): "))

# match user_type:
#     case 1:
#         option = int(input("Enter Option: "))

#         match option:
#             case 1:
#                 print("Opening Student Courses")
#             case 2:
#                 print("Opening Student Marks")
#             case 3:
#                 print("Opening Student Attendance")
#             case _:
#                 print("Invalid Option")

#     case 2:
#         option = int(input("Enter Option: "))

#         match option:
#             case 1:
#                 print("Opening Teacher Students")
#             case 2:
#                 print("Entering Marks")
#             case 3:
#                 print("Opening Teacher Attendance")
#             case _:
#                 print("Invalid Option")

#     case _:
#         print("Invalid User Type")


# # Q17. ATM with Account Type

# account = int(input("Enter Account Type (1-Savings, 2-Current): "))

# match account:
#     case 1:
#         print("Savings Account")
#         operation = int(input("Enter Operation: "))

#         match operation:
#             case 1:
#                 print("Check Balance Selected")
#             case 2:
#                 print("Deposit Selected")
#             case 3:
#                 print("Withdraw Selected")
#             case _:
#                 print("Invalid Operation")

#     case 2:
#         print("Current Account")
#         operation = int(input("Enter Operation: "))

#         match operation:
#             case 1:
#                 print("Check Balance Selected")
#             case 2:
#                 print("Deposit Selected")
#             case 3:
#                 print("Withdraw Selected")
#             case _:
#                 print("Invalid Operation")

#     case _:
#         print("Invalid Account Type")


# # Q18. E-Commerce Application

# category = int(input("Enter Category (1-Electronics, 2-Clothing): "))

# match category:
#     case 1:
#         product = int(input("Enter Product Number: "))

#         match product:
#             case 1:
#                 print("Mobile Selected")
#             case 2:
#                 print("Laptop Selected")
#             case 3:
#                 print("Headphones Selected")
#             case _:
#                 print("Invalid Product")

#     case 2:
#         product = int(input("Enter Product Number: "))

#         match product:
#             case 1:
#                 print("Shirt Selected")
#             case 2:
#                 print("Jeans Selected")
#             case 3:
#                 print("Shoes Selected")
#             case _:
#                 print("Invalid Product")

#     case _:
#         print("Invalid Category")


# # Q19. Food Delivery Application

# category = int(input("Enter Category (1-Vegetarian, 2-Non-Vegetarian): "))

# match category:
#     case 1:
#         food = int(input("Enter Food Number: "))

#         match food:
#             case 1:
#                 print("Paneer Selected")
#             case 2:
#                 print("Dal Selected")
#             case 3:
#                 print("Veg Biryani Selected")
#             case _:
#                 print("Invalid Food")

#     case 2:
#         food = int(input("Enter Food Number: "))

#         match food:
#             case 1:
#                 print("Chicken Biryani Selected")
#             case 2:
#                 print("Chicken Curry Selected")
#             case 3:
#                 print("Fish Fry Selected")
#             case _:
#                 print("Invalid Food")

#     case _:
#         print("Invalid Category")


# # Q20. Simple Calculator

# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# choice = int(input("Enter Operator Number (1-Add, 2-Subtract, 3-Multiply, 4-Divide): "))

# match choice:
#     case 1:
#         print("Result =", num1 + num2)
#     case 2:
#         print("Result =", num1 - num2)
#     case 3:
#         print("Result =", num1 * num2)
#     case 4:
#         if num2 != 0:
#             print("Result =", num1 / num2)
#         else:
#             print("Cannot Divide By Zero")
#     case _:
#         print("Invalid Operator")


# # Q21. Temperature Converter

# choice = int(input("Enter Choice (1-Celsius to Fahrenheit, 2-Fahrenheit to Celsius): "))
# temperature = int(input("Enter Temperature: "))

# match choice:
#     case 1:
#         result = (temperature * 9 / 5) + 32
#         print("Temperature =", result, "F")
#     case 2:
#         result = (temperature - 32) * 5 / 9
#         print("Temperature =", result, "C")
#     case _:
#         print("Invalid Choice")


# # Q22. Unit Converter

# choice = int(input("Enter Choice (1-KM to M, 2-M to KM, 3-KG to G, 4-G to KG): "))
# value = int(input("Enter Value: "))

# match choice:
#     case 1:
#         print(value * 1000, "meters")
#     case 2:
#         print(value / 1000, "kilometers")
#     case 3:
#         print(value * 1000, "grams")
#     case 4:
#         print(value / 1000, "kilograms")
#     case _:
#         print("Invalid Choice")


# # Q23. ATM Withdrawal

# account = int(input("Enter Account Type (1-Savings, 2-Current): "))

# match account:
#     case 1:
#         print("Savings Account")
#         amount = int(input("Enter Withdrawal Amount: "))

#         if amount > 0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid Amount")

#     case 2:
#         print("Current Account")
#         amount = int(input("Enter Withdrawal Amount: "))

#         if amount > 0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid Amount")

#     case _:
#         print("Invalid Account Type")

## 24

# n = int(input())

# for i in range(2, n):
#     if n % i == 0:
#         print("Not prime")
#         break
# else:
#     print("Prime")

## 27

# s = input()

# for ch in s:
#     if s.count(ch) >= 2:
#         print(ch)
#         break
# else:
#     print("No repeated character")

## 31

# for i in range(1, 6):
#     if i % 2 == 0:
#         pass
#     print(i)