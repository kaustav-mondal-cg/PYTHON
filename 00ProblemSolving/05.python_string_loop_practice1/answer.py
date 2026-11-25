# # Q1. Find the substring 420

# N = input()

# if "420" in N:
#     print("Caught")
# else:
#     print("Escaped")


# # Q2. Decompress the string


# S = input()
# result = ""

# for i in range(0, len(S), 2):
#     letter = S[i]
#     count = int(S[i + 1])

#     for j in range(count):
#         result += letter

# print(result)


# # Q3. Check whether both halves are palindromes

# N = int(input())
# S = input()

# mid = N // 2

# first = S[:mid]
# second = S[mid:]

# first_palindrome = True
# second_palindrome = True

# # Check first half
# for i in range(len(first) // 2):
#     if first[i] != first[len(first) - 1 - i]:
#         first_palindrome = False
#         break

# # Check second half
# for i in range(len(second) // 2):
#     if second[i] != second[len(second) - 1 - i]:
#         second_palindrome = False
#         break

# if first_palindrome and second_palindrome:
#     print("yes")
# else:
#     print("no")


# # Q4. Count a character in a string


# S = input()
# C = input()

# count = 0

# for ch in S:
#     if ch == C:
#         count += 1

# print(count)


# # Q5. Reverse a string using a loop


# S = input()
# reversed_string = ""

# for i in range(len(S) - 1, -1, -1):
#     reversed_string += S[i]

# print(reversed_string)


# # Q6. Check whether the complete string is a palindrome


# S = input()

# left = 0
# right = len(S) - 1
# is_palindrome = True

# while left < right:
#     if S[left] != S[right]:
#         is_palindrome = False
#         break

#     left += 1
#     right -= 1

# if is_palindrome:
#     print("yes")
# else:
#     print("no")


# # Q7. Count vowels in a string


# S = input()

# count = 0

# for ch in S:
#     if ch in "aeiou":
#         count += 1

# print(count)


# # Q8. Count digits in a string


# S = input()

# count = 0

# for ch in S:
#     if ch >= "0" and ch <= "9":
#         count += 1

# print(count)


# # Q9. Find the first position of a character


# S = input()
# C = input()

# position = -1

# for i in range(len(S)):
#     if S[i] == C:
#         position = i
#         break

# print(position)


# # Q10. Remove all occurrences of a character


# a = input()
# b = input()

# result = ""

# for ch in a:
#     if ch != b:
#         result += ch

# print(result)
