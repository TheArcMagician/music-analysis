---

---

Note Frequency Detection Using HPS
=====
As I was looking for alternatives to peak frequency based detection, I came across a paper titled ["Efficient Pitch Detection Techniques for Interactive Music"](https://ccrma.stanford.edu/~pdelac/research/MyPublishedPapers/icmc_2001-pitch_best.pdf) by de la Cuadra and others. This paper describes a technique called Harmonic Product Spectrum (HPS).

Harmonics are essentially whole number multiples of a given frequency, if we had a pitch at 100Hz, its harmonics would be at 200Hz, 300Hz and so forth. This scheme takes the magnitudes of the FFTs at these frequencies and multiplies them together. It will then return us the frequency that results in the highest product.

I found sample code for implementing HPS [here](https://www.audiocontentanalysis.org/code/pitch-tracking/hps-2/). This code provides a function that takes as an input a spectrogram of the signal along with its sampling frequency. A spectrogram is a collection of FFTs over time. In Python it can be obtained from the [scipy signal processing library](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.spectrogram.html#scipy.signal.spectrogram).

So, I created [hpsfreq.py](https://github.com/shri-k/music-analysis/blob/master/src/hpsfreq.py) which takes the time series from the file that [wirefile.py](https://github.com/shri-k/music-analysis/blob/master/src/wirefile.py) writes to, and calls the HPS function in [hps.py](https://github.com/shri-k/music-analysis/blob/master/src/hps.py) to find the frequency with the highest harmonic product. It also plots a real time view of the spectrogram.

Using this program, I collected the following data using a keyboard on GarageBand:


| Piano Key     | Correct Frequency (Hz)| HPS Output (Hz)|
| ----------- | ----------- | ----------- |
| C4      | 262   |258* |
| D4 | 294 |290*|
| E4 | 330 | 333*|
| F4 | 349 | 344*|
| G4 | 392 | 387, 398*|
| A4 | 440 | 441|
| B4 | 494 | 495|
| C5 | 523 | 528|
| D5 | 587 | 592|
| E5 | 659 | 333, 656*|
| F5 | 698 | 699|
| G5 | 784 | 785|
| A5 | 880 | 883|
| B5 | 987 | 495|
| C6 | 1046 | 528, 1055*|

The above table shows two octaves that were tested with a piano keyboard using HPS. The entries marked with an asterisk showed a lot of random variations from the indicated number in the table. Some entries reflect that there were multiple commonly outputted frequencies. We can see in E5, B5, and C6 that the HPS output frequency is sometimes one octave below the correct frequency. The reason that there is slight differences between many of the correct and outputted frequencies is because of the limited resolution in the code.

To take this one step further, I created a dictionary mapping these frequencies to their corresponding letter notes and printed them. The updated file is [hpsdict.py](https://github.com/shri-k/music-analysis/blob/master/src/hpsdict.py).

Testing it using the keyboard in GarageBand, it was only able to somewhat identify the right letter notes (regardless of true frequency) around one octave.

So, HPS clearly is an improvement over peak frequency detection. However, there are still instances where the results are questionable in its current state.


Next step in the journey [here.](musicnet.md)
