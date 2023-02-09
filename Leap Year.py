year=input("enter a year: ")
for i in year:
    if i==".":
        print("enter a valid year")
year=int(year)
if(int(year)<=0):
    print("enter a valid year")
elif(year%4==0)and(year%100!=0):
    print(year, " is a leap year")
elif(year%400==0):
    print(year, " is a leap year")
else:
    print(year, " is not a leap year")
