n=int(input())
l=[]
while(n>0):
    rem=n%2
    l.append(rem)
    n=n//2
for i in range(len(l)-1,0,-1):
    print(l[i],end='')
print(l[0])
