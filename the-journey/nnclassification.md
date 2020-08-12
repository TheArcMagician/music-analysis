---

---

Using a Neural Network to Classify Notes
=====

Next I wrote a script, [mwav2fft](https://github.com/shri-k/music-analysis/blob/master/src/mwav2fft.py) (multiple wav files to fft), to process a set of wav files corresponding to a note and output a collection of vectors containing their fft magnitude and the class label. The output is saved as a csv formatted file, such as this [example](https://github.com/shri-k/music-analysis/blob/master/src/class35.csv). Each row has 1024 elements for the fft coefficients and one element for the label. There are as many rows as there are wav files corresponding to that class.

Before using the above script, the wav files needed to be converted to 16 bit format using [sox](http://sox.sourceforge.net/)


By combining the csv files from two classes into train01.csv and test01.csv files it is now possible to train a neural network and test it out for binary note classification. This is done by the following code that I adapted from [this tutorial](https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/) on python based neural networks using the keras library.
```python
'''neuralnote.py: trains a neural network on data from two classes of notes and evaluates its accuracy'''
from keras.models import Sequential
from keras.layers import Dense
import numpy

                
# load training dataset
dataset_training = numpy.loadtxt("train01.csv", delimiter=",")
dataset_testing = numpy.loadtxt("test01.csv", delimiter=",")                

# split into input (X) and output (Y) variables
Xtrain = dataset_training[:,0:1024]
Ytrain = dataset_training[:,4096]
Xtest = dataset_testing[:,0:1024]
Ytest = dataset_testing[:,4096]
                

# create model
model = Sequential()
model.add(Dense(4, input_dim=1024, init='uniform', activation='relu'))
model.add(Dense(4, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

# compile model
model.compile(loss='binary_crossentropy' , optimizer='adam', metrics=['accuracy'])
                

# input the dataset into created model
model.fit(Xtrain, Ytrain, nb_epoch=30000, batch_size=10)


# evaluate the model
scores = model.evaluate(Xtest, Ytest)
print("the test results are:")
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
```
I compared the results classifying different pairs of notes at varying distances apart, and the following figure shows how it affects accuracy. ![figure](https://raw.githubusercontent.com/shri-k/music-analysis/master/the-journey/images/noteclassificationresults1.png) As the figure shows, the average accuracy was above 93 percent in all cases, and generally improves as the notes are farther apart. The noticeable dip in accuracy at a distance of 12 seems to be because that corresponds to an octave (so they are the same note, but different pitches).


Next step in the journey [here.]()
