import pandas as pd 

df = pd.read_csv("vgsales.csv")

#Dataframe filtrado de GTA 5
df_gta5 = df[df["Name"] == "Grand Theft Auto V"]

#colunas de valores de venda que esta em milhões
df_gta5 = df_gta5[["NA_Sales","EU_Sales","JP_Sales","Other_Sales","Global_Sales"]]

#conversão do tipo de `str` para `float`

for col in ["NA_Sales","EU_Sales","JP_Sales","Other_Sales","Global_Sales"]:
    df_gta5[col] = df_gta5[col].apply(lambda value: float(value))

print(df_gta5)