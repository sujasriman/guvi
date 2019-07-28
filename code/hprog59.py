n=int(input())
l=[]
l1=[]
for i in range(2):
    l.append(input().split())
for i in range(n):
    a=0
    l1.append(int(l[a][i])+int(l[a+1][i]))
for i in range(n-1):
    print(l1[i],end=' ')
print(l1[n-1])
