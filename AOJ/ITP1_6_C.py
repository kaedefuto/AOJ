"""
count = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
n = int(input())

for i in range(n):
    b,f,r,v=map(int,input().split())
    count[b-1][f-1][r-1] += v


for i in range(4):
    for j in range(3):
        for k in range(10):          
            print(count[i][j][k],end="")
        print(" ")
    if i==3:
        break
    print("####################")
"""
residence = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

number = int(input())

for i in range(number):
    tou, kai, heya, hito = map(int, input().split())
    residence[tou-1][kai-1][heya-1] += hito

for n in range (4):
    for i in range (3):
        for j in range (10):
            print(' ', end = '')
            print(residence[n][i][j], end = '')
        print()

    if n == 3:
        break
    else :
        print('#'*20)