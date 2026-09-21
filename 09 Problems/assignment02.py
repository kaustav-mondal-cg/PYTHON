# 1
# IPO:
#Input: a, b
#Process: total = a + b
#Output: total

# ALGORITHM:
#Start
#Read a and b
#Calculate total = a + b
#Print total
#Stop

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)


# 2
# IPO:
#Input: num
#Process: Check num % 2 == 0
#Output: "Even" or "Odd"
#
# ALGORITHM:
#   1. Start
#   2. Read num
#   3. If num % 2 == 0, print "Even"
#   4. Else, print "Odd"
#   5. Stop

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3
# IPO:
#   Input: x, y, z
#   Process: Compare x, y, z to find the largest
#   Output: Largest number
#
# ALGORITHM:
#   1. Start
#   2. Read x, y, z
#   3. If x >= y and x >= z, print x
#   4. Else if y >= z, print y
#   5. Else, print z
#   6. Stop

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x >= y and x >= z:
    print("Largest =", x)
elif y >= x and y >= z:
    print("Largest =", y)
else:
    print("Largest =", z)


# 4
# IPO :
#   Input: x (age)
#   Process: Check x >= 18
#   Output: "Eligible" or "Not Eligible"
#
# ALGORITHM:
#   1. Start
#   2. Read x
#   3. If x >= 18, print "Eligible"
#   4. Else, print "Not Eligible"
#   5. Stop

age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 5
# IPO :
#   Input: x (price)
#   Process: If x >= 2000, final_price = x - (x * 0.20), else final_price = x
#   Output: final_price
#
# ALGORITHM:
#   1. Start
#   2. Read x
#   3. If x >= 2000, final_price = x - (x * 0.20)
#   4. Else, final_price = x
#   5. Print final_price
#   6. Stop

price = float(input("Enter price: "))
if price >= 2000:
    discount = price * 0.20
    final_price = price - discount
else:
    final_price = price

print("Final price =", final_price)


# 6
# IPO :
#   Input: x, y, z (m1, m2, m3)
#   Process: avg = (x + y + z) / 3, check avg >= 40
#   Output: "Pass" or "Fail"
#
# ALGORITHM:
#   1. Start
#   2. Read x, y, z
#   3. avg = (x + y + z) / 3
#   4. If avg >= 40, print "Pass"
#   5. Else, print "Fail"
#   6. Stop

m1 = float(input("Enter marks 1: "))
m2 = float(input("Enter marks 2: "))
m3 = float(input("Enter marks 3: "))

average = (m1 + m2 + m3) / 3
print("Average =", average)

if average >= 40:
    print("Pass")
else:
    print("Fail")
