
# from -----------------------pandas library-------
#### data/data.csv -> 'original date', col1, col2
import pandas as pd
newData = pd.read_table('data/data.csv', sep=',') # , header=None
format_cols = ['original date','col1','col2']
newData = pd.read_table('data/data.csv', sep=',', names=format_cols) . # , header=None 
print(type(newData['col2']))  # -> pandas.core.series.Series
print(type(newData)) # pandas.core.frame.DataFrame
print(newData.describe())
print(newData.shape)
print(newData.dtypes)
print(newData.describe(include=['object']))
newData.columns
newData.rename(columns = {'original date':'New_Date','col1':'Col_1','col2':'Col_2'})
newData.rename(columns = {'original date':'New_Date','col1':'Col_1','col2':'Col_2'}, inplace=True)
newData.columns
oCols = ['original date','col1','col2']
newData.columns = oCols
print(newData.head())
#
newData2 = pd.read_table('data/data.csv', sep=',', names=format_cols, header=0) . # , header=None
newData2.columns
newData2.columns = newData2.columns.str.replace(' ', '_')
newData2.columns  # output is:   original date -> original_date 
newData2.shape
newData2.drop('col1',axis=1, inplace =True) 
newData2.drop([0,1] , axis=0, inplace=True)
type(newData2['col2'].sort_values())
newData2.sort_values('col2')
newData2.sort_values(['original_date','col2'])
type(False) # bool
booleans = [] 
    for length in newData2.col2:
        if length >= 400001:
	    booleans.append(True)
	else:
	    booleans.append(False)
print(booleans[0:5])
len(booleans) 
newData2[newData2.col2 >=  10000].original_date
newData2.loc[original_date >= 2010, 'col1']
True or False
True and False
newData2[newData2.col2 >= 400001 and newData2.original_date == '2010'] newData2[(newData2.col2 >= 400001) & (newData2.original_date == '2010')]
newData2[(newData2.col2 >= 400001) | (newData2.original_date == '2010') | (newData2.col1 >= 30)]
newData2[newData2.original_date.isin(['2010','2011'])]
