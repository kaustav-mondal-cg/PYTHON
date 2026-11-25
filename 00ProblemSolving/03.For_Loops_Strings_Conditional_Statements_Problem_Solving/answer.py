
# # 1.

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
# print("Special:", special)

# highest = upper
# for value in [lower, digits, spaces, special]:
#     if value > highest:
#         highest = value

# count = 0
# for value in [upper, lower, digits, spaces, special]:
#     if value == highest:
#         count += 1

# if count > 1:
#     print("Tie")
# else:
#     if highest == upper:
#         print("Uppercase has highest count")
#     elif highest == lower:
#         print("Lowercase has highest count")
#     elif highest == digits:
#         print("Digits have highest count")
#     elif highest == spaces:
#         print("Spaces have highest count")
#     else:
#         print("Special characters have highest count")


# # 2.

# fail = passed = good = excellent = 0

# for i in range(10):
#     marks = int(input("Enter marks: "))

#     if marks < 0 or marks > 100:
#         print("Invalid marks")
#     elif marks < 35:
#         print("Fail")
#         fail += 1
#     elif marks < 50:
#         print("Pass")
#         passed += 1
#     elif marks < 75:
#         print("Good")
#         good += 1
#     else:
#         print("Excellent")
#         excellent += 1

# print("Fail:", fail)
# print("Pass:", passed)
# print("Good:", good)
# print("Excellent:", excellent)


# # 3.

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

#     print(word, "Score:", score)

#     if score > highest_score:
#         highest_score = score
#         highest_word = word

# print("Highest scoring word:", highest_word)


# # 4. 

# for i in range(5):
#     password = input("Enter password: ")

#     upper = lower = digit = special = 0

#     for ch in password:
#         if ch.isupper():
#             upper = 1
#         elif ch.islower():
#             lower = 1
#         elif ch.isdigit():
#             digit = 1
#         else:
#             special = 1

#     score = 0

#     if len(password) >= 8:
#         score += 1
#     score += upper + lower + digit + special

#     if score == 5:
#         print("Strong")
#     elif score >= 3:
#         print("Medium")
#     else:
#         print("Weak")


# # 5. 

# sentence = input("Enter a sentence: ")
# words = sentence.split()

# short = medium = long = 0

# for word in words:
#     length = len(word)

#     if length <= 3:
#         print(word, "Short")
#         short += 1
#     elif length <= 6:
#         print(word, "Medium")
#         medium += 1
#     else:
#         print(word, "Long")
#         long += 1

# print("Short words:", short)
# print("Medium words:", medium)
# print("Long words:", long)


# # 6. 

# for i in range(5):
#     num = input("Enter a number: ")

#     even = odd = 0

#     for ch in num:
#         if ch.isdigit():
#             if int(ch) % 2 == 0:
#                 even += 1
#             else:
#                 odd += 1

#     print("Even digits:", even)
#     print("Odd digits:", odd)

#     if even > odd:
#         print("Even occurs more")
#     elif odd > even:
#         print("Odd occurs more")
#     else:
#         print("Equal")


# # 7.

# s = input("Enter a string: ")

# for i in range(len(s)):
#     already_checked = False

#     for k in range(i):
#         if s[k] == s[i]:
#             already_checked = True
#             break

#     if already_checked:
#         continue

#     count = 0

#     for ch in s:
#         if ch == s[i]:
#             count += 1

#     if count > 1:
#         if count == 2:
#             category = "Duplicate"
#         elif count <= 4:
#             category = "Repeated"
#         else:
#             category = "Highly Repeated"

#         print(s[i], count, category)


# # 8. 

# total = 0
# budget = regular = premium = luxury = 0

# for i in range(8):
#     price = float(input("Enter product price: "))

#     total += price

#     if price < 500:
#         budget += 1
#         print("Budget")
#     elif price < 2000:
#         regular += 1
#         print("Regular")
#     elif price < 5000:
#         premium += 1
#         print("Premium")
#     else:
#         luxury += 1
#         print("Luxury")

# print("Total:", total)
# print("Budget:", budget)
# print("Regular:", regular)
# print("Premium:", premium)
# print("Luxury:", luxury)
# print("Average:", total / 8)


# # 9.

# s = input("Enter a string: ")

# vowels = consonants = digits = special = 0

# for i in range(len(s)):
#     ch = s[i]

#     if ch.lower() in "aeiou" and ch.isalpha():
#         category = "Vowel"
#         vowels += 1
#     elif ch.isalpha():
#         category = "Consonant"
#         consonants += 1
#     elif ch.isdigit():
#         category = "Digit"
#         digits += 1
#     else:
#         category = "Special"
#         special += 1

#     if i % 2 == 0:
#         position = "Even"
#     else:
#         position = "Odd"

#     print(ch, "Position:", i, position, category)

# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Special:", special)


# # 10. 

# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j % 15 == 0:
#             print("Z", end=" ")
#         elif j % 3 == 0:
#             print("X", end=" ")
#         elif j % 5 == 0:
#             print("Y", end=" ")
#         else:
#             print(j, end=" ")
#     print()


# # 11. 

# for i in range(5):
#     username = input("Enter username: ")

#     digits = underscores = 0
#     invalid = False

#     for ch in username:
#         if ch.isdigit():
#             digits += 1
#         elif ch == "_":
#             underscores += 1
#         elif not ch.isalnum():
#             invalid = True

#     if (len(username) < 5 or len(username) > 15
#             or not username[0:1].isalpha() or invalid):
#         print("Invalid")
#     elif digits > 3 or underscores > 2:
#         print("Needs Improvement")
#     else:
#         print("Valid")


# # 12.

# s = input("Enter a sentence: ")

# vowels = consonants = 0
# a = e = i = o = u = 0

# for ch in s.lower():
#     if ch in "aeiou":
#         vowels += 1

#         if ch == "a":
#             a += 1
#         elif ch == "e":
#             e += 1
#         elif ch == "i":
#             i += 1
#         elif ch == "o":
#             o += 1
#         elif ch == "u":
#             u += 1

#     elif ch.isalpha():
#         consonants += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("A:", a, "E:", e, "I:", i, "O:", o, "U:", u)

# if vowels > consonants:
#     print("Vowels Win")
# elif consonants > vowels:
#     print("Consonants Win")
# else:
#     print("Draw")


# # 13. 

# revenue = 0

# for i in range(6):
#     units = int(input("Enter units: "))

#     if units < 0:
#         print("Invalid units")
#         continue

#     if units <= 100:
#         bill = units * 5
#     elif units <= 200:
#         bill = 100 * 5 + (units - 100) * 7
#     elif units <= 400:
#         bill = 100 * 5 + 100 * 7 + (units - 200) * 10
#     else:
#         bill = 100 * 5 + 100 * 7 + 200 * 10 + (units - 400) * 15

#     revenue += bill

#     if bill < 1000:
#         category = "Low"
#     elif bill <= 3000:
#         category = "Medium"
#     else:
#         category = "High"

#     print("Bill:", bill, category)

# print("Total Revenue:", revenue)


# # 14.

# sentence = input("Enter sentence: ")
# words = sentence.split()

# for word in words:
#     vowels = consonants = 0

#     for ch in word.lower():
#         if ch in "aeiou":
#             vowels += 1
#         elif ch.isalpha():
#             consonants += 1

#     if vowels > consonants:
#         print(word, "Vowel Heavy")
#     elif consonants > vowels:
#         print(word, "Consonant Heavy")
#     else:
#         print(word, "Balanced")


# # 15.

# even = odd = positive = negative = zero = 0
# largest = None

# for i in range(3):
#     for j in range(3):
#         num = int(input("Enter matrix value: "))

#         if num % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#         if num > 0:
#             positive += 1
#         elif num < 0:
#             negative += 1
#         else:
#             zero += 1

#         if largest is None or num > largest:
#             largest = num

# print("Even:", even)
# print("Odd:", odd)
# print("Positive:", positive)
# print("Negative:", negative)
# print("Zero:", zero)
# print("Largest:", largest)


# # 16.

# password = input("Enter password: ")

# upper = lower = digits = special = 0

# for ch in password:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
#     elif ch.isdigit():
#         digits += 1
#     else:
#         special += 1

# total = len(password)

# if total > 0:
#     print("Uppercase:", upper * 100 / total, "%")
#     print("Lowercase:", lower * 100 / total, "%")
#     print("Digits:", digits * 100 / total, "%")
#     print("Special:", special * 100 / total, "%")

#     highest = upper
#     category = "Uppercase"

#     if lower > highest:
#         highest = lower
#         category = "Lowercase"
#     if digits > highest:
#         highest = digits
#         category = "Digits"
#     if special > highest:
#         highest = special
#         category = "Special"

#     print("Dominant category:", category)


# # 17.

# highest_marks = -1
# top_student = ""

# for i in range(5):
#     name = input("Enter name: ")
#     marks = float(input("Enter marks: "))

#     vowels = consonants = 0

#     for ch in name.lower():
#         if ch in "aeiou":
#             vowels += 1
#         elif ch.isalpha():
#             consonants += 1

#     if marks < 35:
#         grade = "Fail"
#     elif marks < 50:
#         grade = "C"
#     elif marks < 75:
#         grade = "B"
#     elif marks <= 100:
#         grade = "A"
#     else:
#         grade = "Invalid"

#     print("Grade:", grade)
#     print("Name characters:", len(name))
#     print("Vowels:", vowels)
#     print("Consonants:", consonants)

#     if vowels > consonants:
#         print("More vowels")
#     elif consonants > vowels:
#         print("More consonants")
#     else:
#         print("Equal vowels and consonants")

#     if 0 <= marks <= 100 and marks > highest_marks:
#         highest_marks = marks
#         top_student = name

# print("Top Student:", top_student)


# # 18.

# balance = float(input("Enter starting balance: "))
# deposit_count = withdrawal_count = 0

# for i in range(7):
#     transaction = input("Enter D for deposit or W for withdrawal: ").upper()
#     amount = float(input("Enter amount: "))

#     if amount <= 0:
#         print("Invalid amount")
#         continue

#     if transaction == "D":
#         balance += amount
#         deposit_count += 1
#     elif transaction == "W":
#         if amount > balance:
#             print("Insufficient Balance")
#             continue
#         balance -= amount
#         withdrawal_count += 1
#     else:
#         print("Invalid transaction")
#         continue

#     if balance < 1000:
#         print("Low Balance")

# print("Final Balance:", balance)
# print("Deposits:", deposit_count)
# print("Withdrawals:", withdrawal_count)


# # 19.

# s = input("Enter sentence: ")

# has_digit = has_dot = has_at = False
# password_like = False
# repeated_special = False

# for i in range(len(s)):
#     ch = s[i]

#     if ch.isdigit():
#         has_digit = True
#     if ch == ".":
#         has_dot = True
#     if ch == "@":
#         has_at = True

#     if (ch.isupper() and i + 1 < len(s)
#             and s[i + 1].isdigit()):
#         password_like = True

#     if (not ch.isalnum() and ch != " "
#             and i + 1 < len(s) and s[i + 1] == ch):
#         repeated_special = True

# if password_like or repeated_special:
#     print("Suspicious")
# elif has_at or (has_dot and has_digit):
#     print("Review")
# else:
#     print("Safe")


# # 20.

# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         result = i * j

#         if result % 5 == 0:
#             print("F", end=" ")
#         elif result % 2 == 0:
#             print("E", end=" ")
#         else:
#             print("O", end=" ")
#     print()


# # 21. 

# total_discount = 0
# discount_counts = {20: 0, 15: 0, 10: 0, 0: 0}

# for i in range(10):
#     price = float(input("Enter price: "))

#     if price >= 5000:
#         rate = 20
#     elif price >= 3000:
#         rate = 15
#     elif price >= 1000:
#         rate = 10
#     else:
#         rate = 0

#     discount = price * rate / 100
#     final_price = price - discount

#     total_discount += discount
#     discount_counts[rate] += 1

#     print("Discount:", discount)
#     print("Final Price:", final_price)

# print("20% discount products:", discount_counts[20])
# print("15% discount products:", discount_counts[15])
# print("10% discount products:", discount_counts[10])
# print("No discount products:", discount_counts[0])
# print("Total Discount:", total_discount)


# # 22. String Compression Counter

# s = input("Enter string: ")

# if len(s) > 0:
#     count = 1

#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             print(s[i - 1] + str(count), end="")
#             count = 1

#     print(s[-1] + str(count))


# # 23. 

# total = 0
# junior = mid = senior = executive = 0

# for i in range(8):
#     salary = float(input("Enter salary: "))
#     total += salary

#     if salary < 25000:
#         junior += 1
#         print("Junior")
#     elif salary <= 50000:
#         mid += 1
#         print("Mid")
#     elif salary <= 100000:
#         senior += 1
#         print("Senior")
#     else:
#         executive += 1
#         print("Executive")

# print("Junior:", junior)
# print("Mid:", mid)
# print("Senior:", senior)
# print("Executive:", executive)
# print("Average Salary:", total / 8)


# # 24.

# sentence = input("Enter sentence: ")
# secret = input("Enter secret word: ")

# found = False
# occurrences = 0

# if len(secret) > 0:
#     for i in range(len(sentence) - len(secret) + 1):
#         match = True

#         for j in range(len(secret)):
#             if sentence[i + j] != secret[j]:
#                 match = False
#                 break

#         if match:
#             print("Starting position:", i)
#             occurrences += 1
#             found = True

# if found:
#     print("Occurrences:", occurrences)
# else:
#     print("Secret word not found")


# # 25. 

# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j % 15 == 0:
#             print("F", end=" ")
#         elif j % 3 == 0:
#             print("T", end=" ")
#         elif j % 2 == 0:
#             print("E", end=" ")
#         else:
#             print("O", end=" ")
#     print()


# # 26. 

# total = 0
# poor = average = good = excellent = outstanding = 0
# valid_count = 0

# for i in range(10):
#     rating = float(input("Enter rating: "))

#     if rating < 0 or rating > 10:
#         print("Invalid rating")
#         continue

#     total += rating
#     valid_count += 1

#     if rating <= 3:
#         poor += 1
#         print("Poor")
#     elif rating <= 5:
#         average += 1
#         print("Average")
#     elif rating <= 7:
#         good += 1
#         print("Good")
#     elif rating <= 9:
#         excellent += 1
#         print("Excellent")
#     else:
#         outstanding += 1
#         print("Outstanding")

# print("Poor:", poor)
# print("Average:", average)
# print("Good:", good)
# print("Excellent:", excellent)
# print("Outstanding:", outstanding)

# if valid_count > 0:
#     print("Average Rating:", total / valid_count)


# # 27. 

# sentence = input("Enter sentence: ")
# words = sentence.lower().split()

# for i in range(len(words)):
#     already_checked = False

#     for k in range(i):
#         if words[k] == words[i]:
#             already_checked = True
#             break

#     if already_checked:
#         continue

#     frequency = 0

#     for word in words:
#         if word == words[i]:
#             frequency += 1

#     if frequency > 1:
#         print(words[i], frequency)


# # 28.

# numbers = []
# highest_even = -1

# for i in range(10):
#     num = int(input("Enter integer: "))
#     text = str(abs(num))

#     even = odd = 0

#     for ch in text:
#         if int(ch) % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#     print("Even:", even, "Odd:", odd)

#     if even > highest_even:
#         highest_even = even
#         numbers = [num]
#     elif even == highest_even:
#         numbers.append(num)

# print("Numbers with maximum even digits:", numbers)


# # 29. 

# for i in range(5):
#     email = input("Enter email: ")

#     at_count = 0
#     at_position = -1
#     spaces = False

#     for j in range(len(email)):
#         if email[j] == "@":
#             at_count += 1
#             at_position = j
#         if email[j] == " ":
#             spaces = True

#     valid = True

#     if at_count != 1:
#         valid = False
#     elif spaces:
#         valid = False
#     elif at_position <= 0:
#         valid = False
#     elif at_position == len(email) - 1:
#         valid = False
#     else:
#         dot_found = False

#         for j in range(at_position + 1, len(email)):
#             if email[j] == "." and j > at_position + 1 and j < len(email) - 1:
#                 dot_found = True

#         if not dot_found:
#             valid = False

#     if valid:
#         print("Valid")
#     else:
#         print("Invalid")


# # 30.

# s = input("Enter string: ")

# same = different = both_vowels = both_digits = 0

# for i in range(len(s)):
#     for j in range(i + 1, len(s)):
#         if s[i] == s[j]:
#             same += 1
#         else:
#             different += 1

#         if s[i].lower() in "aeiou" and s[i].isalpha():
#             if s[j].lower() in "aeiou" and s[j].isalpha():
#                 both_vowels += 1

#         if s[i].isdigit() and s[j].isdigit():
#             both_digits += 1

# print("Same pairs:", same)
# print("Different pairs:", different)
# print("Both vowels:", both_vowels)
# print("Both digits:", both_digits)


# # 31. 

# passed = failed = 0
# highest = -1
# lowest = 101

# for i in range(5):
#     total = 0
#     all_pass = True

#     for j in range(5):
#         marks = float(input("Enter subject marks: "))

#         total += marks

#         if marks < 35 or marks > 100:
#             all_pass = False

#     percentage = total / 5
#     print("Total:", total)
#     print("Percentage:", percentage)

#     if all_pass:
#         passed += 1
#         if percentage >= 75:
#             grade = "A"
#         elif percentage >= 60:
#             grade = "B"
#         elif percentage >= 50:
#             grade = "C"
#         else:
#             grade = "D"
#     else:
#         failed += 1
#         grade = "Fail"

#     print("Grade:", grade)

#     if percentage > highest:
#         highest = percentage
#     if percentage < lowest:
#         lowest = percentage

# print("Passed:", passed)
# print("Failed:", failed)
# print("Highest Percentage:", highest)
# print("Lowest Percentage:", lowest)


# # 32.

# secret = input("Enter secret password: ")

# for i in range(5):
#     attempt = input("Enter attempted password: ")

#     matches = 0

#     for j in range(min(len(secret), len(attempt))):
#         if secret[j] == attempt[j]:
#             matches += 1

#     print("Matching positions:", matches)

#     if len(secret) == len(attempt) and matches == len(secret):
#         print("Correct")
#     else:
#         print("Incorrect")


# # 33.

# code = input("Enter product code: ")

# valid = True

# if len(code) != 8:
#     valid = False
# else:
#     for i in range(3):
#         if not ('A' <= code[i] <= 'Z'):
#             valid = False

#     for i in range(3, 8):
#         if not code[i].isdigit():
#             valid = False

# if valid:
#     print("Valid Product Code")
# else:
#     print("Invalid Product Code")


# # 34. 

# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     for num in range(1, i + 1):
#         if num == 2:
#             print("P", end=" ")
#         elif num < 2:
#             print("O", end=" ")
#         else:
#             prime = True

#             for j in range(2, num):
#                 if num % j == 0:
#                     prime = False
#                     break

#             if prime:
#                 print("P", end=" ")
#             elif num % 2 == 0:
#                 print("E", end=" ")
#             else:
#                 print("O", end=" ")
#     print()


# # 35.

# sentence = input("Enter sentence: ")
# words = sentence.split()

# longest = ""
# shortest = ""

# starts_vowel = ends_vowel = contains_digit = 0
# characters = 0

# if len(words) > 0:
#     longest = shortest = words[0]

# for word in words:
#     characters += len(word)

#     if len(word) > len(longest):
#         longest = word

#     if len(word) < len(shortest):
#         shortest = word

#     if word[0].lower() in "aeiou":
#         starts_vowel += 1

#     if word[-1].lower() in "aeiou":
#         ends_vowel += 1

#     for ch in word:
#         if ch.isdigit():
#             contains_digit += 1
#             break

# print("Words:", len(words))
# print("Characters:", characters)
# print("Longest:", longest)
# print("Shortest:", shortest)
# print("Starting with vowel:", starts_vowel)
# print("Ending with vowel:", ends_vowel)
# print("Words containing digits:", contains_digit)


# # 36.

# revenue = 0

# for i in range(5):
#     subtotal = 0

#     for j in range(3):
#         price = float(input("Enter item price: "))
#         subtotal += price

#     if subtotal >= 2000:
#         discount_rate = 15
#     elif subtotal >= 1000:
#         discount_rate = 10
#     else:
#         discount_rate = 0

#     discount = subtotal * discount_rate / 100
#     final_bill = subtotal - discount

#     member = input("Is customer a member? (yes/no): ").lower()

#     if member == "yes":
#         final_bill = final_bill * 0.95

#     revenue += final_bill

#     print("Subtotal:", subtotal)
#     print("Final Bill:", final_bill)

# print("Total Restaurant Revenue:", revenue)


# # 37. 

# word = input("Enter a word: ")

# for i in range(1, len(word) + 1):
#     for j in range(i):
#         print(word[j], end="")
#     print()

# print("Reverse Pattern:")

# for i in range(len(word), 0, -1):
#     for j in range(i):
#         print(word[j], end="")
#     print()


# # 38. 

# sentence = input("Enter sentence: ")
# words = sentence.lower().split()

# for i in range(len(words)):
#     checked = False

#     for k in range(i):
#         if words[k] == words[i]:
#             checked = True
#             break

#     if checked:
#         continue

#     frequency = 0

#     for word in words:
#         if word == words[i]:
#             frequency += 1

#     if frequency > 1:
#         if frequency == 2:
#             category = "Repeated"
#         elif frequency <= 4:
#             category = "Frequently Repeated"
#         else:
#             category = "Highly Repeated"

#         print(words[i], frequency, category)


# # 39.

# total_collection = 0

# for i in range(8):
#     age = int(input("Enter age: "))
#     distance = float(input("Enter distance: "))

#     if age < 0 or distance < 0:
#         print("Invalid details")
#         continue

#     fare = distance * 10

#     if age < 5:
#         fare = 0
#     elif age <= 12:
#         fare = fare * 0.50
#     elif age >= 60:
#         fare = fare * 0.70

#     print("Passenger Fare:", fare)
#     total_collection += fare

# print("Total Collection:", total_collection)


# # 40.

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")

# mirror = True

# if len(s1) != len(s2):
#     mirror = False
# else:
#     for i in range(len(s1)):
#         if s1[i] != s2[len(s2) - 1 - i]:
#             mirror = False
#             break

# if mirror:
#     print("Mirror Compatible")
# else:
#     print("Not Mirror Compatible")


# # 41.

# for i in range(7):
#     present = 0

#     for j in range(5):
#         status = input("Enter P or A: ").upper()

#         if status == "P":
#             present += 1

#     percentage = present / 5 * 100

#     print("Attendance:", percentage, "%")

#     if percentage >= 90:
#         print("Excellent")
#     elif percentage >= 75:
#         print("Good")
#     else:
#         print("Warning")


# # 42. 

# main_sum = secondary_sum = 0
# main_even = secondary_odd = 0

# for i in range(4):
#     for j in range(4):
#         num = int(input("Enter matrix value: "))

#         if i == j:
#             main_sum += num

#             if num % 2 == 0:
#                 main_even += 1

#         if i + j == 3:
#             secondary_sum += num

#             if num % 2 != 0:
#                 secondary_odd += 1

# print("Main Diagonal Sum:", main_sum)
# print("Secondary Diagonal Sum:", secondary_sum)
# print("Main Diagonal Even:", main_even)
# print("Secondary Diagonal Odd:", secondary_odd)

# if main_sum > secondary_sum:
#     print("Main diagonal is greater")
# elif secondary_sum > main_sum:
#     print("Secondary diagonal is greater")
# else:
#     print("Both are equal")


# # 43. 

# word = input("Enter text: ")

# result = ""

# for ch in word:
#     if ch.lower() in "aeiou" and ch.isalpha():
#         result += "@"
#     elif ch.isalpha():
#         result += ch.lower()
#     elif ch.isdigit():
#         result += "#"
#     elif ch == " ":
#         result += "_"
#     else:
#         result += "!"

# print("Transformed Password:", result)


# # 44. 

# balance = float(input("Enter starting balance: "))

# deposits = withdrawals = 0

# n = int(input("Enter number of transactions: "))

# for i in range(n):
#     transaction = input("Enter D or W: ").upper()
#     amount = float(input("Enter amount: "))

#     if amount <= 0:
#         print("Invalid amount")
#         continue

#     if transaction == "D":
#         balance += amount
#         deposits += amount
#     elif transaction == "W":
#         balance -= amount
#         withdrawals += amount
#     else:
#         print("Invalid transaction")
#         continue

#     if balance < 0:
#         print("Overdraft")
#     elif balance < 500:
#         print("Low Balance")
#     else:
#         print("Normal")

# print("Total Deposits:", deposits)
# print("Total Withdrawals:", withdrawals)
# print("Final Balance:", balance)


# # 45.

# word1 = input("Enter first word: ")
# word2 = input("Enter second word: ")

# limit = min(len(word1), len(word2))

# for i in range(limit):
#     if word1[i] == word2[i]:
#         print("S", end="")
#     else:
#         print("D", end="")

# print()

# if len(word1) > limit:
#     print("Extra characters in first word:", word1[limit:])

# if len(word2) > limit:
#     print("Extra characters in second word:", word2[limit:])


# # 46.

# n = int(input("Enter n: "))

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end="")
#         elif (i + j) % 2 == 0:
#             print("E", end="")
#         else:
#             print("O", end="")
#     print()


# # 47.

# out = critical = low = available = 0
# highest_quantity = -1
# highest_product = ""

# for i in range(8):
#     name = input("Enter product name: ")
#     quantity = int(input("Enter quantity: "))

#     if quantity < 0:
#         print("Invalid quantity")
#         continue
#     elif quantity == 0:
#         out += 1
#         print("Out of Stock")
#     elif quantity <= 5:
#         critical += 1
#         print("Critical")
#     elif quantity <= 20:
#         low += 1
#         print("Low")
#     else:
#         available += 1
#         print("Available")

#     if quantity > highest_quantity:
#         highest_quantity = quantity
#         highest_product = name

# print("Out of Stock:", out)
# print("Critical:", critical)
# print("Low:", low)
# print("Available:", available)
# print("Highest Quantity Product:", highest_product)


# # 48.

# for i in range(10):
#     username = input("Enter username: ")

#     letters = digits = underscores = 0
#     invalid = False

#     for ch in username:
#         if ch.isalpha():
#             letters += 1
#         elif ch.isdigit():
#             digits += 1
#         elif ch == "_":
#             underscores += 1
#         else:
#             invalid = True

#     if (invalid or " " in username or len(username) < 3
#             or len(username) > 20):
#         print("Invalid")
#     elif underscores > 2 or digits > 5:
#         print("Acceptable")
#     else:
#         print("Clean")


# # 49.

# sentences = []

# for i in range(10):
#     sentence = input("Enter sentence: ")
#     sentences.append(sentence)

# search_word = input("Enter search word: ").lower()

# total_occurrences = 0

# for i in range(10):
#     words = sentences[i].lower().split()
#     occurrences = 0

#     for word in words:
#         cleaned = word.strip(".,!?;:\"'()[]{}")

#         if cleaned == search_word:
#             occurrences += 1

#     if occurrences > 0:
#         print("Sentence", i + 1, "Occurrences:", occurrences)

#     total_occurrences += occurrences

# print("Total Occurrences:", total_occurrences)


# # 50. Complete Data Analyzer Challenge

# inputs = []

# total_vowels = 0
# total_consonants = 0
# total_digits = 0
# total_special = 0

# highest_score = -1
# highest_vowel_count = -1
# highest_digit_count = -1

# highest_score_input = ""
# highest_vowel_input = ""
# highest_digit_input = ""

# for i in range(10):
#     s = input("Enter input: ")
#     inputs.append(s)

#     upper = lower = vowels = consonants = 0
#     digits = spaces = special = 0
#     score = 0

#     longest_word = ""
#     words = s.split()

#     for word in words:
#         if len(word) > len(longest_word):
#             longest_word = word

#     for ch in s:
#         if ch.isupper():
#             upper += 1
#         elif ch.islower():
#             lower += 1

#         if ch.lower() in "aeiou" and ch.isalpha():
#             vowels += 1
#             score += 2
#         elif ch.isalpha():
#             consonants += 1
#             score += 1
#         elif ch.isdigit():
#             digits += 1
#             score += 3
#         elif ch == " ":
#             spaces += 1
#         else:
#             special += 1
#             score += 4

#     repeated = 0

#     for j in range(len(s)):
#         for k in range(j + 1, len(s)):
#             if s[j] == s[k]:
#                 repeated += 1
#                 break

#     print("\nInput:", s)
#     print("Uppercase:", upper)
#     print("Lowercase:", lower)
#     print("Vowels:", vowels)
#     print("Consonants:", consonants)
#     print("Digits:", digits)
#     print("Spaces:", spaces)
#     print("Special:", special)
#     print("Longest Word:", longest_word)
#     print("Repeated Characters:", repeated)
#     print("Score:", score)

#     total_vowels += vowels
#     total_consonants += consonants
#     total_digits += digits
#     total_special += special

#     if score > highest_score:
#         highest_score = score
#         highest_score_input = s

#     if vowels > highest_vowel_count:
#         highest_vowel_count = vowels
#         highest_vowel_input = s

#     if digits > highest_digit_count:
#         highest_digit_count = digits
#         highest_digit_input = s


# print("\n========== FINAL REPORT ==========")

# print("Highest Score Input:", highest_score_input)
# print("Most Vowels Input:", highest_vowel_input)
# print("Most Digits Input:", highest_digit_input)

# print("Total Vowels:", total_vowels)
# print("Total Consonants:", total_consonants)
# print("Total Digits:", total_digits)
# print("Total Special Characters:", total_special)

# if (total_consonants + total_vowels) > (total_digits + total_special):
#     print("Text Heavy")
# elif total_digits > total_vowels + total_consonants + total_special:
#     print("Number Heavy")
# elif total_special > total_vowels + total_consonants + total_digits:
#     print("Special Character Heavy")
# else:
#     print("Balanced")
