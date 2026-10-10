# number = int(input("Enter a number: "))

# while number != 0:
#     print("You entered:", number)
#     number = int(input("Enter a number: "))

# print("Loop ended")


num = int(input("Number: "))
while num>0:
    digit = num%10
    print(digit)
    num = num//10