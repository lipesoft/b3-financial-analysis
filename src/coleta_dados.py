import pandas as pd

def carregar_dados():
    df = pd.read_csv("data/dados_empresas.csv")
    return df
    