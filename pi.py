def pi():
    print('number of terms')
    sn = input()
    if len(sn)>8:
        print('error; too long')
        return
    n=int(sn)
    x=1
    s=1
    t=0
    for i in range(n):
       t+=s*1/x
       x+=2
       s*=-1
    print(4*t)
pi()