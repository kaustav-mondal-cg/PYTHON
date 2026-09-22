#1

# s = input("Enter a string: ")

# upper = lower = digits = spaces = special = 0

# for ch in s:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
#     elif ch.isdigit():
#         digits += 1
#     elif ch == " ":
#         spaces += 1
#     else:
#         special += 1

# print("Uppercase:", upper)
# print("Lowercase:", lower)
# print("Digits:", digits)
# print("Spaces:", spaces)
# print("Special characters:", special)

# highest = upper

# if lower > highest:
#     highest = lower
# if digits > highest:
#     highest = digits
# if spaces > highest:
#     highest = spaces
# if special > highest:
#     highest = special

# count = 0

# if upper == highest:
#     count += 1
# if lower == highest:
#     count += 1
# if digits == highest:
#     count += 1
# if spaces == highest:
#     count += 1
# if special == highest:
#     count += 1

# if count > 1:
#     print("Tie")
# elif upper == highest:
#     print("Uppercase has the highest count")
# elif lower == highest:
#     print("Lowercase has the highest count")
# elif digits == highest:
#     print("Digits have the highest count")
# elif spaces == highest:
#     print("Spaces have the highest count")
# else:
#     print("Special characters have the highest count")


#2

# fail = passed = good = excellent = 0

# for i in range(1,11):
#     marks = int(input(f"Enter marks of Student {i}: "))
#     if marks < 35:
#         print("Fail")
#         fail += 1
#     elif marks <= 49:
#         print("Pass")
#         passed += 1
#     elif marks <= 74:
#         print("Good")
#         good += 1
#     else:
#         print("Excellent")
#         excellent += 1

# print("Fail:", fail)
# print("Pass:", passed)
# print("Good:", good)
# print("Excellent:", excellent)


#3

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# highest_score = -1
# highest_word = ""

# for word in words:
#     score = 0

#     for ch in word:
#         if ch.lower() in "aeiou":
#             score += 2
#         elif ch.isalpha():
#             score += 1
#         elif ch.isdigit():
#             score += 3
#         else:
#             score += 4

#     print(word, "=", score)

#     if score > highest_score:
#         highest_score = score
#         highest_word = word

# print("Highest scoring word:", highest_word)
# print("Score:", highest_score)

#4

# for i in range(5):
#     password = input("Enter password: ")

#     conditions = 0
#     upper = lower = digit = special = False

#     if len(password) >= 8:
#         conditions += 1

#     for ch in password:
#         if ch.isupper():
#             upper = True
#         elif ch.islower():
#             lower = True
#         elif ch.isdigit():
#             digit = True
#         else:
#             special = True

#     if upper:
#         conditions += 1
#     if lower:
#         conditions += 1
#     if digit:
#         conditions += 1
#     if special:
#         conditions += 1

#     if conditions == 5:
#         print("Strong")
#     elif conditions >= 3:
#         print("Medium")
#     else:
#         print("Weak") 

#5

# sentence = str(input("Enter your sentence: "))

# words = sentence.split()

# if len(words) <=3:
#     print("Short")
# elif len(words) <=6:
#     print("Medium")
# else:
#     print("Long")        

#6

