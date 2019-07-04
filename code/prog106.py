n,k=input().split()
n=int(n)
k=int(k)
l1=[]
l=list(map(int,input().split()))
for i in range(n):
  if(i%2!=0):
    l1.append(i)
print(l1[k-1])
