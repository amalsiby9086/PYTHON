def longest(list2):
    max=len(list2[0])
    temp=list2[0]
    for i in list2:
        if (len(i)>max):
            max=len(i)
            temp=i
    print("Word with longest length:",temp,"\nLength:",max)
list1=["Amal","Ancy","Siby","Simal"]
longest(list1)
