import pandas as pd
import sys, os
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
glosa_path = os.path.join(my_path, "../data/Glosa_Cuentas.csv")

# empty dictionary
ingresos_glosa_dict = {}

glosa = pd.read_csv(glosa_path)
glosa = glosa.iloc[1:13]
glosa.iloc[:, lambda glosa: [0, 2]]
glosa.to_csv('Glosa_Cuentas2.csv') # Export back to csv (with comma's)

#for i in range(len(df)) :
#    ingresos_glosa_dict[df.loc[i, "Nro_Cuenta"]] = df.loc[i, "Nombre_Cuenta"]
#    print(df.loc[i, "Nro_Cuenta"], df.loc[i, "Nombre_Cuenta"])
