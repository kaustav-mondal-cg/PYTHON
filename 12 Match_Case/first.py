# choice = 2

# match choice:
#     case 1:
#         print("Add")
#     case 2:
#         print("Subtract")
#     case 3:
#         print("Multiply")
#     case 4:
#         print("Divide")
#     case _:
#         print("Invalid Choice")

# a = int(input("Enter your first number: "))        
# b = int(input("Enter your second number: "))        
# Operator = input ("Enter your operator (+,-,*,/): ")
# match Operator:
#     case "+":
#         print(a + b)
#     case "-":
#         print(a - b)
#     case "*":
#         print(a * b)
#     case "/":
#         print(a / b)
#     case _:
#         print("Invalid Operator")

a = int(input("Enter your first number: "))        
b = int(input("Enter your second number: "))

Choice = int(input("""Enter a Choice of operation do you want to perform:
                  1.Addition
                  2.Substraction
                  3.Multiplication
                  4.Division
                  5.Exit: 
                  """))
while Choice != 5:
    match Choice:
        case 1:
            print(f"The Addition of {a} and {b} is: ", a + b)
        case 2:
            print(f"The Substraction of {a} and {b} is: ", a - b)
        case 3:
            print(f"The Multiplication of {a} and {b} is: ", a * b)
        case 4:
            print(f"The Division of {a} and {b} is: ", a / b)
        case _:
            print("Invalid Choice")
    Choice = int(input("""Enter a Choice of operation do you want to perform:
                  1.Addition
                  2.Substraction
                  3.Multiplication
                  4.Division
                  5.Exit:
                  """))

