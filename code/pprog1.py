s=input()
l=[]
for i in range(len(s)):
    l.append(s[i])
for i in range(len(l)-1,0,-1):
    print(l[i],end='')
print(l[0])
