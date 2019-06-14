import math
n=int(input())
l=list(map(int,input().split()))
l.sort()
mid=math.ceil(len(l)/2)
print(l[mid-1])
