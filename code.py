#this is the file contaning the transformation code
import pandas as pd
import numpy as np
div_report = pd.read_excel("/Users/vbarros/Documents/Analysis/PythonProject/ProventosRecebidos.xlsx")
#print(div_report.head(50))

#find dates with "," and ", " and remove them. (Can be skipped once to_datetime function automatically does that)
wrong_date = div_report["Data"]
fix_date = wrong_date.str.contains(",")
div_report["Data"] = wrong_date.str.replace(",","")
div_report["Data"] = wrong_date.str.replace(" ","")

#Convert type (object to datetime) and format (MM/DD/YYYY to YYYY-MM-DD) of Data column.
div_report["Data"] = pd.to_datetime(div_report["Data"])


print(div_report["Data"].head(50))