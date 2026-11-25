# # #Seating arrangement

# arr = [ "Ram", "Sharma", "Aditya", "Shivam", "Virat", "Varun", "Kaustav"]
# day = 1
# while day <= 7:
#     print(f"Day {day} seating arrangement: ")
#     c = 0
#     while c < len(arr):
#         print(arr[c], end=" ")
#         arr[c] = arr[c + 1] if c + 1 < len(arr) else arr[0]
#         c += 1
#     print()
#     day += 1




def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "password":
        print("Login successful!")
        break
    else:
        print("Invalid username or password.")
        print("Please try again.")
        print(login())  # Recursive call to login() for retry
        return login()  # Initial call to login()
print(login())  # Initial call to login()