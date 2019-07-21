s1,s2=input().split()
c=0
for i in range(len(s1)):
    s=''
    s=s1[i]
    for j in range(i+1,len(s1)):
        s=s+s1[j]
        if(s in s2):
            c+=1
            break
if(c!=0):
    print("yes")
else:
    print("no")
