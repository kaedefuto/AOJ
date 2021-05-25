while True:
    h,w= map(int,input().split())
    if h==0 and w==0:
        break
    for i in range(h):
        for j in range(w):
            print("#",end="")
        print("")
    print("")
"""
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        print('#' * W)
    print('')
"""