# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:43:49 2019

@author: u1981125
"""


# Bloch Equations

import matplotlib.pyplot as plt
import math
import scipy.fftpack as fft

# initial state

def generate_spec(ta, tb):
    MxA = 0.5
    MxB = 0.5
    MyA = 0
    MyB = 0
    MzA = 0
    MzB = 0
    M0 = 0.5
    
    dt = 0.0001
    gammaA = 0.5
    gammaB = 1.2
    T1A = 3
    T1B = 3 
    T2A = 3
    T2B = 3

    
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
     
        t.append(i * dt)
        x.append(MxA + MxB)
        y.append(MyA + MyB)
        z.append(MzA + MzB)
        
        dMxA = dt * (gammaA * (MyA * Bz - MzA * By) - (MxA / T2A) - (MxA / ta) + (MxB / tb))
        dMyA = dt * (gammaA * (MzA * Bx - MxA * Bz) - (MyA / T2A) - (MyA / ta) + (MyB / tb))
        dMzA = dt * (gammaA * (MxA * By - MyA * Bx) - ((MzA - M0) / T1A) - (MzA / ta) + (MzB / tb))
        dMxB = dt * (gammaB * (MyB * Bz - MzB * By) - (MxB / T2B) - (MxB / tb) + (MxA / ta))
        dMyB = dt * (gammaB * (MzB * Bx - MxB * Bz) - (MyB / T2B) - (MyB / tb) + (MyA / ta))
        dMzB = dt * (gammaB * (MxB * By - MyB * Bx) - ((MzB - M0) / T1B) - (MzB / tb) + (MzA / ta))
        
        MxA = MxA + dMxA
        MyA = MyA + dMyA
        MzA = MzA + dMzA
        MxB = MxB + dMxB
        MyB = MyB + dMyB
        MzB = MzB + dMzB
        
        bz.append(Bz/50.)
        lz.append(math.sqrt(math.pow(MxA + MxB, 2) + math.pow(MyA + MyB, 2) + math.pow(MzA + MzB, 2)))
        i+=1
    return [t, x, y, z, bz, lz]
    
for i in [0.01, 0.1, 0.5, 1]:
    [t, x, y, z, bz, lz] = generate_spec(i, i)
    plt.plot(fft.fft(x), label=str(i))
    
#plt.plot(t, x, label="x")
#plt.plot(t, y, label="y")
#plt.plot(t, z, label="z")
#plt.plot(t, bz, label="Bz")
#plt.plot(t, lz, label="Magnitude")
plt.legend()
#plt.ylim((-1, 2))
plt.xlim((0, 100))
plt.show()