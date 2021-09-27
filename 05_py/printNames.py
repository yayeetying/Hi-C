#Yaying Liang Li, Raymond Yeung, Kevin Cao
#SoftDev
#K<05> -- Amalgamation of Python Random Name Generator Code
#2021-09-24

import random

def printName():
   option = input("Input the number period's roster you want to access: ")
   if option == "1":
       file_name = "pd1.txt"
   elif option == "2":
       file_name = "pd2.txt"

   my_file = open(file_name, "r")
   
   list_names = []
   #source: kite.com
   for line in my_file:
           line_list = line.split()
           list_names.append(line_list)
      
   my_file.close()

   print(" ".join(list_names[random.randint(0, len(list_names)-1)]))
   
   
printName();
