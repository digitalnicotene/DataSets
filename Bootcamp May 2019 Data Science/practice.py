import panda as pd

df = pd.read_csv('pokemon.csv')
print(df.head(3)
print(df.tail(3)

df1 = pd.read_excel('pokemen.excel')

print(df.columns) // headers
df['name']
df['name','type]

df.iloc[1:4] // rows from 1 to 4

df.iloc[2,1] // second row first position

for index,row in df.iterrows():
	print(index,row) // show rows by index

for index,row in df.iterrows():
	print(index,row['Name'] // show name columns
	
df.loc[df['type 1] == 'fire'] //finding specific textual information

df.describe()  //mean and different stats

df.sort_values('name') // sort values by name


df.sort_values([name', 'hp'], ascending= False) // sort values by two columns


//Making Changes to DATA

df['Total'] = df['HP'] + df['attack'] +df['defense']// adding a total columns
df = df.drop(columns=['Total'])  /// drop a whole column

df['Total'] = df.iloc[:,4:10].sum(axis = 1) //adding totals

//axis = 0 adds vertically
//axis = 1 adds horizontally

cols = list(df.colums.values) //shows columns
df = df.[cols[0:4] + [cols[-1]] +col[4:12]] //changing columns

df = pd.to_csv('modified.csv') writing a new csv

//Filtering Data

df.loc[df['type 1'] == 'grass'] // finding specific values in a column by values
df.loc[(df['type 1'] == 'grass') & (df['type 1'] == 'poison')] //finding specific values in two diff columns

df.loc[df['name'].str.contains('Mega') // searches all words that contains 'mega'
df.loc[~df['name'].str.contains('Mega')// searches all words that do no contain 'mega'

import re ..regex expression

df.loc[df['type 1'].str.contains('Fire|Grass', regex = True)


df.loc[df['name'].str.contains('^pi[a-z]*', regex = True)

//Aggregrate Statistics Groupby

df.groupby(["Type 1"]).mean().sort_values('Defense', ascending=False) checking the mean of columns



df['count] = 1  //creating a new count column
df.groupby(['Type 1']).count()['count'] // shows the count column 

df.groupby(['Type 1', 'Type 2']).count()['count'] // shows the count column

 Use loc[] to choose rows and columns by label.
Use iloc[] to choose rows and columns by position.


old = nobel.nlargest(5,'age')  //finding age





 
