n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
print(l[len(l)-2])
