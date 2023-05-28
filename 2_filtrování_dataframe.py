import pandas as pd

df = pd.read_csv("pandas_tutorial_sk-main/pandas_tutorial_sk-main/dataset/train.csv")
print(df.empty)  # Kontroluje jestli je data frame prázdny, True/False
print(df.ndim)  # řekne nám kolik má dimenzí, může jich mít víc, tento je 2, čili řádek a sloupec
print(df.size)  # Počet buněk
print(df.values)  # Vrátí nám 2 rozměrné pole v data typu numpy
print(pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"]))  # pandas series
print(df.dtypes)  # Vypíše typy sloupců
print(df.MSSubClass)  # Vypíše nám hodnoty daného sloupce (To za tečkou je název sloupce)
print(df[["MSSubClass", "MSZoning"]])  # To stejné jen tento zápis zvládne například i češtinu,
                                       # háčky čárky a nebo více sloupců najednou
print(df[df.SalePrice > 175000])  # Vyfiltruje například podle sloupce hodnoty nad 175 000
print(
    sum(df.SalePrice > 175000))  # boolean, vypíše u každého řádku True/False a pomocí sum nám spočítá kolik řádků to splňuje
# & - and | - or ~ - not
print(df[~((df.SalePrice > 175000) & (df.SalePrice < 223500))])
print(df[df.SalePrice.isin([175000, 250000])])
