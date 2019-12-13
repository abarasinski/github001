fibo=[0,1]
x,y=0,1
i=0
while y<20:
    #print(y)
    if not __debug__:
        print("i=",i)
        print("fibo =",fibo)         
        print("fibo[i-2] =", x)
        print("fibo[i-1] =", y)
        print()
        i+=1
    x,y = y,x+y
    fibo.append(y)

if __debug__:
    print(fibo)
