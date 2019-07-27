s1='dhoni'
s2=input()
count=0
l=[]
for i in range(len(s1)):
    l.append(s1[i])
if(len(s2)==len(s1)):
    for i in range(len(s2)):
        if(s2[i] in l):
            count+=1
            l.remove(s2[i])
    if(count==len(s1)):
        print("yes")
    else:
        print("no")
else:
    print("no")
