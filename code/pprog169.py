s=input()
l=[]
l1=[]
count=1
for i in range(len(s)):
    l.append(s[i])
l.append(0)
for i in range(len(l)-1):
    if(l[i]==l[i+1]):
        count+=1
    else:
        l1.append(l[i])
        l1.append(str(count))
        count=1
print(''.join(l1))
