s=input()
l=[]
for i in range(len(s)-1,-1,-1):
    l.append(s[i])
if(len(l)==1):
    print(l[0])
else:
    for i in range(len(l)-1):
        print(l[i],end='-')
    print(l[len(l)-1])
