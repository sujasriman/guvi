s=input()
l=[]
for i in range(len(s)):
    l.append(s[i])
l=list(set(l))
l.sort()
for i in range(len(l)-1):
    print(l[i],end='')
print(l[len(l)-1])
