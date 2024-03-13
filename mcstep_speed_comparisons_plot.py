import matplotlib.pyplot as plt
import numpy as np

# Data
mc_steps = np.array([0,50,100,200,300,400,500,600,700,800,900,1000])
original = np.array([0,1.77,3.65,7.31,10.96,14.75,18.37,21.91,25.54,29.12,33.06,36.66])
numpy_vectorisation = np.array([0,1.17,2.36,4.76,7.19,9.56,11.95,14.44,16.85,19.06,21.53,23.97])
numba_jit = np.array([0,0.32,0.65,1.31,1.97,2.66,3.25,3.89,4.62,5.26,5.89,6.49])
numba_parallel_jit = np.array([0,0.32,0.65,1.32,1.93,2.62,3.3,3.92,4.56,5.14,5.89,6.45])
numpy_vectorisation_and_numba_parallel_jit = np.array([0,0.19,0.39,0.78,1.24,1.63,2.02,2.4,2.83,3.27,3.69,4.08])
cython_cdef_cmath = np.array([0,0.96,1.97,3.97,5.99,7.99,9.85,11.86,13.85,15.93,17.88,19.76])

# Plotting
plt.plot(mc_steps, original, label='original python', marker='o')
plt.plot(mc_steps, numpy_vectorisation, label='numpy vectorisation', marker='s')
plt.plot(mc_steps, numba_jit, label='numba jit', marker='D')
plt.plot(mc_steps, numba_parallel_jit, label='numba parallel jit', marker='^')
plt.plot(mc_steps, numpy_vectorisation_and_numba_parallel_jit, label='numba parallel jit with numpy vectorisation', marker='<')
plt.plot(mc_steps, cython_cdef_cmath, label='cython with cdef & cmath', marker='x')

# Adding labels/title & legend, and display plot
plt.xlabel('Number of MC Steps')
plt.ylabel('Time Taken (seconds)')
plt.title('Time vs MC Steps for Different Acceleration Approaches (nmax=50, temp=0.5)')
plt.legend()
plt.show()