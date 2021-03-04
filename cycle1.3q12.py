list = [0,1,2,3,4,5,6,7,8,9]
print ("Original list:",list)
for i in list:
    if(i%2 == 0):
        list.remove(i)
print ("list after removing even numbers:",list)
