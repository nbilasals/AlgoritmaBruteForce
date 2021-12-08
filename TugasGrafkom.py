x1=int(input('Masukkan x1 = '))
x2=int(input('Masukkan x2 = '))
y1=int(input('Masukkan y1 = '))
y2=int(input('Masukkan y2 = '))

x=x1
y=y1
if x1==x2 : 
    print('Titik-titik pembentuk garis: ')
    while y <= y2 : 
        print ('(',x ,',',y+1,')' )
        y=y+1
        
 elif y1==y2 :
    print('Titik-titik pembentuk garis: ')
    while x <= x2 : 
        print ('(',x+1 ,',',y,')' )
        x=x+1
        
  else :
    m=(y2-y1)/(x2-x1)
    N=(x2-x1)+1
    print ('m=(y2-y1)/(x2-x1)')
    print ('Nilai m adalah ( ',y2 ,'-' ,y1,')/(',x2,'-',x1,') = ',m)
    print ('N=(x2-x1)+1')
    print ('Nilai N adalah ( ',x2,'-',x1, ') +1= ',N)
    print ('Titik-titik pembentuk garis: ')
    i=0
    while i<N:
        y= m*(x-x1)+y1
        ya=round(y)
        print ('(',x ,',',ya,')' )
        i=i+1;
        x=x+1;
      
      
        
        
 
