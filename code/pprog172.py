n=int(input())
l=[]
while(n>0):
    rem=n%10
    l.append(rem)
    n=n//10
l.sort(reverse=True)
for i in range(len(l)-1):
    print(l[i],end='')
print(l[len(l)-1])
