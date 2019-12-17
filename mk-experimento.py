'''
Este script crea un set de observaciones sintéticas.
El modelo es una línea recta y = mx + n con (m, n) = (2.5, -1.0)
y ruido normal con sigma=2.0
'''

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(8978)

m = 2.5
n = -1.0
sigma = 2.0

n_data = 10

x = np.random.uniform(low=-1, high=3, size=n_data)
y = m * x + n + np.random.normal(loc=0, scale=sigma, size=n_data)
e_y = np.ones(n_data) * 2.0

data = np.column_stack((x, y, e_y))

np.savetxt('experiment.dat', data, fmt='%6.3f  %6.3f  %3.1f', 
           header='   x       y  e_y')