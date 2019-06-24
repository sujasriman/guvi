n=int(input())
a=1
b=[]
b.append(a)
b.append(a)
for i in range(1,n-1):
    a=b[i-1]+b[i]
    b.append(a)
for i in range(n-1):
    print(b[i],end=' ')
print(b[len(b)-1])
