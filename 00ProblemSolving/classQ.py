#1

# for i in range(4):
#     for j in range(1,2):
#         print("*       *",end="")
#     print()    
# for k in range(5):
#     print("*",end=" ")

#DIFFERENT APPROCH

n = int(input("Number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==n or i==n:
            print("* ",end="")
        elif n%2==0 and j==(n)/2 and i==(n)/2:
               print(" *",end="")    
        elif n%2!=0 and j==(n+1)/2 and i==(n+1)/2:
               print("* ",end="")      
        else:
            print("  ",end="") 
    print()               

        