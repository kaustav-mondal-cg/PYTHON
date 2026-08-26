# PART 3 — Practical Programs

a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


x = 5
y = 2.5
print("Addition:", x + y, type(x + y))
print("Subtraction:", x - y, type(x - y))
print("Multiplication:", x * y, type(x * y))
print("Division:", x / y, type(x / y))
print("Floor Division:", x // y, type(x // y))
print("Modulus:", x % y, type(x % y))
print("Exponentiation:", x ** y, type(x ** y))


m1, m2, m3 = 80, 75, 90
total = m1 + m2 + m3
avg = total / 3
print("Total:", total)
print("Average:", avg)


price = 50
quantity = 4
total_price = price * quantity
print("Total Price:", total_price)


num = 7
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")


a, b = 7, 3
print("Positive Division:", a / b)
print("Positive Floor Division:", a // b)

a, b = -7, 3
print("Negative Division:", a / b)
print("Negative Floor Division:", a // b)


a, b = -8, -3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)


print("5 - 3 =", 5 - 3)
print("5 - (-3) =", 5 - (-3))
print("-5 - 3 =", -5 - 3)
print("-5 - (-3) =", -5 - (-3))

print("5 // 2 =", 5 // 2)
print("-5 // 2 =", -5 // 2)
print("5 // -2 =", 5 // -2)
print("-5 // -2 =", -5 // -2)
print("Note: Floor division rounds DOWN (towards -∞), not just removing decimals.")

print("5 % 2 =", 5 % 2)
print("-5 % 2 =", -5 % 2)
print("5 % -2 =", 5 % -2)
print("-5 % -2 =", -5 % -2)
print("Note: Result sign follows divisor.")



# PART 4 — Operator Precedence



print("10 + 5 * 2 =", 10 + 5 * 2)
print("20 - 4 / 2 =", 20 - 4 / 2)
print("10 + 20 / 5 * 2 =", 10 + 20 / 5 * 2)
print("2 + 3 * 4 ** 2 =", 2 + 3 * 4 ** 2)
print("100 - 20 // 5 =", 100 - 20 // 5)
print("Order: ** > * / // % > + -")


print("\n=== Task 12: Parentheses ===")
print("10 + 5 * 2 =", 10 + 5 * 2)
print("(10 + 5) * 2 =", (10 + 5) * 2)

print("20 - 10 / 2 =", 20 - 10 / 2)
print("(20 - 10) / 2 =", (20 - 10) / 2)

print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)
print("Parentheses change priority of operations.")


# PART 5 — Boolean Arithmeti

print("True + False =", True + False, type(True + False))
print("True - False =", True - False)
print("True * False =", True * False)
print("True / False -> Error handled below")

try:
    print(True / False)
except Exception as e:
    print("Error:", e)

print("True ** 2 =", True ** 2)


print("\n=== Task 14 ===")
print("True + 5 =", True + 5)
print("False + 5 =", False + 5)
print("True * 10 =", True * 10)
print("False * 10 =", False * 10)
print("True - 5 =", True - 5)
print("False - 5 =", False - 5)
print("Explanation: True=1, False=0")



# PART 6 — String Operations



first = "Kaustav"
last = "College"
print("Full Name:", first + " " + last)


print("\n=== Task 16 ===")
word = "Hi "
print(word * 3)

try:
    print(word * 2.5)
except Exception as e:
    print("Error:", e)


print("\n=== Task 17 ===")
s1 = "Hello"
s2 = "World"
print("String + String:", s1 + s2)

try:
    print(s1 - s2)
except Exception as e:
    print("Error:", e)

print("String * int:", s1 * 3)

try:
    print(s1 / s2)
except Exception as e:
    print("Error:", e)



# PART 7 — None Type

value = None

try:
    print(value + 5)
except Exception as e:
    print("Error:", e)

print("Explanation: None has no numeric value, so arithmetic is not allowed.")



# PART 8 — Error Handling



# Division by zero
try:
    print(10 / 0)
except Exception as e:
    print("ZeroDivisionError:", e)

# Invalid string arithmetic
try:
    print("A" - "B")
except Exception as e:
    print("String Error:", e)

# None arithmetic
try:
    print(None + 5)
except Exception as e:
    print("None Error:", e)



# PART 9 — Mini Calculator


a, b = 12, 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)



# PART 10 — Final Challenge


a = 10
b = -3
c = 2.5

expressions = [
    a + b,
    a - b,
    a * c,
    a / c,
    a // b,
    a % b,
    a ** 2,
    (a + b) * c,
    a + b * c,
    (a + b * c) ** 2
]

for i, exp in enumerate(expressions, 1):
    print(f"Expression {i} result:", exp)

print("\nNote: Precedence and negative numbers affect results.")