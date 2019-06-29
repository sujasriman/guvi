s=input()
l=[]
for i in range(len(s)):
    if(not(s[i].isspace())):
        l.append(s[i])
print(''.join(l))
