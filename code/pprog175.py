s1=input()
s2=input()
s1+=s2
l=[]
for i in range(len(s1)):
    l.append(s1[i])
l=list(set(l))
if(len(l)==26):
    
    print('complementary')
else:
    print('non-complementary')
