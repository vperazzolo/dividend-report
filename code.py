#this is the file contaning the transformation code
import pandas as pd
import numpy as np
div_report = pd.read_excel("/Users/vbarros/Documents/Analysis/PythonProject/ProventosRecebidos.xlsx")

#show all rows:
#pd.set_option("display.max_rows", None)
#print(div_report.head(50))

#Convert type (object to datetime) and format (MM/DD/YYYY to YYYY-MM-DD) of Data column.
div_report["Data"] = pd.to_datetime(div_report["Data"])


#Clean "Papel" column replacing additional information by the Ticker.

ticker = div_report["Papel"]
abev = ticker.str.contains("ABEV3")
bbas = ticker.str.contains("BBAS3")
cmig3 = ticker.str.contains("CMIG3")
cmig4 = ticker.str.contains("CMIG4")
elpl = ticker.str.contains("ELPL4")
geti = ticker.str.contains("GETI3")
itsa = ticker.str.contains("ITSA4")
itub = ticker.str.contains("ITUB4")
ligt = ticker.str.contains("LIGT3")
petr = ticker.str.contains("PETR4")
taee = ticker.str.contains("TAEE11")
tiet = ticker.str.contains("TIET11")
trpl = ticker.str.contains("TRPL4")

div_report["Papel"] = np.where(abev, 'ABEV3',
                      np.where(bbas, 'BBAS3',
                      np.where(cmig3, 'CMIG3',
                      np.where(cmig4, 'CMIG4',
                      np.where(elpl, 'ELPL4',
                      np.where(geti, 'GETI3',
                      np.where(itsa, 'ITSA4',
                      np.where(itub, 'ITUB4',
                      np.where(ligt, 'LIGT3',
                      np.where(petr, 'PETR4',
                      np.where(taee, 'TAEE11',
                      np.where(tiet, 'TIET11',
                      np.where(trpl, 'TRPL4',
                      ticker.str.replace(" ", ""))))))))))))))



#Group "Data" columns by Year
div_report["Data"] = div_report["Data"].dt.strftime('%Y')

#Creating the pivot table
pivot = div_report.pivot_table(index="Papel", columns="Data", values="Liquido Recebido (R$)", aggfunc="first", fill_value=0)
print(pivot)

#Next step -> Change order of columns in pivot table and check values