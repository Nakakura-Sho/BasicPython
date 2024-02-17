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
def kouyaku(n):
    
    if n == 1:
        return True
    else:
        return False

answer = kouyaku(euclid(a,b))
print(answer)

