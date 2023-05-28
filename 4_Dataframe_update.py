import pandas as pd

df = pd.read_csv("dataset/train.csv")
df.MSZoning = 1  # Přepíše všechny hodnoty ve sloupci MSZoning na 1
print(df)
df.MSZoning = pd.Series(list(range(0, 1460)))  # Přepíše hodnoty od nuly až po tisíc ve sloupci MSZoning
print(df)

df.loc[
    df.SalePrice > 181500, "SalePrice"] = 10  # Přepíše hodnoty na 10 v sloupci SalePrice kde je hodnota větší než 181500
print(df)

print(df.loc[(df.SalePrice > 170000) & (df.MSSubClass > 30), :])  # Správné filtrování
