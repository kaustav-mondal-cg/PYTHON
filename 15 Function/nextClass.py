# def info(a,age,name="Ram",):
#     print(name,a)
#     return
#     print(age)
# info(name="Sharma",age=20,a=30) #Keyword arguments


# def info(a,age,name="Ram",):
#     print(name,a)
#     return 4
#     print(age)
# print(info(name="Sharma",age=20,a=30)) #None ai ga

# def info(a,age,name="Ram",):
#     print(a)
#     return 5
# a=info(name="Sharma",age=20,a=30)
# print(a)
# print(info(name="Sharma",age=20,a=30))



def info(a,b,c,*args):
    print(a,b)
    print(args)
info(1,2,3,4,5,6,7)