a = input("aの値を入力: ")
#b = input("bの値を入力: ")

# TODO
n = a
is_prime = True

# 2から n-1 までの数で割り切れるかどうか
for p in range(2, n):
    if n % p == 0:
        is_prime = False
        break

# 1と自分自身以外で割り切れなければ素数
if n == 1:
    is_prime = False

if is_prime:
    print(str(n) + ' は素数である。')
else:
    print(str(n) + ' は素数ではない。')