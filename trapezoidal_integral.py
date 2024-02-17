from math import sin, pi

def fun(f,a=0, b=1, N=100):
    h = (b - a) / N
    answer = 0

    for i in range(1, N + 1):
        answer += (h / 2) * (f(a + (i - 1) * h) + f(a + i * h))

    return answer

result = fun(sin,0,0.5*pi,50)
print(result)
