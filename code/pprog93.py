n=int(input())
temp=0
l1=[]
l=list(map(int,input().split()))
if(n%2!=0):
    b=n-1
else:
    b=n
for i in range(0,b,2):
    temp=l[i]
    l[i]=l[i+1]
    l[i+1]=temp
for i in range(len(l)-1):
    print(l[i],end=' ')
print(l[len(l)-1])
