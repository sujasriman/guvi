num=int(input())
l=list(map(int,input().split()))
s=0
for i in range(num):
    if(l[i]<0):
        s=s+l[i]
print(s)
