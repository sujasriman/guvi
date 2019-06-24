l=list(map(int,input().split()))
b=l[0]
for i in range(10):
    for j in range(i+1,10):
        if(b<l[j]):
            b=l[j]
print(b)
