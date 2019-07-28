n,k=input().split()
n=int(n)
k=int(k)
l=[]
l1=[]
count=0
rem=0
while(n>0):
    rem=n%10
    l.append(rem)
    n=n//10
l.reverse()
l.append(10)
if(k==0):
    l.remove(l[len(l)-1])
    l1=l
else:
    for i in range(len(l)-1):
        if(l[i]<l[i+1]):
            l1.append(l[i])
            count+=1
        if(count==len(l)-k):
            break
for i in range(len(l1)-1):
    print(l1[i],end='')
print(l1[len(l1)-1])
