from scipy.io import wavfile
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import math

#audio amplitude over time(numpy array) and samplin rate(int), keep sampling size the same
#m1, sr1 = librosa.load('M1.wav', sr=None)
#m2, sr2 = librosa.load('M2.wav', sr=None)
#m3, sr3 = librosa.load('M3.wav', sr=None)

m1, data1 = wavfile.read("M1.wav")
m2, data2 = wavfile.read("M2.wav")
m3, data3 = wavfile.read("M3.wav")

data1 = data1.astype(np.float64)
data2 = data2.astype(np.float64)
data3 = data3.astype(np.float64)

rms_M1 = math.sqrt(np.mean(np.square(data1))); rms_M2 = math.sqrt(np.mean(np.square(data2))); rms_M3 = math.sqrt(np.mean(np.square(data3)))
print("RMS for M1 =",rms_M1,'\n'); print("RMS for M2 =",rms_M2,'\n'); print("RMS for M3 =",rms_M3,'\n')

#2) Highest RMS = closest to sound source -> M1
#3) Cross correlation: measure similarity between 2 signals

# corr = signal.correlate(m1, m2, mode='full')
# lags = signal.correlation_lags(len(data1), len(data2), mode='full')

# # Normalize correlation values
# corr /= np.max(np.abs(corr))
# print(corr)
# max_lag = lags[np.argmax(corr)]
# print(f"Maximum correlation at lag: {max_lag}")


#--------------

min_len = min(len(data1), len(data2)) #make both are same size arrays
x = data1[:min_len]
y = data2[:min_len]

N = len(x)
lags = range(-(N-1), N)  # all possible shifts
Rxy = []
for m in lags:
    if m >= 0:
        total = np.sum(x[m:] * y[:N-m])
    else:
        total = np.sum(x[:N+m] * y[-m:])
    Rxy.append(total)

Rxy = np.array(Rxy)

# Find the time delay
peak_index = np.argmax(Rxy)
time_delay_samples = lags[peak_index]
time_delay_seconds = time_delay_samples / m1

print(f"Time delay: {time_delay_samples} samples")
print(f"Time delay: {time_delay_seconds} seconds")

