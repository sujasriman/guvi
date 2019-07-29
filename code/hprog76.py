n=int(input())
l=[]
s=0
for i in range(n):
    l.append(input().split())
for i in range(n):
    for j in range(n):
        l[i][j]=int(l[i][j])
        s=s+l[i][j]
s/=(n*n)
print("%.6f" % s)
