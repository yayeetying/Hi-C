#Yaying Liang Li
#SoftDev
#K<02> -- Prepping - Create a Python program that prints a SoftDev student's name
#2021-09-23

import random

def printName():
   file_name = input("Input the .txt file containing the roster: ")
   my_file = open(file_name, "r")
   
   list_names = []
   #source: kite.com
   for line in my_file:
           line_list = line.split()
           list_names.append(line_list)
      
   my_file.close()

   print(" ".join(list_names[random.randint(0, len(list_names)-1)]))
   
   
printName();
