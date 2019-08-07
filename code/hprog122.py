n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(n):
    s1=0
    s2=0
    for j in range(0,i):
        s1=s1+l[j]
    for k in range(i+1,n):
        s2=s2+l[k]
    if(s1==s2):
        count+=1
        break
if(count>0):
    print('yes')
else:
    print('no')
