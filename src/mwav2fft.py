"""mwav2npy: read multiple wave files and append their fft to a single csv file, append also the class label to it"""


import wave
import sys
import numpy as np
import math
from scipy.fftpack import fft
import os



def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val

SAMPLES = 1024*8 #total number of samples
CHUNK = 1 #read audio from stream one sample at a time

classLabel = int(sys.argv[1]) 

directory = os.getcwd()

for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        wf = wave.open(filename, 'rb')
    else:
        continue


    time_series = np.zeros(SAMPLES)
    sum_fftmag = np.zeros(int(SAMPLES/2))
    counter = 0
    numfftcounter = 0
    fftTaken = False
    data = wf.readframes(CHUNK)
    while data != b'':
        currentVal = twos_comp(int.from_bytes(data, "little"),16)
        counter = counter+1
        time_series[counter%SAMPLES] = currentVal #store currentVal in time_series
        if counter%SAMPLES == SAMPLES-1:
           fftTaken = True
           # take fft and compute the magnitude
           freq_data = fft(time_series)
           fft_mag = 2/SAMPLES * np.abs( freq_data [0:int(SAMPLES/2)])
           sum_fftmag = sum_fftmag+fft_mag
           numfftcounter = numfftcounter + 1
        data = wf.readframes(CHUNK)

    if fftTaken == False:
        freq_data = fft(time_series)
        fft_mag = 2/SAMPLES * np.abs( freq_data [0:int(SAMPLES/2)])
        sum_fftmag = sum_fftmag+fft_mag
        numfftcounter = numfftcounter + 1

    avg_fftmag = sum_fftmag / numfftcounter
    f = open('class'+str(classLabel)+'.csv', 'ab')
    x = np.append(avg_fftmag, int(classLabel))
    np.savetxt(f, [x], delimiter=",", fmt='%d')
    f.close()
 



