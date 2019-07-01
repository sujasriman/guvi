n=int(input())
s=0
i=0
l=[]
while(n>0):
    rem=n%10
    s=s+(rem*(2**i))
    i+=1
    n=n//10
while(s>0):
    rem=s%8
    l.append(rem)
    s=s//8
for i in range(len(l)-1,0,-1):
    print(l[i],end='')
print(l[0])
