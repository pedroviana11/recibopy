import pandas as pd

# Substitua pelo caminho completo e correto do arquivo
caminho_arquivo = "/home/pv-lds/Desktop/base.xlsx"

df = pd.read_excel(caminho_arquivo)

print(df)

oi = df.name

print(oi)