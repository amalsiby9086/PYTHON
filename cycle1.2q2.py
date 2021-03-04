num=[]
n=int(input("Enter the no of elements"))
print("Ente the elements")
for i in range(0,n):
    no=int(input())
    if no >100:
        num.append("Over")
    else:
        num.append(no)
print("Res is",num)
