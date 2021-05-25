n,m,l= map(int,input().split())

a = [list(map(int,input().split())) for i in range(n)]
b = [list(map(int,input().split())) for i in range(m)]

c=[]
for i in range(n):
    line=[]
    for j in range(l):
        count=0
        for k in range(m):
            count +=a[i][k]*b[k][j]
        line.append(count)
    c.append(line)
for i in c:
    print(*i)



        


        


       
        
     
