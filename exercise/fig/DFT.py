import matplotlib.pyplot as plt
import numpy as np

#Time Continous Signal
x = np.linspace(0,8)
y = np.sin((2*np.pi)*x/8) + 0.5 * np.sin((4*np.pi)*x/1)
plt.figure(figsize=(8,6))
plt.plot(x, y, 'b')
plt.grid(True)
plt.show()


#Discrete Time Signal
x = np.arange(0,8)
y = np.sin((2*np.pi)*x/8) + 0.5 * np.sin((4*np.pi)*x/1)
plt.figure(figsize=(8,6))
plt.stem(x, y, 'b')
plt.grid(True)
for i in range(len(x)):
    plt.text(x[i], y[i], f"{y[i]:.2f}", 
             ha='center', va='bottom', fontsize=9)
plt.show()


def DFT(x):
    """
    Function to calculate DFT of 1D real valued signal x.
    """
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N,1))
    e = np.exp(-2j*np.pi*k*n/N)
    
    X = np.dot(e,x)
    return X

X = DFT(y)

# calculate the frequency
sr = 1
N = len(y)
n = np.arange(N)
T = N/sr
freq = n/T 

plt.figure(figsize = (8, 6))
plt.stem(freq, abs(X), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('DFT Amplitude |X(freq)|')
plt.show()
    
    

