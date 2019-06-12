string=list(map(int,input()))
count=0
for i in range(len(string)):
    if(string[i]==0 or string[i]==1):
        count+=1
if(count==len(string)):
    print("yes")
else:
    print("no")
