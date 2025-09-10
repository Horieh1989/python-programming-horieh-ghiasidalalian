def plus(a, b):
    while b>0:
        a=a+1 if b>0 else a-1
        b=b-1 if b>0 else b+1
    return a
def minus(a, b):
    return plus(a, -b)
def multiply(a, b):
    if b==0 or a==0:
        return 0
    elif b<0:
        return -multiply(a, -b)
    else:
        return plus(a, multiply(a, b-1))
    
a = 3
b = 5