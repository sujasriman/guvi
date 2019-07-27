n=int(input())
l=list(map(int,input().split()))
count=0
l1=[]
for i in range(n-1):
    if((l[i]!=l[i+1])or(l[i]==l[i+1])):
        l1.append(l[i])
    if(l[i+1] in l1):
        print(l[i+1])
        count+=1
        break
if(count==0):
    print("unique")
