x=input("enter the string in which you want to calculate letters and didgits")
l=0
d=0
for i in x:
    if i.isdigit():
        d+=1
    if i.isalpha():
        l+=1
print("letters:",l)
print("digits:",d)