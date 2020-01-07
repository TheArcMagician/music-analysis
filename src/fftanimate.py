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




