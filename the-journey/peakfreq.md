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



Next step in the journey [here.](hps.md)
