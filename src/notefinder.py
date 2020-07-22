import csv

with open('1727.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        for x in row:
            y = 0
            z = 0
            if z != y:
                H = y
                print(H)
         #   else:
          #      print("no single notes found")
            y = row[0]
            z = y



#  print(y)

    #    if (row[0] == "9182"):
    #        print("X")
