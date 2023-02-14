n=input("enter the grade :")
if n!='A' or n!= 'B':
    print("A or B")
s=input("enter the salary :")
if s.isalpha():
    print("enter only numbers")
s=int(s)
if(s<=0):
    print("enter a valid salary")
elif(n==0):
    print("your salary bonus is=:",s*0.05+s)
elif(n=='C'):
    print("Enter a valid grade")
elif(s<0):
    print("enter a valid number")
    int(input("enter valid salary"))
elif(n=='B'):
    print("your salary bonus is=:",s*0.1+s)
elif(s<10000):
    print("your salary bonus is=:",s*0.02+s)
else:
    print("no bonus")
