# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:02:51 2019

@author: u1981125
"""

# Bloch Equations

import matplotlib.pyplot as plt
import math

# initial state
Mx = 0
My = 0
Mz = 1
M0 = 1

dt = 0.0001
gamma = 1
T1 = 3 
T2 = 3

Bx = 0
By = 0
Bz = 50

t = []
x = []
y = []
z = []
i = 0
bz = []
lz = []

#while ((M0 - Mz) > 0.01 and i*dt > 1):
for l in range(0, 80000):   
    if (i * dt == 0.5):
        Bx = 50
        Bz = 0
    if ((i * dt) >= 0.5320):
        Bx = 0
        Bz = 50
    
    t.append(i * dt)
    x.append(Mx)
    y.append(My)
    z.append(Mz)
    
    dMx = dt * (gamma * (My * Bz - Mz * By) - (Mx / T2))
    dMy = dt * (gamma * (Mz * Bx - Mx * Bz) - (My / T2))
    dMz = dt * (gamma * (Mx * By - My * Bx) - ((Mz - M0) / T1))
    
    Mx = Mx + dMx
    My = My + dMy
    Mz = Mz + dMz
    bz.append(Bz/50.)
    lz.append(math.sqrt(math.pow(Mx, 2) + math.pow(My, 2) + math.pow(Mz, 2)))
    i+=1
    
    
    
plt.plot(t, x, label="x")
plt.plot(t, y, label="y")
plt.plot(t, z, label="z")
plt.plot(t, bz, label="Bz")
plt.plot(t, lz, label="Magnitude")
plt.legend()
plt.ylim((-1, 2))
plt.show()