'''Foi utilizado o Jupyter para codar, tendo em vista a facilidade que ele trás quando se trata de lidar com projetos de 
analise de dados. Também estou considerando que você já tenha todas as bibliotecas necessarias instaladas. Os passos estão descritos no README.'''

import pandas as pd
import plotly.express as px

# Passo 1
tabela = pd.read_csv("telecom_users.csv")
tabela = tabela.drop("Unnamed: 0", axis=1)
display(tabela)
print(tabela.info())

# Passo 2
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())

# Passo 3
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 4

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    grafico.show()

# Passo 5 (Conclusão, descrito no README)
