n,m=input().split()
n=int(n)
m=int(m)
l=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
for i in range(n):
    l1.append(l[i])
for i in range(n,n+m):
    l2.append(l[i])
for i in range(len(l1)):
    if(l1[i] in l2):
        l3.append(l1[i])
        l2.remove(l1[i])
if(len(l3)==1):
    print(l3[0])
else:
    for i in range(len(l3)-1):
        print(l3[i],end=' ')
    print(l3[len(l3)-1])
