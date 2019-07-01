n=int(input())
l=[]
while(n>0):
    rem=n%10
    l.append(rem)
    n=n//10
l.reverse()
print(l[0]+l[len(l)-1])
