s=input()
l=[]
for i in range(len(s)):
    if(s[i] not in l):
        l.append(s[i])
for i in range(len(l)-1):
    print(l[i],end='')
print(l[len(l)-1])
