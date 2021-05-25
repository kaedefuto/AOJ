i=0
a= []
while True:
    x = int(input())
    if x==0:
        break
    else:
        a.append(x)
    i+=1
for j in range(i):
    print("Case "+str(j+1)+": "+str(a[j]))