# -*- coding: utf-8 -*-

# Discrete Fourier Transform

import numpy as npy

# caclulate discrete fourier transform
# input is an array of complex numbers
def DFT(signal):
    n = len(signal)
    f = []
    for s in range(0, n):
        k=0
        for i in range(0, n):
            k += signal[i]*npy.exp(-1*1j*2*npy.pi*s*(i/n))
        f.append(npy.round(k, decimals=2))    
    return f  


# caclulate inverse discrete fourier transform
def InvDFT(signal):
    n = len(signal)
    f = []
    for s in range(0, n):
        k=0
        for i in range(0, n):
            k += signal[i]*npy.exp(1j*2*npy.pi*s*(i/n))
        f.append(npy.round(k/n, decimals=2))    
    return f
  

signal = [5+1j, 7+8j, 8+2j, 100+9j, 15, -100, 0.898]
print("Signal: ")
print(signal)
print()

print("Discret Fourier Transform: ")
print(DFT(signal))
print()

# calculate DFT using numpy API
print("Discret Fourier Transform (Numpy API): ")
print(npy.round(npy.fft.fft(signal), decimals=2))
print()

print("Inverse Discret Fourier Transform: ")
print(InvDFT(DFT(signal)))




