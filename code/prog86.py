string=input()
l=len(string)
count=0
for i in range(l):
    j=i+1
    for j in range(j,l):
        if(string[i]==string[j]):
            count+=1
if(count==0):
    print("Yes")
else:
    print("No")
