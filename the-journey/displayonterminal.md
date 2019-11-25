---

---

Displaying the Signal in a Terminal
=====

Just for fun, I wanted to see a real time visual of the audio signal from the microphone. The following code is modified from the wire.py provided as an example by PyAudio. In order to show the audio values, I scaled it down by a factor of ten and used the [ansi color standard for terminals.](https://bixense.com/clicolors/)

Below is the code:
```python
"""
Terminal Display: show the time series from microphone in the terminal

"""

import pyaudio
import numpy as np
import math


def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val


CHUNK = 1
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 60

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

#ANSI colors from https://bixense.com/clicolors/
colorString = '\x1b[6;30;42m'
colorReset = '\x1b[0m'

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    currentVal = twos_comp(int.from_bytes(data, "little"),16)
    print(colorString + (int(abs(currentVal)/10))*" "+ colorReset)

stream.stop_stream()
stream.close()

p.terminate()
```
Here is a screenshot showing the terminal
![Terminal Disp](https://raw.githubusercontent.com/TheArcMagician/music-analysis/master/the-journey/images/termdisp.png)


Next step in the journey [here.](freqdomain.md)
