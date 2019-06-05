a=int(input())
fact=1
if(a>0):
    for i in range(1,a+1):
        fact=fact*i
    print(fact)
elif(a==0):
    fact=1
    print(fact)
else:
    print("invalid")
