T = int(input())

for i in range(T):
    integers = list(map(int, input().split(" ")))

    a, b = integers[0], integers[1]

    #if, elif, else
    if a < b:
        print(f"#{i+1} <")
    elif a == b: 
        print(f"#{i+1} =")
    else :
        print(f"#{i+1} >")
    