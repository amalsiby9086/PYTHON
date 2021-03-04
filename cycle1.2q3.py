names=["amal","ancy","siby","simal"]
count=0
for name in names:
    for letter in name:
        if letter =='a' or letter=='A':
            count=count+1
print("There are",count,"a in the list")
