#Yaying Liang Li, Raymond Yeung, Kevin Cao
#SoftDev
#K<05> -- Amalgamation of Python Random Name Generator Code
#2021-09-27

import random

def printName():
   names = {
      'pd1': ["Alejandro Alonso", "Aryaman Goenka", "Christopher Liu",
              "Deven Maheshwari", "Emma Buller", "Ella Krechmer",
              "Gavin McGinley", "Haotian Gan", "Ivan Lam", "Ishraq Mahid",
              "Ivan Mijacika", "Julia Nelson", "Lucas Lee", "Lucas Tom Wang",
              "Michelle Lo", "Oscar Wang", "Rayat Roy", "Renggeng Zheng",
              "Shriya Anand", "Shyne Choi", "Sadid Ethun", "Tomas Acuna",
              "Theodore Fahey", "Tina Nguyen", "Tami Takada", "William Chen",
              "Yusuf Elsharawy", "Zhaoyu Lin"],
      
      'pd2': ["Alif Abdullah", "Andrew Juang", "Andy Lin", "Austin Ngan",
              "Annabel Zhang", "Cameron Nelson", "David Chong",
              "Daniel Sooknana", "Eric Guo", "Eliza Knapp", "Hebe Huang",
              "Han Zhang", "Yoonah Chang", "Joshua Kloepfer", "Josephine Lee",
              "Mark Zhu", "Jonathan Wu", "Jesse Xie", "Justin Zou",
              "Kevin Cao", "Liesel Wong", "Michael Borczuk", "Noakai Aronesty",
              "Patrick Ging", "Qina Liu", "Roshani Shrestha", "Rachel Xiao",
              "Raymond Yeung", "Sophie Liu", "Shadman Rakib", "Thomas Yu",
              "Wenhao Dong", "Yaying Liang Li", "Yuqing Wu"]
   }

   #Find length of each list
   pd1_len = len(names['pd1'])
   pd2_len = len(names['pd2'])

   #Choose a random person
   num = random.randint(0, pd1_len + pd2_len - 1)
   if num < pd1_len:
      print("period1: " + names['pd1'][num])
   else:
      print("period2: " + names['pd2'][num - pd1_len])
   
   
printName();
