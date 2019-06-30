s1,s2=input().split()
count=0
if(len(s1)==len(s2)):
    for i in range(len(s1)):
        if(s[i].isupper()):
            if(ord(s1[i])==ord(s2[i]) or ord(s1[i])==ord(s2[i])-32):
               count+=1
        else:
            if(ord(s1[i])==ord(s2[i]) or ord(s1[i])==ord(s2[i])+32):
                count+=1
    if(count==len(s1)):
        print("yes")
    else:
        print("no")
else:
    print("no")
