import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import os
from scipy import stats

from IPython.display import IFrame

data = os.path.join('data','avndviRaintemp.csv')




df=pd.read_csv(data);

print df.tail()
print df.columns


df = df[['Ave_NDVI', 'Rainfal']]
print df.head()


df.corr()

print stats.pearsonr(df.Ave_NDVI, df.Rainfal)





plt.figure(figsize=(8,8))
seaborn.heatmap(df.corr(), annot=True, cmap="coolwarm").set_title('Seaborn')

plt.imshow(df.corr(), cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(df.columns)), df.columns, rotation=90)
plt.yticks(range(len(df.columns)), df.columns)
plt.gcf().set_size_inches(8,8)

labels = df.corr().values
for y in range(labels.shape[0]):
    for x in range(labels.shape[1]):
        plt.text(x, y, '{:.2f}'.format(labels[y, x]), ha='center', va='center', color='white')

