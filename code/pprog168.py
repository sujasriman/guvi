s=input()
l=[]
l1=[]
for i in range(len(s)):
    l.append(s[i])
for i in range(0,len(l),2):
    for j in range(int(l[i+1])):
        l1.append(l[i])
print(''.join(l1))
