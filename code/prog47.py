n=int(input())
l=list(map(int,input().split()))
b=l[0]
for i in range(n):
    for j in range(i+1,n):
        if(b<l[j]):
            b=l[j]
c=l[0]
for i in range(n):
    for j in range(i+1,n):
        if(c>l[j]):
            c=l[j]
print(c,b)
