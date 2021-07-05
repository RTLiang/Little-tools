diction = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
diction1 = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
word = input('word')
i = int(input('i'))
n='code is '
w=[]
re2=[]
for wo in word:
    w.append(wo)
#print(w)
replace1 =[diction[a] if a in w else a for a in w]
#print(replace1)
for r in replace1:
    r = r+i
    if r <= 0:
        r+= 26
    if r>26:
        r -= 26
    re2.append(r)
#print(replace1)
#print(re2)
replace2=[diction1[a] if a in re2 else a for a in re2]
for m in replace2:
    n=n+str(m)
print(n)
