s=input()
c=input()
l=[]
l1=[]
l2=[]
l3=[]
for i in range(len(s)):
    l.append(s[i])
for i in range(len(c)):
    l3.append(c[i])
for i in range(l.index('|')):
    l1.append(l[i])
for i in range(l.index('|')+1,len(l)):
    l2.append(l[i])
for i in range(len(l3)):
    l2.append(l3[i])
if(len(l1)==len(l2)):
    l1=''.join(l1)
    l2=''.join(l2)
    print(l1+'|'+l2)
else:
    print("Impossible")
