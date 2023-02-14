a=int(input("enter a number :"))
if(a<=0):
    print("Enter a Positive number")
b=int(input("enter a second number :"))
if(b<=0):
    print("Enter a Positive number")
c=a*b
d=a+b
if(c%d==0):
    print("YEAH")
else:
    print("NAH")
