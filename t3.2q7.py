input_user=input("enter the string you want to reverse\n")
rev=input_user[::-1]
vowel=['a','e','i','o','u']
z=[]

for i in vowel:
    if i in rev:
        z.append(i)

print("".join(z))        