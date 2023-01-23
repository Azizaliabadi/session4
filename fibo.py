n=int(input("enter a number"))
sum1=1 ; sum2=1 ; sum3=0
print(n, 'tedade anasor:')
print(sum1)
while n-1>0:
    print(sum1)
    sum3=sum2; sum2=sum1; sum1=sum2+sum3
    n=n-1
