# def divide(c,d,/,*,a=20, b=2):  #c and d me ek sath value dena pare ga kui ki usko positional-only parameters bolte ha
#     return a / b, c+d           #a and b me randomly value de sakte ha kyu ki bo keyword-only ha

# print(divide(14,15,a=10,b=2))  


# def calculate(a, b, /, operation="add"):
#     if operation == "add":
#         return a + b
#     if operation == "multiply":
#         return a * b
#     return None

# print(calculate(3, 4))                        # 7
# print(calculate(3, 4, operation="multiply"))  # 12



# def create_user(name, *, age, city):
#     return f"{name}, age {age}, from {city}"

# print(create_user("Kaustav", age=18, city="Durgapur"))


# def book_ticket(source, destination, /, *, passenger, seat="regular"):
#     print(source, "to", destination)
#     print("Passenger:", passenger)
#     print("Seat:", seat)

# book_ticket("Pune", "Mumbai", passenger="Asha", seat="window")
# book_ticket("Pune", "Mumbai", passenger="Asha")



#-----------------*args-----------------------#

def add(*args):
    print(args)
    print(type(args))

add(10, 20, 30)



#------------------**kwargs---------------------#

def add(**kwargs):
    print(kwargs)
    print(type(kwargs))

add(a=10, b=20, c=30)