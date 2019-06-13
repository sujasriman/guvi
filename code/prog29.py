import math
minutes=int(input())
if(minutes>60):
    h=minutes/60
    h=math.floor(h)
    m=minutes-(h*60)
else:
    h=0
    m=minutes
print(h,m)
