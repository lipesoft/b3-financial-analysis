def margem_liquida(df):
    df["margem_liquida"] = df["lucro"] / df["receita"]
    return df 


def crescimento_receita(df):
    df["crescimento_receita"] = df.groupby("empresa")["receitas"].pct_change()
    return df
    