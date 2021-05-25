while True:
    h,w= map(int,input().split())
    if h==0 and w==0:
        break
    for i in range(h):
        for j in range(w):
            if i%2==0 and j%2==0:
                print("#",end="")
            elif i%2==0 and j%2!=0:
                print(".",end="")

            if i%2!=0 and j%2!=0:
                print("#",end="")
            if i%2!=0 and j%2==0:
                print(".",end="")
        print("")
    print("")
