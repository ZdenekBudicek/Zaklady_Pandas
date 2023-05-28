import pandas as pd

df1 = pd.DataFrame(1, index=[1, 3, 2, 4], columns=["a", "b", 1, 2])

print(df1.iloc[[0, 1], [0, 1]])  # vyfiltruje prvně 2 řádky a druhá závorka první 2 sloupce
print(df1.loc[:2])  # vypíše hodnoty po nějaký index řádku, hledá název ale ne pořadí!
print(df1.loc[:2, ["a", "b"]])  # Filtruje také sloupce ale musím psát jejich název

df = pd.DataFrame(1, index=["i", "j", "a", "b"], columns=["a", "b", 1, 2])
print(df.iloc[:3, :1])  # vyfiltruje první 3 řádky a druhá hodnota 1 sloupec
print(df.iloc[-2:-1, 1:3])  # Lze vypisovat i od zadu

df_real = pd.read_csv("dataset/train.csv")
print(df_real.head())
print(
    df_real.loc[~((df_real.SalePrice > 175000) & (df_real.SalePrice < 223500)), ["SalePrice", "YrSold"]])  # První zápis
print(df_real[~((df_real.SalePrice > 175000) & (df_real.SalePrice < 223500))][
          ["SalePrice", "YrSold"]])  # Druhá možnost zápisu
