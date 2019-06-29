n,k=input().split()
n=int(n)
k=int(k)
l=[]
for i in range(1,max(n,k)+1):
    if(n%i==0 and k%i==0):
        l.append(i)
print(max(l))
