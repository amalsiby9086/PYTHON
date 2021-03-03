list1=['a','e','i','o','u','A','E','I','O','U']
string=input('Enter the string:')
list2=[]
for i in string:
 for j in list1:
     if(i==j):
         list2.append(i)
         break
print('Vowel List')
print(list2)
