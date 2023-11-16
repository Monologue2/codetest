bill = int(input())
N = int(input())

recipe = 0

for i in range(N):
    parse = input().split(" ")
    price , amount = int(parse[0]), int(parse[1])
    
    recipe = recipe + (price * amount)

if bill == recipe:
    print("Yes")
else:
    print("No")
    
    