x =[]
y= []
count=0
while True:
    a,b=list(map(int,input().split()))
    if a==0 and b==0:
        break
    x.append(a)
    y.append(b)
    count+=1
for i in range(count):
    if x[i]>y[i]:
        print(y[i],x[i])
    else :
        print(x[i],y[i])