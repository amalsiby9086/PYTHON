list1 = []
n = int(input("Enter the number of elements: "))
print ("Enter the numbers: ")
for i in range (0,n):
 num = int(input())
 list1.append(num)
print("Elements:",list1)
print ("Positive integers: ")
for i in list1:
 if (i>0):
     print(i)
