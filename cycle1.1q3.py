list1 =[]
n = int(input("Enter the number of elements: "))
print("Enter the numbers: ")
for i in range(0,n):
 num = int(input())
 list1.append(num)
for i in list1:
 print('The square of',i,'is', i*i)
