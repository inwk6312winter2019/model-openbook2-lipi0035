#Part 1

import csv

def count_accessible_busstops(csv1,csv2):
  count = 0
  street_csv = open(csv1)
  bus_csv = open(csv2)
  reader1 = csv.DictReader(street_csv)
  reader2 = csv.DictReader(bus_csv)
  street_fdmid = []
  bus_fdmid = []
  for row1 in  reader1:
    if(row1["ST_CLASS"].upper() == "ARTERIAL".upper()):
      street_fdmid.append(row1["FDMID"])
  for row2 in reader2:
    if(row2["ACCESSIBLE"].upper() == "Accessible".upper()):
      bus_fdmid.append(row2["FDMID"])
  for i in range(len(street_fdmid)):
    for j in range(len(bus_fdmid)):
      if(street_fdmid[i] == bus_fdmid[j]):  
        count = count+1 
  return count

cnt1 = count_accessible_busstops("Street_Centrelines.csv","Bus_Stops.csv")
print ("Number of bus Stops on ARTERIAL road which are Accessible are : {}".format(cnt1))

 
#Part 2

def count_nonstandard_busstops(csv1,csv2):
  count = 0
  street_csv = open(csv1)
  bus_csv = open(csv2)
  reader1 = csv.DictReader(street_csv)
  reader2 = csv.DictReader(bus_csv)
  street_fdmid = []
  bus_fdmid = []
  for row1 in  reader1:
    if(row1["ST_CLASS"].upper() == "LOCAL STREET".upper()):
      street_fdmid.append(row1["FDMID"])
  for row2 in reader2:
    if(row2["ACCESSIBLE"].upper() == "Non-Standard".upper()):
      bus_fdmid.append(row2["FDMID"])
  for i in range(len(street_fdmid)):
    for j in range(len(bus_fdmid)):
      if(street_fdmid[i] == bus_fdmid[j]):  
        count = count+1 
  return count

cnt2 = count_nonstandard_busstops("Street_Centrelines.csv","Bus_Stops.csv")
print ("Number of bus Stops on LOCAL STREET road which are Non-Standard are : {}".format(cnt2))

#Part 3

def count_inaccessible_busstops(csv1,csv2):
  count = 0
  street_csv = open(csv1)
  bus_csv = open(csv2)
  reader1 = csv.DictReader(street_csv)
  reader2 = csv.DictReader(bus_csv)
  street_fdmid = []
  bus_fdmid = []
  for row1 in  reader1:
    if(row1["ST_CLASS"].upper() == "MINOR COLLECTOR".upper()):
      street_fdmid.append(row1["FDMID"])
  for row2 in reader2:
    if(row2["ACCESSIBLE"].upper() == "Inaccessible".upper()):
      bus_fdmid.append(row2["FDMID"])
  for i in range(len(street_fdmid)):
    for j in range(len(bus_fdmid)):
      if(street_fdmid[i] == bus_fdmid[j]):  
        count = count+1 
  return count

cnt3 = count_inaccessible_busstops("Street_Centrelines.csv","Bus_Stops.csv")
print ("Number of bus Stops on MINOR COLLECTOR road which are Inaccessible are : {}".format(cnt3))
