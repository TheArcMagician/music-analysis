---

---

Note Frequency Detection Using Peak Frequency
=====
The next step for me, I thought, would be to see which individual frequency had the highest amplitude (and therefore was the most prominent). Using the previous fftanimate code, I added a few lines to identify the peak frequency. After looking for ways to [find the index of the max element of a numpy array,](https://thispointer.com/find-max-value-its-index-in-numpy-array-numpy-amax/) I came up with the following:
```python
   peak_index = np.where(fft_mag == np.amax(fft_mag))
   peak_freq = frequency[peak_index[0][0]]
   print(peak_freq)
```
So, I ran the modified program called [peakfreq.py](https://github.com/shri-k/music-analysis/blob/master/src/peakfreq.py) along with [wirefile.py](https://github.com/shri-k/music-analysis/blob/master/src/wirefile.py) to test this out on a 432Hz pure tone using this [youtube video.](https://www.youtube.com/watch?v=TxHctJZflh8) This was the result:

![pure tone](https://raw.githubusercontent.com/shri-k/music-analysis/master/the-journey/images/puretone.png)
While the number displayed in the terminal is not exactly 432, it is within the resolution of the FFT. 

So, with this I thought it was working perfectly.

That is until I tested this program on a piano keyboard from garageband on my phone, which produced the following:
![piano key](https://raw.githubusercontent.com/shri-k/music-analysis/master/the-journey/images/bflat.png)
This was supposed to show the frequency of the B flat above middle C (which is 466Hz). But unfortunately as the FFT plot shows, the harmonics of the keyboard interfered with this 'peak frequency' method. In particular, the peak frequency appears closer to 2800Hz.


Next step in the journey [here.](hps.md)
