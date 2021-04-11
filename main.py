import math
import numpy as np
import matplotlib.pyplot as plt

#get inputs
q = float(input('Please Enter Discharge [Q(m^3/s)]\n'))
b = float(input('Please Enter Bottom Width [B(m)]\n'))
z = float(input('Please Enter Side Slope [Z]\n'))
s = float(input('Please Enter Longitudnial Slope [S]\n'))
n = float(input('Please Enter Roughness Coefficient [N]\n'))

k = b**(8/3)*n*q*(s**(-0.5))

if (z == 0):
    yn = b*(1.155*k+(2/3)*k**0.547)
    
else:
    yn = b*((1.145-0.4*(math.log10(z)))*k**0.61-k/3.5)
    

if (b == 0):
    k = n*q*(s**-(0.5))
    yn = k**(3/8)*z**(-5/8)*(4*(1+z**2))**(1/8)
    
yn = 0.5*yn

while(True):
    yn = yn + 0.01
    a = (b + z *yn) * yn
    p = b + 2*yn*(1 + z**2)**0.5
    r = a / p
    qc = 1/n*a*r**(2/3)*s**0.5
    
    if (qc >= q):
        print('\n The Depth of The Channel is [Yn (m)] ', yn)
        print('\n The Velocity in The Channel is [Vn (m/s)] ', q/a)
    
        break

#drawing section
answer = input('Do you want to draw section? [Yes/No]\n')
if answer == 'yes' or answer == 'Yes' or answer =='Y':
    x = []
    x.append(1)
    x.append(x[0]+1*0.5)
    x.append(x[1]+3)
    x.append(x[2]+z*(yn+0.3))
    x.append(x[3]+b)
    x.append(x[4]+z*(yn+0.3))
    x.append(x[5]+4)
    x.append(x[6]+z*0.5)
    
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
    
    for i in np.arange(xw[0], xw[1], 0.2):
        plt.plot(i, yw[0])
    
    for i in range(0,7):
        plt.plot(x, y)
        
    print('\nQ = ', q)
    print('\nB = ', b)
    print('\nz = ', z)
    print('\nN = ', n)
    print('\nS = ', s)
    print('\nYn = ', yn)
    print('\nVn = ', q/a)

#save the plot
plt.savefig('plot.png', dpi=300)
