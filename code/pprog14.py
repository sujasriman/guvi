n=int(input())
s=input()
l=[]
for i in range(n):
    if((s[i]!='a')and(s[i]!='e')and(s[i]!='i')and(s[i]!='o')and(s[i]!='u')and(s[i]!='A')and(s[i]!='E')and(s[i]!='I')and(s[i]!='O')and(s[i]!='U')):
        l.append(s[i])
for i in range(len(l)-1,0,-1):
    print(l[i],end='')
print(l[0])
