import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import sounddevice as sd







t = np.linspace(0,3,12*1024)
x = (np.sin(2*np.pi*440*t)*(np.heaviside(t,1)-np.heaviside(t-0.4,1)))
x = x + (np.sin(2*np.pi*220*t)*(np.heaviside(t-0.5,1)-np.heaviside(t-0.5-0.3,1)))
x = x + (np.sin(2*np.pi*196*t)*(np.heaviside(t-1,1)-np.heaviside(t-1-0.25,1)))
x = x + (np.sin(2*np.pi*392*t)*(np.heaviside(t-1.5,1)-np.heaviside(t-1.5-0.1,1)))
x = x + (np.sin(2*np.pi*440*t)*(np.heaviside(t-2.5,1)-np.heaviside(t-2.5-0.75,1)))



fn1, fn2 = np.random.randint(0, 512, 2)
noise = np.sin(2*np.pi*fn1*t) + np.sin(2*np.pi*fn2*t)
xn = x + noise
N = 3*1024
f = np.linspace(0, 512, int(N/2))
xf = (2/N) * np.abs(fft(x)[0:int(N/2)])
xnf = (2/N) * np.abs(fft(xn)[0:int(N/2)])
peak = np.max(xf)
tmp = []
for i in range(0, len(xnf)):
 if xnf[i] > peak:
   tmp += [i]
fn1_dash, fn2_dash = round(f[tmp[0]]), round(f[tmp[1]])
x_filtered = xn - (np.sin(2 * np.pi * fn1_dash * t) + np.sin(2 * np.pi * fn2_dash * t))
xnff = (2/N) * np.abs(fft(x_filtered)[0:int(N/2)])







sd.play(x, 3*1024)
sd.play(x_filtered, 4*1024)
plt.subplot(3, 2, 1)
plt.plot(t, x)
plt.Ɵtle("Song")
plt.subplot(3, 2, 2)
plt.plot(t, xn)
plt.Ɵtle("Song_with_Noise")
plt.subplot(3, 2, 3)
plt.plot(f, xf)
plt.Ɵtle("Song_Frequency")
plt.subplot(3, 2, 4)
plt.plot(f, xnf)
plt.Ɵtle("Song_with_Noise_Frequency")
plt.subplot(3, 2, 5)
plt.plot(t, x_filtered)
plt.Ɵtle("Filtered Song")
plt.subplot(3, 2, 6)
plt.plot(f, xnff)
plt.Ɵtle("Filtered_Song_Frequency")