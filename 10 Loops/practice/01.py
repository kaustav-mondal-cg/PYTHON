#ChatGPT

#1

# for i in range (1,5):
#     for j in range (1, i+1):
#         print("*", end=" ")
#     print()

#2

# for i in range(1,6): # use 1,5 to prevent extra line
#     for j in range(1,6-i):
#         print("*", end=" ")
#     print()    

#3

# for i in range(1,5):
#     for j in range(1,6-i):
#         print(" ", end=" ")
#     for k in range(1,i+1):
#         print("*  ",end=" ")
#     print()        

# #Better
# for i in range(1,5):
#     print(" " * (5 - i), end="")
#     for k in range(1,i+1):
#         print("* ", end="")
#     print()

#4

# for i in range(1,5):
#     for j in range(i-1):
#         print(" ", end="")
#     for k in range(1,6-i):
#         print("*",end=" ")
#     print()    

#5

for i in range(1,5):
    print(" " * (4 - i), end="")
    for k in range(1,i+1):
        print("* ", end="")
    print()
for i in range(1,4):
    for j in range(i-1):
        print(" ", end="")
    for k in range(1,5-i):
        print(" *",end="")
    print()    