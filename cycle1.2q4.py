list1=[2,4,5,6]
list2=[2,3,4,8]
common=[]
sum1=sum(list1)
sum2=sum(list2)
if len(list1)==len(list2):
    print("\nTwo lists are of same length")
else:
    print("\nTwo Lists are of Unequal Length")
if sum(list1)==sum(list2):
    print("\nThe Lists of Sum are equal")
else:
    print("\nThe Lists of Sum are not equal")
for i in list1:
    for j in list2:
        if i==j:
            common.append(i)
print("Common Elements Are : ",common)
