n,q=input().split()
n=int(n)
q=int(q)
l=list(map(int,input().split()))
m=[]
for i in range(1,q+1):
    a,b=input().split()
    a=int(a)
    b=int(b)
    s=0
    for j in range(a,b+1):
        s=s+l[j-1]
    m.append(s)
for i in range(0,len(m)):
    print(m[i])
