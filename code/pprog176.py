s1,s2=input().split()
l1=[]
l2=[]
for i in range(len(s1)):
    l1.append(s1[i])
for i in range(len(s2)):
    l2.append(s2[i])
l1=list(set(l1))
l2=list(set(l2))
l1.sort()
l2.sort()
if(l1==l2):
    print('true')
else:
    print('false')
