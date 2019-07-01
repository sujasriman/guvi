s=input()
l=list(s.split())
l1=[]
for i in range(len(l)):
    b=len(l[i])
    l1.append(b)
print(l[l1.index(max(l1))])
