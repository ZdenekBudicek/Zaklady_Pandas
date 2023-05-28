import pandas as pd
import numpy as np

# Pomocí tuple uděláme multiindex
df = pd.DataFrame(
    data={
        ("player1", "x"): np.arange(2, 7),  # np arrage je range v kniznici numpy
        ("player1", "y"): np.arange(2, 7),
        ("player2", "x"): np.arange(2, 7),
        ("player2", "y"): np.arange(2, 7),
    },
    index=[("player1", "x"), ("player1", "x"), ("player1", "x"), ("player1", "x"), ("player1", "x")]
)
print(df)

# Nová úroveň nad sloupci
print(df.columns)

# Index je reprezentovany v tuples
print(df.index)

# Přístup na jednotlivou úroveň
print(df["player1"]["x"])

# Přístup na jednotlivou úroveň pomocí loc (iloc je na tom podobne)
print(df.loc[:, ("player1", "x")])

# Změna hodnoty pomocí loc
df.loc[:, ("player1", "x")] = 1
print(df)

# Vytvoření pomocí slovníku
df = pd.DataFrame(data={"a": np.arange(1, 10), "b": np.arange(10, 19)})
print(df)

# Tvorba nového sloupce pomocí závorek
df["c"] = np.arange(20, 29)
print(df)

# Přidání pomocí kombinování sloupců
# (a+b)**2
df["d"] = (df["a"] + df["b"]) ** 2
print(df)

# Přídání řádku pomocí locu, pomocí indexu
# Musí sedět počet sloupců
df.loc[9] = [0, 1, 2, 3]
print(df)

# Ukázka indexu kombinováním datovych typů
df.loc["bla"] = [0, 1, 2, 3]
print(df)

print(df.shape[0])

# Odstraňování sloupců pomocí columns difference
print(df.loc[:, df.columns.difference(["c"])])

print(df)

# Mazání sloupce pomocí drop
df.drop("c", axis=1, inplace=True)

# Mazaní řádku pomocí drop a hodnoty indexu
# inplace operace upraví původní dataframe
df.drop("bla", axis=0, inplace=True)

print(df)

# Mazání pomocí podmínky
df.drop(df[(df.a >= 4) & (df.a <= 6)].index, axis=0, inplace=True)
print(df)
