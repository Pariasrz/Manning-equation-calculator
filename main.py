import math


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
