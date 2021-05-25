r,c= map(int,input().split())

a = [list(map(int,input().split())) for i in range(r)]

for i in range(r):
    a[i].append(sum(a[i]))

Column_sum=[0]*(c+1)

for i in range(c+1):
    for j in range(r):
        Column_sum[i]+=a[j][i]

for i in range(r):
    print(*a[i])
print(*Column_sum)

        


       
        
     
