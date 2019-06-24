import math
n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    s=s+l[i]
s=s/n
print(math.floor(s))
