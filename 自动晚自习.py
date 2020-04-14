import time
import webbrowser
bio = 'https://ke.qq.com/webcourse/index.html#cid=1402813&term_id=101500404&taid=6516929973282749&lite=1'
eng = 'https://ke.qq.com/webcourse/index.html#cid=1352872&term_id=101450453&taid=6364115036841128&lite=1'
chi = 'https://ke.qq.com/webcourse/index.html#cid=1343101&term_id=101440364&taid=6568722983845501&lite=1'
math = 'https://ke.qq.com/webcourse/index.html#cid=1343788&term_id=101441051&taid=6298865893671212&lite=1'
chem = 'https://ke.qq.com/webcourse/index.html#cid=1353900&term_id=101451481&taid=7172213133584556&lite=1'
phy = 'https://ke.qq.com/webcourse/index.html#cid=1363972&term_id=101461555&taid=6370196710543364&lite=1'
week = str(time.strftime("%w"))
now = 0
def start(a,b):
    webbrowser.open(a,new = 2)
    time.sleep(3600)
    webbrowser.open(b,new = 2)
while now < 1929:
    now = int(time.strftime("%H%M", time.localtime()))
    time.sleep(10)
else:
    if week == '1':
        start(eng,chi)
    elif week == '2':
        start(math,phy)
    elif week == '3':
        start(chem,eng)
    elif week == '4':
        start(bio,math)
    elif week == '5':
        start(chem,phy)
    else:
        quit()
