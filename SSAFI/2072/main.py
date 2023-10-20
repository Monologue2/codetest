T = int(input())

for i in range(T):
    
    ans = 0
    integers = list(map(int, input().split(" ")))
    for j in integers:
        if (j%2 == 1):
            ans = ans + j

    print(f"#{i+1} {ans}")
