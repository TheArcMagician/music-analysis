---

---

PyAudio
=====

I began researching for a library that would enable input from a microphone as well as sound files. What I found was this: [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/). It implements a library for python that allows playing and recording of audio on many platforms.

I first used the provided examples for recording and playing a WAVE file.

Here is their example for playing a WAVE file:

```python
"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import sys

CHUNK = 1024

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()'
```
Other examples can be found in the above link to PyAudio.
