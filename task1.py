import csv
#from collections import DictReader

#Part 1
def name_tuple():
  
  with  open('Street_Centrelines.csv',newline = '') as fin:
    reader = csv.DictReader(fin)
    for row in reader:
      print((row["STR_NAME"],row["FULL_NAME"],row["FROM_STR"],row["TO_STR"]))

name_tuple()

#Part 2

def hist_maintenance(csvfile):
  d = {}
  with open(csvfile,newline = '') as fin:
    reader = csv.DictReader(fin)
    for row in reader:
      m = row["MAINTENANCE"]
      d[m] = d.get(m,0)+1
  return d

main_dict = hist_maintenance("Street_Centrelines.csv")
print(main_dict)

#Part 3
def hist_own(csvfile):
  d = {}
  with open(csvfile,newline = '') as fin:
    reader = csv.DictReader(fin)
    for row in reader:
      m = row["OWN"]
      d[m] = d.get(m,0)+1
  return d

dict_own = hist_own("Street_Centrelines.csv")
print(list(dict_own))

#Part 4

def hist_st_class(csvfile):
  d = {}
  with open(csvfile,newline = '') as fin:
    reader = csv.DictReader(fin)
    for row in reader:
      l1 = []
      l2 = []
      k = row["ST_CLASS"]
      v = row["STR_NAME"]
      if(k not in d.keys()):
        l1.append(v)
        d[k] = l1
      else:
        l2 = d[k]
        l2.append(v)
        d[k] = l2
  return d

dict_st_class = hist_st_class("Street_Centrelines.csv")
print(dict_st_class)




