n=int(input())
l=list(map(int,input().split()))
for i in range(n-1):
    if(l[i]>l[i+1]):
        l[i]=l[i+1]
    else:
        l[i]=-1
l[n-1]=-1
for i in range(n-1):
    print(l[i],end=' ')
print(l[n-1])
