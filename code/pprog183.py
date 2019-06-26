n=int(input())
num=[]
z=[]
l=list(map(int,input().split()))
for i in range(len(l)):
    if(l[i]==0):
        z.append(l[i])
    else:
        num.append(l[i])
num=num+z
for i in range(len(num)-1):
    print(num[i],end=' ')
print(num[len(l)-1])
