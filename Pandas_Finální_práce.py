import pandas as pd
import numpy as np
import seaborn as sns
import warnings
import matplotlib
import matplotlib.pyplot as plt


# NAČÍTÁNÍ DAT
files = ['dataset\\test.csv', 'dataset\\train.csv']

df_list = []

for file in files:
    temp_df = pd.read_csv(file)
    df_list.append(temp_df)

df = pd.concat(df_list, axis=0, ignore_index=True)

# KONTROLA DATOVÝCH TYPŮ
print(df.dtypes)
numeric_columns = df.dtypes[df.dtypes != np.object_].index.to_list()
print(numeric_columns)
string_columns = df.dtypes[df.dtypes == np.object_].index.to_list()
print(string_columns)
print(df.loc[:, string_columns].head())
print(df.Street.value_counts())

# KONTROLA NAN HODNOT
nan_counts = df.isna().sum()
nan_counts_sorted_df = nan_counts.loc[nan_counts > 0].sort_values(ascending=False).to_frame(name="counts")
print(nan_counts_sorted_df)

# Výpočet procent
nan_counts_sorted_df["percentage"] = (nan_counts_sorted_df["counts"] / df.shape[0]) * 100
print(nan_counts_sorted_df)

# ANALÝZA obecná
print(df.loc[:, numeric_columns].head())
print(df.describe())

print(df.loc[:, string_columns].describe())

# počet nan hodnot ve sloupci SalePrice
print(df.SalePrice.isna().sum())
df = df.loc[df.SalePrice.notna(), :]
print(df.shape)

# Graf sloupce SalePrice
df['SalePrice'].plot.hist(bins=50)
plt.show()

# Výpočet korelace pro SalePrice
print(df.loc[:, numeric_columns].corr()["SalePrice"].sort_values())

# Korelační matice
plt.rcParams['figure.figsize'] = 20, 15
dic = {"size": 14}
matplotlib.rc('font', **dic)
x = df.loc[:, numeric_columns]
alpha = x.corr().columns
plt.rcParams["axes.grid"] = False

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(x.corr(method='pearson'), cmap=plt.cm.coolwarm, vmin=-1, vmax=1)
fig.colorbar(cax)

plt.xticks(rotation='vertical')
ax.set_xticks(np.arange(len(alpha)))
ax.set_yticks(np.arange(len(alpha)))
ax.set_xticklabels([' '] + alpha)
ax.set_yticklabels([' '] + alpha)
ax.tick_params(labelsize=18)
plt.show()

# Jak analyzovat string atributy
plt.rcParams['figure.figsize'] = 10, 6
dic = {"size": 10}
matplotlib.rc('font', **dic)

df.boxplot(column=["SalePrice"], by="MSZoning")
plt.show()

# používání pairplot
warnings.filterwarnings("ignore")
df_numeric = df.loc[df.SalePrice.notna(), numeric_columns[1:10] + ["SalePrice"]]
sns.pairplot(df_numeric, hue='SalePrice')
plt.show()
