def sosuu(n):
    is_prime = True

    # 2から n-1 までの数で割り切れるかどうか
    for p in range(2, n):
        if n % p == 0:
            is_prime = False
            break

    # 1と自分自身以外で割り切れなければ素数である
    if n == 1:
        is_prime = False

    return is_prime
