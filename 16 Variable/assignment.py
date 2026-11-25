# # 1.Create a function with a local variable city and print it.

# def classroom():
#     standard = "12th"
#     city = "New York"
#     print(f"Standard: {standard}, City: {city}")

# classroom()

# #2 Create a global variable school. Read it inside a function.

# school = "Greenwood High"
# def read_school():
#     print(f"School: {school}")

# read_school()

# #3 Assign a variable inside an if block and print it outside the block

# if True:
#     country = "USA"
# print(f"Country: {country}")

# #4 Use a for loop to assign a loop variable. Print it after the loop.

# for i in range(5):
#     loop_variable = i
# print(f"Loop Variable: {loop_variable}")

# #5 Explain the difference between scope and lifetime in your own words.

# #Scope is where in your code a variable can be accessed, while lifetime is how long that variable exists in memory while the program runs.

# #6 200,100

# #7 
# clicks = 0
# def click():
#     global clicks
#     clicks += 1

# click()

# #8

## Because the variable `name` is assigned a value inside the function `show()`, Python treats it as a local variable. When the function tries to print `name`, it looks for a local variable `name` that has not been defined yet, leading to an UnboundLocalError

#9 Write a nested function that reads a variable from its enclosing function.

# def outer_function():
#     outer_variable = "I am from the outer function."

#     def inner_function():
#         print(outer_variable)  

#     inner_function()

# outer_function()  

#10 Write a function that returns a list. Show that the returned list can be changed by the caller.

# def list():
#     return [1, 2, 3]

# my_list = list()
# print(f"Original list: {my_list}")
# my_list.append(4)
# print(f"Modified list: {my_list}")

#11 Use nonlocal to create a counter that returns 1, 2, 3 across three calls.
# def create_counter():
#     n = 0
#     def counter():
#         nonlocal n
#         n += 1
#         return n
    
#     return counter

# c = create_counter()
# print(c())  
# print(c())  
# print(c())  

#12 
#3
#2
#1

#13 Explain why the loop variable in a normal for loop can remain available after the loop, but a list-comprehension variable in Python 3 does not overwrite an outer variable.

#Because in a normal for loop, the loop variable is defined in the outer scope, so it remains accessible after the loop. In contrast, a list comprehension creates its own local scope for the loop variable, preventing it from overwriting any outer variable with the same name.


#14 Create a function that returns another function. Explain which variable remains available and why.

# def outer_function():
#     outer_variable = "I am from the outer function."

#     def inner_function():
#         print(outer_variable)  # This variable remains available because it is in the enclosing scope of inner_function.

#     return inner_function

# print(outer_function())  # This will print the inner_function object, but not call it.

#15 Explain why variable names such as list, str, and sum should usually be avoided.

# Because these names are built-in functions in Python. Using them as variable names can lead to unexpected behavior and make the code harder to read and debug.