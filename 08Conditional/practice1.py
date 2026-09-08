a = float(input("Enter your first no.: "))
b = float(input("Enter your second no.: "))
c = input("What you want to do? (Add/Sub/Mult/Div): ")

if c == "Add" :
    add = a + b
    print(f"The answer is {add}")
elif c == "Sub" :
    sub = a - b
    print(f"The answer is {sub}")
elif c == "Mult" :
    mult = a*b 
    print(f"The answer is {mult}")
elif c == "Div" :
    div = a/b
    print(f"The answer is {div}")
else:
    print("Please write the following instruction correctly.")           
