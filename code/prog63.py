l=list(map(int,input().split()))
a=0
for i in range(len(l)-1):
    if(l[i]<=l[i+1]):
        a=l[i]
    else:
        a=l[i+1]
print(a)
