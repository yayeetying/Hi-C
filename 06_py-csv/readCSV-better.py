#Team Name: Hi-C; Yaying Liang Li, Andy Lin, Josephine Lee
#SoftDev
#K<06> -- Taking knowledge from other teams and implemenenting it here
#2021-10-06

import random, csv

def openFile():
    info = {} #create new dict called info
    
    with open('occupations.csv',mode='r') as csvfile: #open file for reading; we can refer to it as csvfile
        reader = csv.DictReader(csvfile) #reader is object of class csv
        for row in reader: #every row is a dict; format: {'Job Class': <xx>, 'Percentage': <yy>}
            #for first row in file, create key-value pair in info with format: 'Job Class': <xx>, 'Percentage': <yy>
            #key is 'Job Class'; value is 'Percentage'
            #for every other row, update existing key-value pair to include new value given
            info[row['Job Class']] = float(row['Percentage'])

    #keys = list(info.keys())
    #weights = info.values();

    #make a randomized, weighted choice
    #population are the occupations, weights are the percentages they should show up
    result = random.choices(list(info.keys()), weights = info.values(), k=1)
    print(result)

openFile()
