n,k=input().split()
n=int(n)
k=int(k)
b=n//2
count=0
for i in range(1,b):
    a=pow(k,i)
    if(a==n):
        count+=1
        break
if(count==1):
    print("yes")
else:
    print("no")
