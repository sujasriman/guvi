n,k=input().split()
n=int(n)
k=int(k)
l=list(map(int,input().split()))
l1=[]
if(k in l):
  print(k)
else:
  for i in range(len(l)):
    if(l[i]<k):
      l1.append(l[i])
  print(l1[len(l1)-1])
