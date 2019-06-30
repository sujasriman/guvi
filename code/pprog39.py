n=int(input())
n=n//2
count=0
for i in range(1,n):
    a=pow(2,i)
    if(a==n):
        count+=1
        break
if(count==1):
    print("yes")
else:
    print("no")
