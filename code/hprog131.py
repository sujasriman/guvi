import math
n=int(input())
l=list(map(int,input().split()))
l.sort()
a=[]
a1=[]
for i in range(n):
    if(i<math.ceil(n/2)):
        a.append(l[i])
    else:
        a1.append(l[i])
a1.reverse()
if(n%2!=0):
    for i in range(len(a)-1):
        print(a1[i],a[i],end=' ')
    print(a[len(a)-1])
else:
    for i in range(len(a)-1):
        print(a1[i],a[i],end=' ')
    print(a1[len(a)-1],a[len(a)-1])
