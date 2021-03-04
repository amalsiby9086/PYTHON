name=input('Enter the string:')
char=name[0]
new=''
flag=0
for i in name:
    if(i==char and flag>1):
        new=new+'$'
    else:
        new=new+i
        flag = flag + 1
print(new)
