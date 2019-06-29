n=int(input())
count=0
l=list(map(int,input().split()))
for i in range(n):
    if(l[i]%2!=0):
        count+=1
if(count==len(l)):
    print("odd")
else:
    print("even")
