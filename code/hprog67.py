l1=list(input().split('#'))
l2=list(input().split('#'))
s1=0
s2=0
for i in range(1,len(l1)):
    l1[i]=int(l1[i])
    l2[i]=int(l2[i])
    s1=s1+l1[i]
    s2=s2+l2[i]
if(s1>s2):
    print(l1[0])
else:
    print(l2[0])
