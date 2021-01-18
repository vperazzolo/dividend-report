#this is the file contaning the transformation code
import pandas as pd
import numpy as np
div_report = pd.read_excel("/Users/vbarros/Documents/Analysis/PythonProject/ProventosRecebidos.xlsx")
#print(div_report)

#find dates with "," and ", " and remove them.
wrong_date = div_report["Data"]
fix_date = wrong_date.str.contains(",")

div_report["Data"] = wrong_date.str.replace(",","")
div_report["Data"] = wrong_date.str.replace(" ","")

print(div_report["Data"].head(50))

#next step-> convert type  and format of Data column