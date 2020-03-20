---

---

Note Frequency Detection Using HPS
=====
As I was looking for alternatives to peak frequency based detection, I came across a paper titled ["Efficient Pitch Detection Techniques for Interactive Music"](https://ccrma.stanford.edu/~pdelac/research/MyPublishedPapers/icmc_2001-pitch_best.pdf) by de la Cuadra and others. This paper describes a technique called Harmonic Product Spectrum (HPS).

Harmonics are essentially whole number multiples of a given frequency, if we had a pitch at 100Hz, its harmonics would be at 200Hz, 300Hz and so forth. This scheme takes the magnitudes of the FFTs at these frequencies and multiplies them together. It will then return us the frequency that results in the highest product. 

Next step in the journey [here.](dictionary.md)
