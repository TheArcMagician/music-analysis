'''multinoteclassify: trains a multi-class neural network using musical note data and evaluates the classification accuracy as the number of classes increases from 2 to 13'''
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
                
                
# starting and ending notes that have at least 1000 samples
start = 62
end = 79 

# open file to save results in
f = open('output_multi.txt', 'w')

for start_note in range(start, end , 1):
    for num_classes in range(2,13,1):
        if start_note+num_classes-1 > end:
           break
        print(start_note, num_classes)

        # setup training and testing values using the first class
        dataset = np.loadtxt("class"+str(start_note)+".csv", delimiter=",")
        Xtrain = dataset[0:1000,0:1024]
        e = np.zeros((1, num_classes))
        e[0,0] = 1
        Ytrain = np.tile(e, (1000,1))
        Xtest = dataset[-100:,0:1024]
        Ytest = np.tile(e, (100,1))

        # setup training and testing values using the remaining classes
        counter = 1
        while counter < num_classes: 
            dataset = np.loadtxt("class"+str(start_note+counter)+".csv", delimiter=",")
            Xtrain = np.concatenate((Xtrain, dataset[0:1000,0:1024])) 
            e[0, counter-1] = 0
            e[0, counter] = 1
            Ytrain = np.concatenate((Ytrain, np.tile(e, (1000,1)) ))
            Xtest = np.concatenate((Xtest, dataset[-100:,0:1024])) 
            Ytest = np.concatenate((Ytest, np.tile(e, (100,1)) ))
            counter = counter+1

        # create model
        model = Sequential()
        model.add(Dense(8, input_dim=1024, init='uniform', activation='relu'))
        model.add(Dense(8, init='uniform', activation='relu'))
        # use softmax for the output layer
        model.add(Dense(num_classes, init='uniform', activation='softmax'))

        # compile model
        model.compile(loss='categorical_crossentropy' , optimizer='adam', metrics=['accuracy'])
                

        # train the model using the training data
        model.fit(Xtrain, Ytrain, nb_epoch=300, batch_size=10)
        # save the model to file (optional)
        model.save("model"+str(start_note)+"_"+str(num_classes))
                

        # evaluate the model
        scores = model.evaluate(Xtest, Ytest)
        print("comparing "+str(num_classes)+"classes starting from "+str(start_note))
        print("the test results are:")
        print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
        f.write("%d, %d, %.2f\n" % (num_classes, start_note, scores[1]*100))

f.close()

