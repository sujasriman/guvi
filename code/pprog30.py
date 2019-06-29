s1,s2,k=input().split()
k=int(k)
count=0
for i in range(len(s1)):
    if(s1[i]!=s2[i]):
        count+=1
if(count==k):
    print("yes")
else:
    print("no")
