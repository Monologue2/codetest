# Python 반올림, 내림, 올림 모듈
import math

T = int(input())

for i in range(T):
    integers = list(map(int, input().split(" ")))

    ans = 0
    for j in integers:
        ans = ans + j
    # Python 반올림 round(integer, index) , 내림 floor(integer, index), 올림 ceil(integer, index)
    print(f"#{i+1} {round(ans/len(integers))}")