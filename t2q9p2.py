import random
while True:
    number=int(input("enter the number which you want to guess with lucky number"))
    i=random.randint(0,10)
    if i==number:
        break
    else:
        answer=str(input("enter no if you want to stop guessing"))
    if answer=="no":
        break
    continue
        
    