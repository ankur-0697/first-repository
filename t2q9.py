import random
while True:
    lucky=int(input("enter the number which you want to guess with lucky number"))
    i=random.randint(0,10)
    if i==lucky:
        break
    else:
        continue
    