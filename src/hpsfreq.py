"""hpsfreq: loads time series from a file and generates and plots a spectrogram then prints its harmonic product spectrum frequency in Hz"""

# import needed packages
import matplotlib.pyplot as plt
import numpy as np
from hps import hps
from scipy import signal

SAMPLES = 1024*8
time_series = np.zeros(SAMPLES)
frequency = np.linspace(0.0, 22050, int(SAMPLES/2))
fs = 44100

#prepare for plotting an animation
plt.ion()

while True:

   #load time series from file
   try: 
      time_series = np.load('audio.npy')
   except ValueError:
      pass
  
   #create the spectrogram
   f, t, Sxx = signal.spectrogram(time_series, fs, nperseg=4096)

   #plot the spectrogram  
   plt.pcolormesh(t, f, Sxx)
   plt.ylabel('Frequency [Hz]')
   plt.xlabel('Time [sec]')
   plt.show()
   plt.pause(0.01)
   plt.clf()

   #find the hps frequency and print it
   print(hps(Sxx,fs)[1])




