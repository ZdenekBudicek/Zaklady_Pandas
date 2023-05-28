import pandas as pd

df_train = pd.read_csv("dataset/train.csv")
df_test = pd.read_csv("dataset/test.csv",
                      index_col="Id",  # index_col nastaví co je index(jaký sloupec)
                      sep=",",  # sep podle čeho má dělit ty data, v tomto případě podle čárky
                      # skiprows=3 # jaký řádek má vynechat, nesmí být zaplé index_col aby toto šlo, takže zakomentovat
                      )
print(df_test)  # vyprintuje prvních 5 řádků a 5 posledních řádků, nepoužívat na velké množství dat
print(df_test.head())  # vyprintuje prvních 5 řádků
print(df_test.tail())  # vyprintuje posledních 5 řádků, lepší na velké objemy dat, nemusí je celé načítat
print(df_test.shape)  # Vypíše počet řádků a počet sloupců v souboru
print(df_test.axes)  # vypíše co je X osa a co je Y osa, zde například X je jen RangeIndex a jede od 0 až po 1459
# Y jsou zde názvy sloupců
print(df_train.columns)  # Vypíše mi všechny názvy sloupců
df_train.set_index("Id")  # Nastaví že Index je ID (to stejné co výše jen jinak)
