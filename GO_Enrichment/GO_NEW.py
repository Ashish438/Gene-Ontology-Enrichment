import pandas as pd
import xlsxwriter

df=pd.read_excel("/home/arraygen/Desktop/GO_NEW/GO_enrichment_input.xlsx","DownRegulated")

#print(df[["Gene Symbol","GO Biological Process Term"]])

#print(df.columns)

#print(df[['Gene Symbol','GO Biological Process Term']])




sheet_col_name='GO Biological Process Term'

# FOR TOW COLUMNS
df_new=df[['Gene Symbol','GO Biological Process Term']]


data=df[sheet_col_name]
data.dropna(inplace = True)

#print(data)

data=data.str.replace(",GO","#").str.split("#")

data=pd.DataFrame(data)

l2=[]

# iterating over rows using iterrows() function
for i, j in data.iterrows():
    l1=j.tolist()
    for d in l1:
        for d1 in d:
            print(d1.split("~")[1].strip(","))
            l2.append(d1.split("~")[1].strip(","))
    print(i)
    print()


s1=set(l2)
print(len(s1))
print(len(l2))

l3=[]
for name in s1:
    t1=tuple((name,l2.count(name)))
    l3.append(t1)

#print(l3)

df_out=pd.DataFrame(l3)
df_sort=df_out.sort_values(by=1,ascending=False)


print(type(df_sort[0]))


# DROP NaN Value From #FOR TOW COLUMNS
df_new=df_new[df_new["Gene Symbol"].notnull()]
print(type(df_new))



# iterate over all the elements
for items in df_sort[0].iteritems():
    k,v=items
    print(k,v)



# iterating over rows using iterrows() function
for i, j in df_new.iterrows():
    print(i,j)
    print()

# Writing Data To Xlsx

workbook = xlsxwriter.Workbook('GO_Enrichment_Analysis.xlsx')

worksheet = workbook.add_worksheet(sheet_col_name)
bold = workbook.add_format({'bold': 1})


#print(data[0][0].split("~")[1])

headings = ['Term', 'Count']

worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', df_sort[0])
worksheet.write_column('B2', df_sort[1])

#######################################################################
#
# Create a new chart object.
#

chart1 = workbook.add_chart({'type': 'pie'})

cat_last_row=len(df_sort[0])
val_last_row=len(df_sort[1])

# Configure the series. Note the use of the list syntax to define ranges:
chart1.add_series({
    'name':       'Pie sales data',
    'categories': [sheet_col_name, 1, 0, 20, 0],
    'values':     [sheet_col_name, 1, 1, 20, 1],
    'data_labels': {'value': True},
})


# Add a title.
chart1.set_title({'name': sheet_col_name})

# Set an Excel chart style. Colors with white outline and shadow.
chart1.set_style(10)


# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('C2', chart1, {'x_scale': 2.5, 'y_scale':2.5})


workbook.close()
