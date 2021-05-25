z =[]
count=0
while True:
    a,b,c= input().split()
    x = int(a)
    y = int(c)
    if b=="+":
        z.append(x+y)
    elif b=="-":
        z.append(x-y)
    elif b=="*":
        z.append(x*y)
    elif b=="/":
        z.append(x//y)
    elif b=="?":
        break
    count+=1
for i in range(count):
    print(z[i])





    