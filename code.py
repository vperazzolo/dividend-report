#this is the file contaning the transformation code
import pandas as pd
import numpy as np

#import excel file
div_report = pd.read_excel("/Users/vbarros/Documents/Analysis/PythonProject/ProventosRecebidos.xlsx")

## Show all rows:
#pd.set_option("display.max_rows", None)
#print(div_report.head(50))


## Convert type (object to datetime) and format (MM/DD/YYYY to YYYY-MM-DD) of Data column.
div_report["Data"] = pd.to_datetime(div_report["Data"])

## Convert decimal delimiter "," to "." and type (object to float) of other value columns.
div_report = div_report.replace(",",".", regex=True)
div_report[["Valor Unitário (R$)", "Bruto Recebido (R$)", "IR (R$)", "Liquido Recebido (R$)"]] = div_report[["Valor Unitário (R$)", "Bruto Recebido (R$)", "IR (R$)", "Liquido Recebido (R$)"]].astype(float)
#print(div_report.dtypes)

## Just another way to replace values por column
#div_report["Valor Unitário (R$)"] = [x.replace(",",".") for x in div_report["Valor Unitário (R$)"]]


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


## Group "Data" columns by Year
div_report["Data"] = div_report["Data"].dt.strftime('%Y')

## Create pivot table
pivot = div_report.pivot_table(index="Papel", columns="Data", values="Liquido Recebido (R$)", aggfunc="sum", fill_value=0)#, margins=True, margins_name="Grand Total")

## Sort the pivot table column ("Data") in the descending level.
pivot = pivot.sort_index(axis=1, level=1, ascending=False)

## Pivot table calculation
pivot["Total"] = pivot.sum(axis="columns")
pivot["Mean"] = pivot.mean(axis="columns")
pivot["Median"] = pivot.median(axis="columns")
#pivot_total_year = pivot.sum(axis="index")

print(pivot)


#Next step -> Create vizualizations