n,q=input().split()
n=int(n)
q=int(q)
l=list(map(int,input().split()))
m1=[]
for i in range(1,q+1):
    a,b=input().split()
    a=int(a)
    b=int(b)
    m=[]
    for j in range(a,b+1):
        m.append(l[j-1])
    m1.append(min(m))
for i in range(0,len(m1)):
    print(m1[i])
