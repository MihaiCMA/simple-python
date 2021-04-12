
# Program extracting first column
import xlrd
 
loc = ("path")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

pairs = []

for i in range(2,sheet.nrows):
    pairs.append([sheet.cell_value(i, 2),sheet.cell_value(i, 0),"Salutare, te rog sa semnezi urmatorul document! Merci!"])

for i in pairs:
   for j in i:
       if (bool(j)==False):
           pairs.remove(i)
           break
       

import xlsxwriter
# Some data we want to write to the worksheet.
# splitting pairs
l=[pairs[i:i + 5] for i in range(0, len(pairs), 5)]

# Start from the first cell. Rows and columns are zero indexed.

for pair in l:
    # Create a workbook and add a worksheet.
    
    workbook = xlsxwriter.Workbook('Voluntari'+ str(l.index(pair)+1) +'.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0
    pair.insert(0,['_es_signer_email', '_es_signer_fullname','_es_agreement_message'])
    # Iterate over the data and write it out row by row.
    for item, cost, trueness in (pair):
        worksheet.write(row, col,     item)
        worksheet.write(row, col + 1, cost)
        worksheet.write(row, col + 2, trueness)
        row += 1


    workbook.close()
