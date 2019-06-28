n,k=input().split()
n=int(n)
k=int(k)
l=[]
count=0
for i in range(n):
    st=input()
    l.append(st)
l.append(' ')
for i in range(len(l)-1):
    if(l[i]==l[i+1]):
        count+=1
if(count==k-1):
    print("yes")
else:
    print("no")
