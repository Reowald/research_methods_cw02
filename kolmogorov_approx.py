import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.plotting.register_matplotlib_converters()
from sklearn.model_selection import train_test_split

'''An approximation of conditional Kolmogorov complexity'''

# read CSV file in dataframe
news_data = pd.read_csv('compression_info.csv')


x = news_data['Original Size (bytes)']
y = news_data['Compressed Size (bytes)']


# create a new column to confirm the newspaper name
news_data['newspaper_name'] = news_data['File Name'].str.extract('(.*)_', expand=False)
# calculate approximation of conditional Kolmogorov complexity under a new column
news_data['kolmogorov_com'] = (x-y) -1
# calculate compression ratio under a new column
news_data['compression_ratio'] = (x/y)

# rename the columns
new_col_names = ['file_name', 'orig_size', 'com_size', 'paper_name', 'kol_com', 'com_ratio']
news_data.columns = new_col_names

# print dataframe details
print(news_data.columns)
print(news_data.dtypes)
print(news_data.shape)
print(news_data.head())
print(news_data.tail())
#print(news_data)


#Select size of plot to be produced
plt.figure(figsize=(10,4))
# Add title
plt.title("Average Compression Ratio Of Newspaper Articles Online")
# Bar chart showing average
sns.barplot(x='paper_name', y='com_ratio', data=news_data, palette="Set1", errorbar='sd', hue='paper_name', legend=False)
# Add label for vertical axis
plt.ylabel("Average Compression Ratio")
plt.xlabel("Newspaper Name")
plt.show()

plt.figure(figsize=(10,4))
plt.title("Total Number of Articles For Each Newspaper")
sns.countplot(data=news_data, x='paper_name', palette="Set1", hue='paper_name')
plt.ylabel("Total Number of Articles")
plt.xlabel("Newspaper Name")
plt.show()

#set the width and height of the figure
plt.figure(figsize=(14,7))
sns.scatterplot(x=news_data['paper_name'], y=news_data['kol_com'])
plt.show()

plt.figure(figsize=(14,7))
sns.scatterplot(x=news_data['paper_name'], y=news_data['com_ratio'])
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(data=news_data, palette="Set1")
plt.show()

#KDE PLot
sns.kdeplot(data=news_data, y='com_ratio', x='kol_com')
sns.kdeplot(data=news_data['com_ratio'], label="com ratio", fill=True)
sns.kdeplot(data=news_data['kol_com'], label="com ratio", fill=True)

# Add title and legend
plt.title("add details")
plt.show()
#plt.legend()

#BARPLOT - COUNTPLOT - SCATTERPLOT - BOXPLOT - KDEPLOT

#sns.countplot(x= 'income', data=Adult_data)

#X= Adult_data[COLUMNS]
#X.head()
#y = Adult_data.income
#y.head()

