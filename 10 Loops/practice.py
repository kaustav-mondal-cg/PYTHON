#Find if the word is palindrome or not

Name=input("Enter your word: ").strip().upper()
length=len(Name)
sum=""
for number in range(length-1,-1,-1):
    sum=sum+Name[number]

if Name==sum:
    print(f"The word {Name} is Palindrome")
else:
    print(f"The word {Name} is not Palindrome")



#Find all the prime numbers from 1 to 100

N=int(input("Enter any number: "))
if N == 1:
    print("1 is neither prime nor composite number")
else:
    prime = True 

    for i in range(2,N):
        if N%i==0:
            prime = False

    if prime : 
        print(f"{N} is a prime number.")       
    else:
        print(f"{N} is a composite number.")            


