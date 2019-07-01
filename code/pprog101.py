n=int(input())
s=0
l=list(map(int,input().split()))
for i in range(1,n):
   s=s+l[i]
print(s)
