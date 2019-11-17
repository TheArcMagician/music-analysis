---

---

Plotting The Time Signal
=====

After becoming aquainted with the PyAudio library, I tried to create a plot of the time signal from a .wav file. I started with the example from PyAudio to play a .wav file and had to modify to do the following:
* Create numpy array to store the time signal data
* Transform the audio data from 2's complement to integers
* Use matplotlib to plot the time signal data

Here is the code:
```python
"""Play a WAVE file and plot its time signal."""

# import needed packages
import pyaudio  # importing pyaudio library
import wave     # import library to be able to read/write wav files
import sys      # import "sys" library to be able to read command line arguments
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


N = 220160  # number of samples in 5 second audio
RATE = 44100 # sample rate of WAV file
CHUNK = 1 #number of chunks to load from file at a time

time_series = np.zeros(N)
time = np.linspace(0.0, N/RATE, N)

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val


if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)
#above to check if file name was not given

wf = wave.open(sys.argv[1], 'rb')
#above to open the given file name

p = pyaudio.PyAudio()
#p is a class from PyAudio that creates an audio stream to play on speaker

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

counter = 0
while counter*CHUNK < N:
    data = wf.readframes(CHUNK)
    stream.write(data)
    currentVal = twos_comp(int.from_bytes(data, "little"),16)
    time_series[counter] = currentVal
    counter = counter+1

stream.stop_stream()
stream.close()
p.terminate()


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
plt.plot(time, time_series)
plt.xlabel('time (s)')
plt.ylabel('audio signal')
plt.show()
```
Here is the resulting plot:










Next step in the journey [here.](displayonterminal.md)
