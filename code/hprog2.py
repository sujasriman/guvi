n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
if((0 in l)and(l.count(0)==n)):
    print(0)
else:
    for i in range(len(l)-1):
        print(l[i],end='')
    print(l[len(l)-1])
