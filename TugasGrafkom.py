print("Program Membuat Garis dengan Algoritma Brute Force")
print('==================================================')

import numpy as np
import matplotlib.pyplot as plt

x1=int(input('Masukkan x1 = '))
y1=int(input('Masukkan y1 = '))
x2=int(input('Masukkan x2 = '))
y2=int(input('Masukkan y2 = '))

x=x1
y=y1
xs = []
ys = []

if x1==x2:
    print('Titik-titik pembentuk garis: ')
    while y <= y2 : 
        print ('(',x ,',',y+1,')' )
        y=y+1
        xs.append(x)
        ys.append(y)

elif y1==y2:
    print('Titik-titik pembentuk garis: ')
    while x <= x2 : 
        print ('(',x+1 ,',',y,')' )
        x=x+1
        xs.append(x)
        ys.append(y)
        
else:
    m=(y2-y1)/(x2-x1)
    N=(x2-x1)+1
    print ('m=(y2-y1)/(x2-x1)')
    print ('Nilai m adalah ( ',y2 ,'-' ,y1,')/(',x2,'-',x1,') = ',m)
    print ('N=(x2-x1)+1')
    print ('Nilai N adalah ( ',x2,'-',x1, ') + 1= ',N)
    print ('Titik-titik pembentuk garis: ')
    i=0
    while i<N:
        y= m*(x-x1)+y1
        ya=round(y)
        print ('(',x ,',',ya,')' )
        i=i+1;
        xs.append(x)
        ys.append(y)
        x=x+1;

np.array(xs)
np.array(ys)
plt.plot(xs,ys)
plt.grid()
plt.show()
