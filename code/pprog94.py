n=int(input())
l=[]
count=0
while(n>0):
    rem=n%10
    l.append(rem)
    n=n//10
for i in range(len(l)):
    if(l.count(l[i])>1):
        count+=1
        break
if(count==1):
    print("yes")
else:
    print("no")
