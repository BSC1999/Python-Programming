def addBinary(a, b):
    a = int(a, 2)
    b = int(b, 2)
    c = a + b
    return bin(c)[2:]

a = "15"
b = "45"
print(addBinary(a,b))
