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
