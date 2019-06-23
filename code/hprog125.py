s=input()
l=[]
for i in range(len(s)):
    if(s.count(s[i])==1):
        l.append(s[i])
print(''.join(l))
