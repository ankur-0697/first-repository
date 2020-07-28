print("hello welcome to calculator")
a=int(input('''
               enter 1 if you want to add two numbers
               enter 2 if you want to subtract two numbers
               enter 3 if you want to divide two numbers
               enter 4 if you want to Multiply two numbers
               enter 5 if you want to take average of two numbers'''))
first=int(input("enter first number"))
second=int(input("enter second number"))
if a==1:
    res=int(first+second)
    if res<0:
        print("zsa")
    else:
        print("The addition of two numbers is:",res)
if a==2:
    res=(first-second)
    if res<0:
        print("zsa")
    else:    
        print("The substraction of two numbers is:",res)
if a==3:
    res=float(first/second)
    if res<0:
        print("zsa")
    else:
        print("Result after dividing these two numbers is:",res)
if a==4:
    res=int(first*second)
    if res<0:
        print("zsa")
    else:
        print("The multiplication of two numbers is:",res)
if a==5:
    
    first1=int(input("enter third number"))
    second1=int(input("enter fourth number"))
    res=(first+second+first1+second1)/4
    if res<0:
        print("zsa")
    else:    
        print("the average of these numbers is:",res)   

