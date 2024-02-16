from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
from math import sin, pi
#範囲を定義する
a = 0
b = 0.5*pi
N = 100
h = (b-a)/N

answer=0#初期化
for i in range(1,N+1):
    
    answer+=(h/2)*(sin(a+(i-1)*h) + sin(a+i*h))


print(answer)