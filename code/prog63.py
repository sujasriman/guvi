l=list(map(int,input().split()))
a=l[0]
for i in range(1,len(l)):
    if(a>l[i]):
        a=l[i]
print(a)
