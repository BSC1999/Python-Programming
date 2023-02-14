def perfectsquare(n):
    res=n
    #print(res)
    #print(n,"n")
    for i in range(1,n+1):
        temp=i*i
        #print(temp,"i^2")
        if temp>n:
            break
        else:
            res=min(res,1+perfectsquare(n-temp))
            #print(res)
    return res
n=int(input("enter a number: "))
if n<=3:
    print("1")
else:
    print(perfectsquare(n))
