# Input 시 Line 단위
T = int(input())


for i in range(T):
    
    ans = 0
    # List 내의 String에 Int() Mapping
    integers = list(map(int, input().split(" ")))
    for j in integers:
        # if문 % /
        if (j%2 == 1):
            ans = ans + j

    print(f"#{i+1} {ans}")
