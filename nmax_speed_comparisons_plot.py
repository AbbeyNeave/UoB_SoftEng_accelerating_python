import matplotlib.pyplot as plt
import numpy as np
# Data
nmax = np.array([5,10,20,30,40,50,60,70,80,90,100])
original = np.array([0.02,0.07,0.29,0.66,1.18,1.81,2.65,3.59,4.67,5.91,7.32])
numpy_vectorisation = np.array([0.02,0.05,0.19,0.43,0.76,1.18,1.69,2.33,3.04,3.84,4.79])
numba_jit = np.array([0,0.014,0.05,0.12,0.2,0.32,0.388,0.45,0.53,0.58,0.64])
numba_parallel_jit = np.array([0.07,0.02,0.05,0.12,0.23,0.32,0.46,0.63,0.82,1.03,1.27])
numpy_vectorisation_and_numba_parallel_jit = np.array([0.00,0.01,0.04,0.07,0.13,0.19,0.29,0.39,0.51,0.64,0.82])
cython_cdef_cmath = np.array([0.01,0.04,0.16,0.35,0.65,0.99,1.42,1.95,2.51,3.18,3.99])
# Plotting
plt.plot(nmax, original, label='original python', marker='o')
plt.plot(nmax, numpy_vectorisation, label='numpy vectorisation', marker='s')
plt.plot(nmax, numba_jit, label='numba jit', marker='D')
plt.plot(nmax, numba_parallel_jit, label='numba parallel jit', marker='^')
plt.plot(nmax, numpy_vectorisation_and_numba_parallel_jit, label='numba parallel jit with numpy vectorisation', marker='<')
plt.plot(nmax, cython_cdef_cmath, label='cython with cdef & cmath', marker='x')
# Adding labels/title & legend, and display plot
plt.xlabel('nmax')
plt.ylabel('Time Taken (seconds)')
plt.title('Time vs Lattice Size for Different Acceleration Approaches (mcsteps=50, temp=0.5)')
plt.legend()
plt.show()