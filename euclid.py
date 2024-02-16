a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
if a > b:
    A = a
    B = b
else:
    A = b
    B = a

while B != 0:
    A, B = B, A % B

print(A)