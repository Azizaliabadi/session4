import random

while True:
    karbar=input("c continue va e exit")
    if karbar=="k":
        break
    else:
        n= int(input("enter random number:"))
        list= []

        while True:
            adad=random.randint(0,20)
            if adad in list:
                 continue
            else:
                 if len(list) == n:
                    break
                 else:
                    list.append(adad)
            print(list)
