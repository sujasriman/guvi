n=int(input())
l=[]
a=1
b=1
for i in range(n):
    l.append(input().split())
for i in range(n):
    l[i][i]=int(l[i][i])
    a*=l[i][i]
for i in range(n):
    l[i][n-1-i]=int(l[i][n-1-i])
    b*=l[i][n-1-i]
print(a+b)
