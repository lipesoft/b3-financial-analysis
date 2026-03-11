import matplotlib.pyplot as ptl 

 def grafico_receita(df, empresa):
    dados = df[df["empresa"] == empresa]

    plt.figure()
    
    plt.plot(dados["ano"], dados["receita"])

    ptl.title(f"Receita ao longo do tempo - {empresa}")

    plt.xlabel ("Ano")
    plt.ylabel ("Receita")

    plt.show()