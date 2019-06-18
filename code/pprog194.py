def r_p_s(a,b):
    if((a=='R' and b=='P')or(a=='P' and b=='R')):
        return 'P'
    elif((a=='R' and b=='S')or(a=='S' and b=='R')):
        return 'R'
    elif((a=='S' and b=='P')or(a=='P' and b=='S')):
        return 'S'
    elif(a==b):
        return 'D'
c,d=input().split()
ans=r_p_s(c,d)
print(ans)
