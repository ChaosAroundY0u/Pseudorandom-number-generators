import numpy as np
import matplotlib.pyplot as plt
import time

t = np.linspace(-2*np.pi, 2*np.pi, 1024)

A1 = 2
omega1 = 3
fi1 = np.pi / 2

A2 = 2.5
omega2 = 1.7
fi2 = 0

signal = A1 * np.sin(2*np.pi*omega1 * t + fi1) + A2 * np.cos(2*np.pi*omega2 * t + fi2)
plt.figure(1, label = "Signal")
plt.plot(t, signal)
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Signal")
plt.show()

def discrete_fourier_transform(signal): #N**2 operations
    N = len(signal)
    ans = np.zeros(N, dtype = complex)
    for k in range(N):
        for n in range(N):
            ans[k] += signal[n] * np.exp(-1j * 2 * np.pi * k * n / N)       
    return ans

freqs = np.arange(len(signal))
start = time.perf_counter()
spectr = discrete_fourier_transform(signal)
finish = time.perf_counter()
print("Manual DFT: ", finish - start)      

plt.figure(2, label = "Spectr (DFT)")
plt.plot(freqs, spectr)
plt.grid(True)
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("Spectr (DFT)")
plt.show()

def inverse_discrete_fourier_transform(spectr):
    N = len(spectr)
    ans = np.zeros(N, dtype = complex)
    for k in range(N):
        for n in range(N):
            ans[k] += 1 / N * spectr[n] * np.exp(1j * 2 * np.pi * k * n / N)
    return ans

start = time.perf_counter()
restored_signal = inverse_discrete_fourier_transform(spectr)
finish = time.perf_counter()
print("Manual IDFT: ", finish-start)

plt.figure(3, label = "Restored signal (IDFT)")
plt.plot(t, restored_signal)
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Restored signal (IDFT)")
plt.show()

def fast_fourier_transform(signal): #N*log2(N) operations
    signal = np.asarray(signal)
    N = signal.shape[0]
    if N % 2 > 0:
        raise ValueError("size of input must be a power of 2")
    elif N <= 32:
        return discrete_fourier_transform(signal)
    else:
        X_even = fast_fourier_transform(signal[0::2])
        X_odd = fast_fourier_transform(signal[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:int(N // 2)] * X_odd,
                               X_even + factor[int(N // 2):] * X_odd])
start = time.perf_counter()
spectr_fft = fast_fourier_transform(signal)
finish = time.perf_counter()
print("Manual FFT: ", finish - start)

plt.figure(4, label = "Spectr (FFT)")
plt.plot(freqs, spectr_fft)
plt.grid(True)
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("Spectr (FFT)")
plt.show()


def inverse_fast_fourier_transform(signal):
    signal = np.asarray(signal)
    N = signal.shape[0]
    if N % 2 > 0:
        raise ValueError("size of input must be a power of 2")
    elif N <= 32:
        return inverse_discrete_fourier_transform(signal)
    else:
        X_even = inverse_fast_fourier_transform(signal[0::2])
        X_odd = inverse_fast_fourier_transform(signal[1::2])
        factor = np.exp(2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:int(N // 2)] * X_odd,
                               X_even + factor[int(N // 2):] * X_odd]) / 2
    
start = time.perf_counter()
restored_signal_fft = inverse_fast_fourier_transform(spectr_fft)
finish = time.perf_counter()
print("Manual IFFT: ", finish - start)
plt.figure(5, label = "Restored signal (IFFT)")
plt.plot(freqs, restored_signal_fft)
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Signal")
plt.show()

start = time.perf_counter()
spectr_vstroen = np.fft.fft(signal)
finish = time.perf_counter()
print("np.fft.fft: ", finish - start)
plt.figure(6, label = "Spectr np.fft.fft")
plt.plot(freqs, spectr_vstroen)
plt.grid(True)
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("Spectr (np.fft.fft)")
plt.show()

start = time.perf_counter()
restored_signal_vstroen = np.fft.ifft(spectr_vstroen)
finish = time.perf_counter()
print("np.fft.ifft: ", finish - start)

plt.figure(7, label = "Restored signal np.fft.ifft")
plt.plot(freqs, restored_signal_vstroen)
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Restored signal np.fft.ifft")
plt.show()
