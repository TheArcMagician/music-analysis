---

---

Note Frequency Detection Using HPS
=====
As I was looking for alternatives to peak frequency based detection, I came across a paper titled ["Efficient Pitch Detection Techniques for Interactive Music"](https://ccrma.stanford.edu/~pdelac/research/MyPublishedPapers/icmc_2001-pitch_best.pdf) by de la Cuadra and others. This paper describes a technique called Harmonic Product Spectrum (HPS).

Harmonics are essentially whole number multiples of a given frequency, if we had a pitch at 100Hz, its harmonics would be at 200Hz, 300Hz and so forth. This scheme takes the magnitudes of the FFTs at these frequencies and multiplies them together. It will then return us the frequency that results in the highest product. 


| Piano Key     | Correct Frequency | HPS Output |
| ----------- | ----------- | ----------- |
| C4      | 262   | |
| D4 | 294 |
| E4 | 330 | 
| F4 | 349 | 
| G4 | 392 | 
| A4 | 440 | 
| B4 | 494 | 
| C5 | 523 | |
| D5 | 587 |
| E5 | 659 | 
| F5 | 698 | 
| G5 | 784 | 
| A5 | 880 | 
| B5 | 987 | 
| C6 | 1108 | |


Next step in the journey [here.](dictionary.md)
