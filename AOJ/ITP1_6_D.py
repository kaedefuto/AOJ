
n,m= map(int,input().split())

count = [list(map(int,input().split())) for i in range(n)]

count1 = [int(input()) for i in range(m)]

num =0
for i in range(n):
    for j in range(m):
        num+=count[i][j]*count1[j]
    print(num)
    num=0 
       
        
     
