s1,s2=input().split()
count=0
for i in range(min(len(s1),len(s2))):
    if(s1[i]==s2[i]):
        count+=1
        break
if(count==1):
    print("yes")
else:
    print("no")
