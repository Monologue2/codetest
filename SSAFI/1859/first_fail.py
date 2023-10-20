T = int(input())

for i in range(T):

    N = int(input())
    prices = list(map(int, input().split(" ")))

    # 1. 현재 Index보다 높은 Index에 위치한 값들 중 Highest value  찾기
    # 2. Highest value - 현재 Index 값 저장, Highest value의 초기 값은 0
    # 반복 후 모두 추가
    re_sell = 0
    #Max 함수, List Slice 활용 / 최대값 min(iterable), max(iterable)
    for index in range(N): # N 대신 len(prices) 가능
        highest_value = 0
        if prices[index+1:len(prices)]: #empty 인 List는 False 처리
            highest_value = max(prices[index+1:len(prices)]) # Empty List Problem
        if highest_value > prices[index]:
            re_sell = re_sell + highest_value - prices[index]
    print(f"#{i+1} {re_sell}")