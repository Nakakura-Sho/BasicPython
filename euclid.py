def euclid(a,b):


    if a > b:
        A = a
        B = b
    else:
        A = b
        B = a

    while B != 0:
        A, B = B, A % B
    return A
#ここから問4
A = euclid(a,b)
if A == 1:
    return True
else:
    return False