year=int(input("Enter the current year:"))
future=int(input("Enter the future year:"))
print("Leap years are: ")
for year in range (year,future+1):
 if(year%4==0 and year%100!=0):
     print(year)
 if(year%400==0):
     print(year)
