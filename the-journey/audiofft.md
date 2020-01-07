---

---

FFT of Audio Signal
=====

Details.

```python
"""
Wirefile: record audio and keep saving samples to a file.
"""

import pyaudio
import numpy as np
import math


def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val


SAMPLES = 1024*8 #total number of samples
CHUNK = 1 #read audio from stream one sample at a time
CHANNELS = 1
RATE = 44100 #sample rate
RECORD_SECONDS = 1200  #maximum recording time

# start recording from microphone
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


#keep saving SAMPLES number of samples to file
time_series = np.zeros(SAMPLES)
counter = 0
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    currentVal = twos_comp(int.from_bytes(data, "little"),16)
    counter = counter+1
    time_series[counter%SAMPLES] = currentVal #store currentVal in time_series
    if counter%SAMPLES == SAMPLES-1:
       np.save('audio', time_series) #save SAMPLES number of samples to file



# close and terminate the microphone stream
stream.stop_stream()
stream.close()
p.terminate()


```

```python
"""
fftanimate: continuously reads audio from a numpy vector in a file and displays its fft as an animation.
"""

# import needed packages
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
from scipy.fftpack import fft

SAMPLES = 8192

fig = plt.figure()
fig.add_subplot(1,1,1)
plt.ion()
plt.show()

time_series = np.zeros(SAMPLES)
frequency = np.linspace(0.0, 22050, int(SAMPLES/2))

while True:
   try:
      time_series = np.load('audio.npy') #read from file
   except ValueError:
      pass
   # take fft and compute the magnitude
   freq_data = fft(time_series)
   fft_mag = 2/SAMPLES * np.abs( freq_data [0:int(SAMPLES/2)])

   # plot the fft, pause for a bit and then clear the plot
   plt.plot(frequency, fft_mag)
   plt.xlabel('frequency (Hz)')
   plt.ylabel('fft amplitude')
   axes = plt.gca()
   axes.set_ylim([0, 200])
   axes.set_xlim([0, 10000])
   plt.pause(0.01)
   plt.clf()
```
![gif](https://raw.githubusercontent.com/shri-k/music-analysis/master/the-journey/images/fftanimation.gif)
Next step in the journey [here.](peakfreq.md)

