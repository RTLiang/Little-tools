import tkinter as tk
win=tk.Tk()
print('请输入x值，y值，在x值中输入 00 表示输入完毕')
lx=[]
cond=True
sigx=0
sigy=0
sigxy=0
sigx2=0
while cond==True:
    x0=input('x')
    if x0 =='00' :
        cond=False
    else:
        x=int(x0)
        lx.insert(x,-1)
        y=int(input('y'))
        sigx=sigx+x
        sigy=sigy+y
        sigxy=sigxy+x*y
        sigx2=sigx2+x*x
n=len(lx)
avex=sigx/n
avey=sigy/n
bup=sigxy-n*avex*avey
bdown=sigx2-n*avex**2
b0=bup/bdown
b=str(b0)
a=str(avey-b0*avex)
result='回归方程为 y =' + b +' x +'+ a
wid=len(result)
win.title('回归线性方程')
win.geometry('800x600')
l=tk.Label(win,text=result,width=wid,height=7)
l.pack()
