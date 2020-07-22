---

---

Getting Note Samples from MusicNet
=====

I was interested in exploring the possibility of training a [neural network](https://en.wikipedia.org/wiki/Artificial_neural_network) to help with note detection. A key component in training a neural network is having access to a suitable dataset. While looking for somewhere that would have a large amount of samples for various notes, I came across [MusicNet](https://homes.cs.washington.edu/~thickstn/musicnet.html).
  
As noted on their [website](https://homes.cs.washington.edu/~thickstn/musicnet.html), "MusicNet is a collection of 330 freely-licensed classical music recordings, together with over 1 million annotated labels indicating the precise time of each note in every recording, the instrument that plays each note, and the note's position in the metrical structure of the composition." 

First I downloaded the [full repository](https://homes.cs.washington.edu/~thickstn/media/musicnet.tar.gz) consisting of more than 10 GB of wav files and annotations in csv format. Each csv file corresponds to one of the wav files and indicates at what times what notes are being played.

I wrote a script, [notefinder.py](https://github.com/shri-k/music-analysis/blob/master/src/rough/notefinder.py), to automate the process of pulling out samples of individual notes from each wav file. The output of this script is a collection of folders containing samples of each individual note. 

```python
"""notefinder: pulls out samples of individual notes from the MusicNet repository"""

import csv
import scipy.io.wavfile as wf
import numpy as np
import os

directory = os.getcwd() 

for filename in os.listdir(directory+'/train_labels/'):

    # the following code identifies each csv filename and reads the corresponding wav file
    if filename.endswith(".csv"):

        filenumber = filename[:-4] #number of the file
        
        #read music from the corresponding file
        sample_rate, music = wf.read(directory+'/train_data/'+filename[:-3] + 'wav')

        #the following opens the csv file and reads it
        with open(directory+'/train_labels/'+filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            file_list = list(csv_reader) #file_list is a list of lines read from the csv file
    
            brn = 0 # keeps track of the "biggest right number" i.e. largest ending time seen so far
            counter = 0 #counter to keep track of how many notes have been found, for the file name
            for i in range(1, len(file_list) - 2):

                #update brn to the highest ending time of a note seen so far
                if int(file_list[i][1]) > brn:
                    brn = int(file_list[i][1])

                line = file_list[i+1]  # read the next line

                #named variables corresponding to key elements in the line
                note_start_time = int(line[0])
                note_end_time = int(line[1])
                instrument = line[2]
                note_number = line[3]
                note_value = line[6].replace(' ','')  #remove spaces


                #to avoid picking up overlapping notes, check that this line corresponds to a note such that
                # its starting time is higher than brn, and also that its ending time is smaller than the 
                # next starting time
                if ((note_start_time >= brn) and (note_end_time <= int(file_list[(i+2)][0]))):

                    counter = counter + 1          

                    #name the output file based on original filename, instrument, note number, note value, and counter number
                    newwav = filenumber + '_' + instrument + '_' + note_number + '_' + note_value + '_' + str(counter)+'.wav'

                    pathname = directory + '/train_notes/' + '/note' + note_number + '/'
                    fname = pathname+newwav  #filename with the path for the detected note
                    # make the folder if it doesn't exist
                    os.makedirs(os.path.dirname(fname), exist_ok=True)

                    #write a wave file with the given file name that samples from the original music file accordingly
                    wf.write(fname, sample_rate, music[note_start_time:note_end_time])

```


Next step in the journey [here.](nnclassification.md)
