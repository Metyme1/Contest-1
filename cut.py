import math
n=input()
arr=[]

for i in n:
    j=ord(i)
    arr.append(j)
su=sum(arr)
if(su%100==0):
    
    tot=math.ceil(su/100)+1

    tot=tot*100
    self_love=math.floor((su/tot)*100)

    other=100-self_love
    print(str(other)+'%')
else:
    tot=math.ceil(su/100)

    tot=tot*100
    self_love=math.floor((su/tot)*100)

    other=100-self_love
    print(str(other)+'%')
    




    