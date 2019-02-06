#Part 1
import csv

def count_accessible_busstops(csv1,csv2):
  count = 0
  with open(csv1,newline = '') as fin1:
    reader1 = csv.DictReader(fin1)
    with open(csv2,newline = '') as fin2:
      reader2 = csv.DictReader(fin2)
      for row1 in reader1:
        if(row1["ST_CLASS"] == "ARTERIAL"):
          for row2 in reader2:
            if(row2["ACCESSIBLE"] == "Accessible" and row1["FDMID"] == row2["FDMID"]):
              count = count+1 
  return count

cnt1 = count_accessible_busstops("Street_Centrelines.csv","Bus_Stops.csv")
print(cnt1)

#Part 2

def count_nonstandard_busstops(csv1,csv2):
  count = 0
  with open(csv1,newline = '') as fin1:
    reader1 = csv.DictReader(fin1)
    with open(csv2,newline = '') as fin2:
      reader2 = csv.DictReader(fin2)
      for row1 in reader1:
        if(row1["ST_CLASS"].upper() == "LOCAL STREET".upper()):
          for row2 in reader2:
            if(row2["ACCESSIBLE"].upper() == "Non-Standard".upper()):
              if(row2["FDMID"] == row1["FDMID"]):
                count = count+1 
  return count

cnt2 = count_nonstandard_busstops("Street_Centrelines.csv","Bus_Stops.csv")
print(cnt2)

#Part 3

def count_inaccessible_busstops(csv1,csv2):
  count = 0
  with open(csv1,newline = '') as fin1:
    reader1 = csv.DictReader(fin1)
    with open(csv2,newline = '') as fin2:
      reader2 = csv.DictReader(fin2)
      for row1 in reader1:
        if(row1["ST_CLASS"] == "MINOR COLLECTOR"):
          for row2 in reader2:
            if(row2["ACCESSIBLE"] == "Inaccessible" and row2["FDMID"] == row1["FDMID"]):
              count = count+1 
  return count

cnt3 = count_inaccessible_busstops("Street_Centrelines.csv","Bus_Stops.csv")
print(cnt3)

