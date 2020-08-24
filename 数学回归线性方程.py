print('请输入x值，y值(至少两组数据)，在x值中输入 00 表示输入完毕')
ly=[]
lx=[]
cond=True
sigx=0
sigy=0
sigxy=0
sigx2=0
sse = 0
sst = 0
while cond==True:
    x0=str(input('x'))
    if x0 =='00' :
        cond=False
    else:
        x=float(x0)
        lx.insert(-1 , float(x))
        y=float(input('y'))
        ly.insert(-1, float(y))
        sigx=sigx+x
        sigy=sigy+y
        sigxy=sigxy+x*y
        sigx2=sigx2+x*x
n=len(ly)
if n <= 1:
    result ='请输入至少两组数据'
else :
    avex=sigx/n
    avey=sigy/n
    bup=sigxy-n*avex*avey
    bdown=sigx2-n*avex**2
    b0=bup/bdown
    b=str(b0)
    a=str(avey-b0*avex)
    result='回归方程为 y =' + b +' x +'+ a
    print(result)
    while n >= 1:
        xx = float(lx[-1])
        yy = float(ly[-1])
        sse = float((((xx * b0) + float(a)) - avey)**2) + sse
        sst = float((yy - avey)**2) +sst
        del lx[-1]
        del ly[-1]
        n -=1
s = sse/sst
print('R^2=',s)
