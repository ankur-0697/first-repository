x=int(input("enter number of elements you want to add in list and tupple"))
y=[]
counter=1
for i in range(x):
    z=int(input("enter the "+str(counter)+" elemet:"))
    y.append(""+str(z)+"")
    counter+=1
print(y)
print(tuple(y))
