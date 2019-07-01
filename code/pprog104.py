n=int(input())
s=0
l=list(map(int,input().split()))
for i in range(n-1):
    s=s+l[i]+l[i+1]
print(s)
