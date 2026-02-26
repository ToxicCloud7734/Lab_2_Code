from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

# Read audio file
fs, data = wavfile.read("M3.wav")

print("Original Sampling Frequency:", fs)
print("Number of original samples:", len(data))

t = np.arange(len(data)) / fs

plt.figure(figsize = (12,6))
plt.subplot(2,1,1)
plt.plot(t, data)
plt.title("Original Audio Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

target_fs = 8000
factor = fs // target_fs

print("Downsampling factor:", factor)

downsampled_data = data[::factor]
new_fs = fs // factor

print("New Sampling Frequency:", new_fs)
print("Number of samples after downsampling:", len(downsampled_data))

t_down = np.arange(len(downsampled_data)) / new_fs

plt.subplot(2,1,2)
plt.plot(t_down, downsampled_data)
plt.title("Downsampled Audio Signal (8 kHz)")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.tight_layout()

plt.show()