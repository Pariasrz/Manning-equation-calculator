
import math
import numpy as np
import matplotlib.pyplot as plt

#get inputs
q = float(input('Please Enter Discharge [Q(m^3/s)]\n'))
#b = float(input('Please Enter Bottom Width [B(m)]\n'))
#z = float(input('Please Enter Side Slope [Z]\n'))
s = float(input('Please Enter Longitudnial Slope [S]\n'))
n = float(input('Please Enter Roughness Coefficient [N]\n'))

b = [0.3, 0.45, 0.6, 0.9, 1.2, 1.5]
for i in np.arange(2, 100.5, 0.5):
    b.append(i)
    
#print(b)    

for i in b:
   
    k = i**(8/3)*n*q*(s**(-0.5))
    
    if (i < 0.6):
        z = 1
    elif i >= 0.6:
        z = 1.5
    
    yn = i*((1.145-0.4*(math.log10(z)))*k**0.61-k/3.5)
    if ( yn <= 0 ):
        yn=.05
 
    yn = 0.5*yn
    
    while(True):
         
      yn = yn + 0.01
      a = (i + z *yn) * yn
      p = i + 2*yn*(1 + z**2)**0.5
      r = a / p
      qc = 1/n*a*r**(2/3)*s**0.5
    
      if (qc >= q):
         
         break
              
    if (yn/i) > 0.5 and (yn/i) < 1:
       
        Yn = print('\nThe Depth of The Channel is [Yn (m)] %0.2f '% yn)
        V = q/a
        V = print('\nThe Velocity in The Channel is [ Vn (m/s)] %0.2f '% V)
        B = print('\nThe Bottom Width of The Channel is [ B(m)] %0.2f '% i)
        Z = print('\nThe Lateral slope of the channel is [  Z ] %0.2f '% z)
        print('')
        break
    if (q <= 0.3):
        fb = 0.2
    elif (q > 0.3 and q <= 1.2):
        fb = 0.25
    elif (q > 1.2 and q <= 5):
        fb = 0.3
    elif (q > 5 and q <= 7.5):
        fb = 0.35
    elif (q > 7.5 and q <= 10):
        fb = 0.4
    elif (q > 10 and q <= 15):
        fb = 0.45
    elif (q > 15 and q <= 20):
        fb = 0.5
        
print("FreeBoard is ", fb)
        
        
#drawing section
answer = input('Do you want to draw section? [Yes/No]\n')

if answer == 'yes' or answer =='Y'  or answer == 'y':
    x = []
    x.append(1)
    x.append(x[0]+1*0.5)
    x.append(x[1]+3)
    x.append(x[2]+z*(yn+0.3))
    x.append(x[3]+i)
    x.append(x[4]+z*(yn+0.3))
    x.append(x[5]+4)
    x.append(x[6]+z*0.5)    
    print(x)
    
    y = []
    y.append(yn+0.8)
    y.append(y[0]+0.5)
    y.append(y[1])
    y.append(y[2]-yn-0.3)
    y.append(y[3])
    y.append(y[2])
    y.append(y[2])
    y.append(y[0])
    
    xw = []
    xw.append(x[2]+0.3*z)
    xw.append(x[5]-0.3*z)
    
    yw = []
    yw.append(y[2]-0.3)

    f2 = []    
    for k in x:
        f2.append(1 + yn)
    
    plt.plot(x,f2, '--b')
    
    for j in np.arange(xw[0], xw[1], 0.2):
        plt.plot(j, yw[0])
    
    for j in range(0,7):
        plt.plot(x, y)
        
    
    print("sth", yw)
    
    vn = q/a
    print('\nQ = ', q)
    print('\nB = ', i)
    print('\nz = ', z)
    print('\nN = ', n)
    print('\nS = ', s)
    print('\nFreeBoard = ', fb)
    Yn = print('\nYn = %0.2f '% yn)
    Vn = print('\nVn = %0.2f '% vn)
    print(' ')
    print(' ')
    

     
Yn = "{:.2f}".format(yn)
Vn = "{:.2f}".format(vn)
#save the plot
plt.savefig('plot.png', dpi=300)

import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Manning.xlsx')
worksheet = workbook.add_worksheet()


items = (['Q (m^3 / s)', q],
         ['B (m) ', i],
         ['Z', z],
         ['N', n],
         ['S', s],
         ['Yn (m)', Yn],
         ['Vn (m/s)', Vn])

row = 0
col = 0

cell_format = workbook.add_format()
cell_format.set_bold()
cell_format.set_center_across()
cell_format.set_bg_color('lime')
#worksheet.set_row(0, 6, cell_format)

# Iterate over the data and write it out row by row.
for item, cost in (items):
    worksheet.write(row, col,item, cell_format)
    worksheet.write(row + 1, col, cost)
    col += 1

workbook.close()









