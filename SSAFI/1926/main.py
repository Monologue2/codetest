T = int(input())

# range(end)
# range(start, end), 이때 end - 1 까지
# range(start, end, step), 이때 end - 1 까지

for i in range(1, T + 1):
    numbers = str(i)
    # number가 3인 부분은 걸러내지만, 박수를 칠 땐 숫자를 부르지 않는 경우
    pop = False

    # 출력할 수 있는 2가지, 박수 칠 때와 숫자를 부를 때
    dp = ""
    ans = ""
    for number in numbers:
        # number 가 0 일 경우에도 박수를 쳐버리는 경우
        if(int(number) % 3 == 0 and int(number) != 0):
            dp = dp + "-"
            pop = True
        else:
            ans = ans + number
            
    if pop:
        print(dp, end=" ")
    else:
        print(ans, end=" ")