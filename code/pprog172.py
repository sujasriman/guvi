n=int(input())
l=[]
l1=[]
while(n>0):
    rem=n%10
    l.append(rem)
    n=n//10
l.sort(reverse=True)
for i in range(len(l)):
    l1.append(l[i])
for i in range(len(l1)-1):
    print(l1[i],end='')
print(l1[len(l)-1])
