Enter = int(input("""What do you want to do?
                  1.Even numbers
                  2.Odd numbers
                  3.Prime numbers
                  4.Armstrong numbers
                  :  """))
num = int(input("Enter a number : "))
match Enter:
    case 1:
        if num%2==0:
            print("Even number")
        else:
            print("Not a even number")
    case 2:
        if num%2!=0:
            print("Odd number")
        else:
            print("Not a odd number")
    case 3:
        if num>1:
            for i in range(2,num):
                if (num%i)==0:
                    print("Not a prime number")
                    break
            else:
                print("Prime number")
    case 4:
        number=num
        sum=0
        while num>0:
            digit=num%10
            sum+=digit**3
            num//=10
        if sum==number:
            print("Armstrong number")
        else:
            print("Not a armstrong number")
    case _:
        print("Invalid input")