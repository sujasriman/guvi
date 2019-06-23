n=int(input())
a=[]
b=0
for i in range(n):
    a.append(input().split())
for i in range(n):
    j=i
    a[i][j]=int(a[i][j])
    b=b+a[i][j]
print(b)
