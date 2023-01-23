import random
n= int(input("enter random number:"))
list=[]
for i in range (n):
    i+=1
    r=(random.randint(0,20))
    list.append(r)
print(list)
