# Write Your Code

N = int(input())

for i in range(1, N + 1):
    star = '*'*i
    output = f'{star:>{N}}'
    print(output)