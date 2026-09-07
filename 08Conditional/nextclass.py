Citizen = input("Are you the citizen of India? (Yes/No): ")

if Citizen == "Yes" or Citizen == "yes" or Citizen == "YES":
    Age = int(input("Enter your age: "))
    if Age >= 18:
        print("You are eligible to vote")
    if Age < 18:
        print("You are not eligible to vote")
if Citizen == "No" or Citizen == "no" or Citizen == "NO":
    print("You are not eligible to vote")