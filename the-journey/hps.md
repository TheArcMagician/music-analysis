---

---

Note Frequency Detection Using HPS
=====
As I was looking for alternatives to peak frequency based detection, I came across a paper titled ["Efficient Pitch Detection Techniques for Interactive Music"](https://ccrma.stanford.edu/~pdelac/research/MyPublishedPapers/icmc_2001-pitch_best.pdf) by de la Cuadra and others. This paper describes a technique called Harmonic Product Spectrum (HPS).

Harmonics are essentially whole number multiples of a given frequency, if we had a pitch at 100Hz, its harmonics would be at 200Hz, 300Hz and so forth. This scheme takes the magnitudes of the FFTs at these frequencies and multiplies them together. It will then return us the frequency that results in the highest product. 


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

So, HPS clearly is an improvement over peak frequency detection. However, there are still instances where the results are questionable in its current state.

hps.py / hpsfreq.py

Next step in the journey [here.](dictionary.md)
