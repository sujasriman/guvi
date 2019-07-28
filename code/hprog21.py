n,m=input().split()
n=int(n)
m=int(m)
l=[]
count=0
for i in range(n):
    l.append(input().split())
for i in range(n):
    for j in range(m):
        l[i][j]=int(l[i][j])
for i in range(n):
    if(0 in l[i]):
        a=l[i].index(0)
        l[i][a]=-1
        count+=1
        for j in range(m):
            l[i][j]=0
if(count>0):
    for k in range(n):
        l[k][a]=0
for i in range(n):
    for j in range(m-1):
        print(l[i][j],end=' ')
    print(l[i][m-1])
