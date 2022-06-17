from traceback import print_tb
import pandas as pd
import csv

ingresos_dict = {}
prev_p = ""

with open('Ingresos.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
      if row[0].startswith('NOMBRE DEL CANDIDATO'):
        continue
      politico, partido, plata = row
      plata = plata.replace(",", "")
      try:
        plata = int(plata)
      except:
        plata = 0
      # print(plata)
      #print(politico)
      if(politico == prev_p):
        ingresos_dict[politico] = int(plata) + ingresos_dict[politico]

      else:
        ingresos_dict[politico] = int(plata)

      prev_p = politico
    
    #print(ingresos_dict)

with open('Ingresos.csv','r') as in_file, open('ouput.csv','w') as out_file:
  
    reader = csv.reader(in_file, delimiter=',')

    seen = set() # set for fast O(1) amortized lookup
    
    for row in reader:
        if row[0].startswith('NOMBRE DEL CANDIDATO'):
            continue
        politico = row[0]
        #print(politico)
        if politico in seen: 
          continue # skip duplicate

        seen.add(politico)
        row[2] = ingresos_dict[politico]
        print(row)
        out_row = row[0]+","+row[1]+","+str(row[2])+"\n"
        print(out_row)
        out_file.write(out_row)
