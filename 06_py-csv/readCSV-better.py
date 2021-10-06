#Team Name: Hi-C; Yaying Liang Li, Andy Lin, Josephine Lee
#SoftDev
#K<06> -- Taking knowledge from other teams and implemenenting it here
#2021-10-06

import random, csv

def openFile():
    keys = ["Job Occupations", "Percentages"]
    #create new dict called info and initialize it with empty keys (no values in keys yet)
    info = dict.fromkeys(keys)
    
    with open('occupations.csv',mode='r') as csvfile: #open file for reading; we can refer to it as csvfile
        reader = csv.DictReader(csvfile) #reader is object of class csv
        for row in reader: #every row is a dict; format: {'Job Class': <xx>, 'Percentage': <yy>}
            print(row['Job Class'])
            #every row's 'Job Class' will be added to info under the key "Job Occupations"
            info["Job Occupations"] = row['Job Class']

    print(info)

openFile()
