#Incomplete - trying to change the weights to numbers, but prob lies in floating
#strings that have commas ('cause of the way I split them)

#Yaying Liang Li
#SoftDev
#K<06> -- Reading CSV Files
#2021-09-28

import random

def read_file():
    all_jobs = {}
    
    with open("occupations.txt", "r") as my_file:
        lines = my_file.read().splitlines() #lines is a list
        for line in lines:
            if '"' in line: #some lines contain quote marks...
                listo = line.split('"') #listo is a list
            else: #other lines just have commas, so let's split them by that!
                listo = line.split(",")

            #ignore the header + total lines; credits to Andy
            if listo[0] != "Job Class" and listo[0] != "Total":
                if listo[0] != "": #if listo[0] is the actual occupation
                    all_jobs[listo[0]] = float(listo[len(listo)-1])
                else: #if listo[0] is just "" (nothing) :(
                    all_jobs[listo[1]] = float(listo[len(listo)-1])
                    
        print(random.choices(all_jobs.keys(),
                             weights = all_jobs.values(),
                             k=1))

read_file();
