def plus(a, b):
    while b>0:
        a=a+1 if b>0 else a-1
        b=b-1 if b>0 else b+1
    return a
