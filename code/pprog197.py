n=int(input())
l=list(map(int,input().split()))
l.sort()
a=l[len(l)-1]-l[0]
print(a)
