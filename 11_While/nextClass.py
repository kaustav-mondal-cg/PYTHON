

# while jab i<j karunga
# tab if laga k str1[i]==rstr[j] kare 
# tab wo first or last ka index check karega or while loop repeat nahi karega
# so by this we can run our code faster than usual

string = input("Enter your word: ").strip().lower()
i = 0
j = len(string)-1
Flag = True
while i<j and Flag == True:
    if string[i] == string[j]:
      i = i+1
      j = j-1
    else:
        Flag=False
         
if Paranthesis:   
    print("Palindrome")
else:
    print("Not Palindrome")   
    



#palindrome by while 
# w=input("Enter your word:").lower()
# i=len(w)-1
# reverse=""
# while i>=0:
#     reverse+=w[i]
#     i-=1
# if w==reverse:
#     print("palindrome")
# else:
#     print("Not Plaindrome")


