n,k=input().split()
n=int(n)
k=int(k)
count=0
l=[]
while(n>0):
    rem=n%10
    l.append(rem)
    n=n//10
l.reverse()
for i in range(k+1):
    if(i in l):
        count+=1
if(count==k+1):
    print("yes")
else:
    print("no")
