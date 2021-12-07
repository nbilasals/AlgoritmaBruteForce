x1=int(input('Masukkan x1 = '))
x2=int(input('Masukkan x2 = '))
y1=int(input('Masukkan y1 = '))
y2=int(input('Masukkan y2 = '))

if x1==x2 :
    y1=y1+1
    x1=x1
    y2=y2+1
    x2=x2
    print ('Titik pembentuk garis: ')
    print ('(',x1 ,',',y1,') dan(',x2 ,',',y2,')' ) 
elif y1==y2 :
    x1=x1+1
    y1=y1
    x2=x2+1
    y2=y2
    print ('Titik pembentuk garis: ')
    print ('(',x1 ,',',y1,') dan(',x2 ,',',y2,')' ) 
else :
    m=(y2-y1)/(x2-x1)
    N=(x2-x1)+1
    print ('m=(y2-y1)/(x2-x1)')
    print ('Nilai m adalah ( ',y2 ,'-' ,y1,')/(',x2,'-',x1,') = ',m)
    print ('N=(x2-x1)+1')
    print ('Nilai N adalah ( ',x2,'-',x1, ')= ',N)
    print ('Titik-titik pembentuk garis: ')
    x=x1
    while x<=N+1:
        y= m*(x-x1)+y1
        ya=round(y)
        print ('(',x ,',',ya,')' )
        x=x+1;

        
