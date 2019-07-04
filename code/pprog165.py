n,k=input().split()
n=int(n)
k=int(k)
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
  if(l[i]>k):
    l1.append(l[i])
print(l1[0])
