s=input()
l1=[]
for i in range(len(s)-1,-1,-1):
    l1.append(s[i])
if(len(l1)==1):
    print(l1[0])
else:
    for i in range(len(l1)-1):
        print(l1[i],end='-')
    print(l1[len(l1)-1])
