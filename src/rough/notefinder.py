import csv
import scipy.io.wavfile as wf
import numpy as np
import os

directory = os.getcwd() #'/home/sk/Downloads/musicnet/code'

for filename in os.listdir(directory+'/train_labels/'):
    if filename.endswith(".csv"):
        print(filename)
        sr, x = wf.read(directory+'/train_data/'+filename[:-3] + 'wav')

        with open(directory+'/train_labels/'+filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            file_list = list(csv_reader)
    
            brn = 0
            ctr = 0
            for i in range(1, len(file_list) - 2):
                if int(file_list[i][1]) > brn:
                    brn = int(file_list[i][1])

                if ((int(file_list[i+1][0]) >= brn) and (int(file_list[i+1][1]) <= int(file_list[(i+2)][0]))):
                    print(str(brn)+":"+str(i+1)+":" + str(file_list[i+1]))
                    l = file_list[i+1]
                    u = '_'
                    ctr = ctr + 1
                    l[6] = l[6].replace(' ','')
                    newwav = filename[:-4] + u + l[2] + u + l[3] + u + l[6]+ u + str(ctr)+'.wav'

                    pathname = directory + '/train_notes/' + '/note' + l[3] + '/'
                    fname = pathname+newwav
                    os.makedirs(os.path.dirname(fname), exist_ok=True)
                    wf.write(fname, sr, x[int(l[0]):int(l[1])])
    










