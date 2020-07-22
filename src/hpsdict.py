"""hpsdict: loads time series from a file and generates and plots a spectrogram then prints its harmonic product spectrum frequency in Hz along with the corresponding letter note"""

# import needed packages
import matplotlib.pyplot as plt
import numpy as np
from hps import hps
from scipy import signal
import math

SAMPLES = 1024*8
time_series = np.zeros(SAMPLES)
frequency = np.linspace(0.0, 22050, int(SAMPLES/2))
fs = 44100

scaledict = {
   "C": 523,
   'C#': 554,
   "D": 587,
   'D#': 622,
   "E": 659,
   "F": 698,
   'F#': 739,
   "G": 784,
   'G#': 830,
   "A": 880,
   'A#': 932,
   'A#': 466,
   "B": 988,
   "B": 499,
   "C": 1055
}

def findmin(freq):
   cbnote = "C"
   cbfreq = 523
   for i,j in scaledict.items():
      if  abs(scaledict[i]-freq)<abs(cbfreq-freq):
          cbnote = i
          cbfreq = scaledict[i]
   return cbnote   
  
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

   #find the hps frequency and print it along with the note from the dictionary
   print(findmin(hps(Sxx, fs)[1]), hps(Sxx,fs)[1])




