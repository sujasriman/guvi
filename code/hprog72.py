l=list(input().split())
l1=[]
for i in range(len(l)):
    a=''
    if(i%2==0):
        if('.' in l[i]):
            n=len(l[i])-2
        else:
            n=len(l[i])-1
        for j in range(n,-1,-1):
            a=a+l[i][j]
        l1.append(a)
    else:
        l1.append(l[i])
for i in range(len(l1)-1):
    print(l1[i],end=' ')
print(l1[len(l1)-1])
