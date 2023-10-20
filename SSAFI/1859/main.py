T = int(input())

for i in range(T):

    # 순차 접근과 리스트 분할은 복잡도 문제 발생
    # Index 뒷 순번부터 접근하는 방법을 생각해보자
    # 뒤부터 볼 경우 리스트 복제를 할 필요 없음

    N = int(input())
    prices = list(map(int, input().split(" ")))
    # 마지막 price 부터 시작

    highest_price = prices[N - 1]

    # 마지막 prices 가 합쳐지므로 별도의 List 필요
    dp = [0] * N

    # highest_price 가 현재 price 보다 클 경우 : highest_price - price
    # highest_price 가 현재 price 보다 작을 경우 : highest_price = price
    for j in range(N - 2, -1, -1):
        if highest_price > prices[j]:
            dp[j] = highest_price - prices[j]
        else:
            highest_price = prices[j]

    print(f"#{i+1} {sum(dp)}")