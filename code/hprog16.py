n,k=input().split()
n=int(n)
k=int(k)
l=list(map(int,input().split()))
l.remove(k)
l1=[]
l2=[]
a=0
b=0
for i in range(n-1):
    l1.append(abs(k-l[i]))
for i in range(len(l1)):
    a=min(l1)
    b=l[l1.index(a)]
    l2.append(b)
    l1.remove(a)
    l.remove(b)
    if(len(l2)==3):
        break
for i in range(len(l2)-1):
    print(l2[i],end=' ')
print(l2[len(l2)-1])
