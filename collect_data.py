import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming all your files are in the same directory as your script
# directory = r'C:\Users\ryand\Code\Data\Dataset News Articles\News Articles'
directory = r'C:\Users\ryand\Code\Data\Dataset News Articles\News Articles\compressed'

# Get a list of all files in the directory
files = [file for file in os.listdir(directory) if file.endswith('.txt.gz')]
# files = [file for file in os.listdir(directory) if file.endswith('.txt')]

# Initialize lists to store data
file_names = []
file_sizes = []

# Iterate through the files
for file in files:
    # Extract column label from the file name
    column_label = file.split('_')[0]
    
    # Get the file size
    file_size = os.path.getsize(os.path.join(directory, file))
    
    # Append data to lists
    file_names.append(column_label)
    file_sizes.append(file_size)

# Create a DataFrame
df = pd.DataFrame({'File': file_names, 'Size': file_sizes})

print(df.info)

# Plot using Seaborn scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='File', y='Size', hue='File', palette='viridis', s=100)
plt.title('File Sizes Scatter Plot')
plt.xlabel('File Label')
plt.ylabel('File Size (Bytes)')
plt.show()
