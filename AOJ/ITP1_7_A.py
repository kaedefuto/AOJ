
while True:
    x,y,z=map(int,input().split())
    k = x+y
    if x==-1 and y==-1 and z==-1:
        break
    elif x==-1 or y==-1:
        print("F")
    elif k>=80:
        print("A")
    elif 65<=k<80:
        print("B")
    elif 50<=k<65:
        print("C")
    elif 30<=k<50:
        if z>=50:
            print("C")
        else:
            print("D")
    elif k<30:
        print("F")
        


       
        
     
