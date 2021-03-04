import math
n=int(input("Enter the lower bound : "))
m=int(input("Enter the upper bound : "))
num_list=[]
for num in range(n,m+1):
    count=flag=0
    num=str(num)
    for i in num:
        count=count+1
        if int(i)%2!=0 :
            flag=1
    if count==4 and int(num)== (math.isqrt(int(num))**2) and flag==0:
        num_list.append(int(num))
if len(num_list)==0:
    print("List is Empty!")
else:
    print("Resultant list is :",num_list)
