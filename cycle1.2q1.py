string1=input("Enter the word:")
list1=string1.split(' ')
print('count')
dict1=dict()
for i in list1:
    if i in dict1:
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
print(dict1)
