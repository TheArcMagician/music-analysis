---

---

The Frequency Domain
=====

Before continuing further with audio processing, I wanted to explore ways to transform a time series into the frequency domain. The most common way to do this is by using the [Fast Fourier Transform (FFT).](https://en.wikipedia.org/wiki/Fast_Fourier_transform) I found a tutorial and python code [here](https://alphabold.com/fourier-transform-in-python-vibration-analysis/). It takes an arbitrary time signal consisting of two sinusoidal components and computes their FFT and presents both plots.

Below is the code presented with some minor modifications:

```python
"""
Illustrating how FFT works
from https://alphabold.com/fourier-transform-in-python-vibration-analysis/
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import pi
from scipy.fftpack import fft

#set sample rate and generate time array
sample_rate = 1024
max_time = 2
N = max_time * sample_rate
time = np.linspace(0, max_time, N)

#generate a time signal that is the sum of two sinusoids
freq1 = 100
a1 = 17
freq2 = 340
a2 = 6
waveform1 = a1 * np.sin (2 * pi * freq1 * time)
waveform2 = a2 * np.sin (2 * pi * freq2 * time)
time_signal = waveform1 + waveform2

#plot a portion of the time signal
plt.plot (time[0:100] , time_signal[0:100])
plt.title ('Time Domain Signal')
plt.xlabel ('Time')
plt.ylabel ('Amplitude')
plt.show ()

#generate the frequency array
frequency = np.linspace (0.0, sample_rate/2, int (N/2))

#take fft of the time signal and compute its magnitude
freq_data = fft(time_signal)
fft_magnitude = 2/N * np.abs (freq_data [0:np.int (N/2)])

#plot the magnitude of the fft
plt.plot(frequency, fft_magnitude)
plt.title('Frequency domain Signal')
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude')
plt.show()
```

Here is a plot of the time signal: 

![timeplot](https://raw.githubusercontent.com/TheArcMagician/music-analysis/master/the-journey/images/timeplot.png)


And here is the corresponding FFT plot: 
![fftplot](https://raw.githubusercontent.com/TheArcMagician/music-analysis/master/the-journey/images/fftplot.png)

Notice that this plot shows two distinct spikes, one at 100 Hz and another at 340 Hz. These directly correspond with the two waveforms I defined in the code.


Next step in the journey [here.](audiofft.md)
