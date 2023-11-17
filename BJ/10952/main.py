# Write Your Code

while(True):
    line = input().split(' ')
    A, B = int(line[0]), int(line[1])
    if(A == 0 & B == 0):
        break
    print(A + B)