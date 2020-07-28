counter=1
while counter<=5:
    print("type in the",counter,"number")
    counter=counter+1        
    import random
    i=random.randint(0,10)
    num=int(input("enter the lucky number"))
    if i==num:
        print("good guess")
        break
        counter=counter+1
    else:
        print("try again")
if i!=num:
    print("sorry but that was not very successful")

    