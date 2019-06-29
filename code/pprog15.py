s=input()
l=[]
for i in range(len(s)):
    b=s.count(s[i])
    l.append(b)
a=l.index(max(l))
print(s[a])
