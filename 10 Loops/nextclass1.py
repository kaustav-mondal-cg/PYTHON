# total = 0
# passed = True

# for i in range(1, 6):
#     marks = int(input(f"Enter marks for subject {i}: "))
#     total += marks

#     if marks < 35:
#         passed = False
# percentage = total / 5
# if passed:
#     if percentage >= 90:
#         grade = "A+"
#     elif percentage >= 80:
#         grade = "A"
#     elif percentage >= 70:
#         grade = "B"
#     elif percentage >= 60:
#         grade = "C"
#     elif percentage >= 50:
#         grade = "D"
#     else:
#         grade = "F"
# else:
#     grade = "F"
# print("Total:", total)
# print("Percentage:", percentage, "%")
# print("Grade:", grade)
# if passed:
#     print("Result: PASS")
# else:
#     print("Result: FAIL")



# total = 0
# discount = True

# for j in range(1,6):
#     price = int(input(f"Enter price of each product {j}: "))
#     total += price

#     if price < 1000:
#         discount = False
# if discount :
#     member = input("Are you a member? (Yes/No): ")
#     if price >= 5000:
#         if member == "Yes":
#             total = total*.25
#         else:
#             total = total*.20    
#     elif price >= 2000:
#             if member == "Yes" :
#                    total = total*.15
#             else:
#                    total = total*.10
#     elif price >= 1000:
#         if member == "Yes" :
#             total = tatol*.10
#         else:
#             total = total*.05
#     else:
#         total = total
# else:
#     total = total

# print (f"Your total cost is {total}")


total = 0

for j in range(1, 6):
    price = int(input(f"Enter price of product {j}: "))
    total += price

member = input("Are you a member? (Yes/No): ")

if total >= 5000:
    if member == "Yes":
        total -= total * 0.25
    else:
        total -= total * 0.20

elif total >= 2000:
    if member == "Yes":
        total -= total * 0.15
    else:
        total -= total * 0.10

elif total >= 1000:
    if member == "Yes":
        total -= total * 0.10
    else:
        total -= total * 0.05

print(f"Your total cost is {total}")