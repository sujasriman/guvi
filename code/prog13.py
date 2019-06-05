a=int(input())
count=0
if(a>0):
   for i in range(1,a+1):
       if(a%i==0):
           count=count+1
else:
    print("invalid")    
if(count==2):
    print("yes")
else:
    print("no") 
