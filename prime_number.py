def is_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# aの素数判定
if is_prime_number(a):
    print(str(a) + ' は素数である。')
else:
    print(str(a) + ' は素数ではない。')

# bの素数判定
if is_prime_number(b):
    print(str(b) + ' は素数である。')
else:
    print(str(b) + ' は素数ではない。')
