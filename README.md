# Desafio: Análise de Dados com Pandas
Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone. O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes. Isso representa uma perda de milhões para a empresa. O que a empresa precisa fazer para resolver isso?

Base de dados usada foi pega no Kaggle para fins de estudo. O Arquivo está disponível no projeto.
Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset 

Antes de iniciar o código, foi preciso entender o problema, e traçar uma rota para resolução do mesmo. Com os seguintes passos:

## Passo 1: Importar e Visualizar a base de dados
 - Entender quais as informações tão disponíveis
 - Descobrir o que não era útil na base de dados
## Passo 2: Tratamento de dados
 - Valores que estão reconhecidos de forma errada
 - Valores vazios
 - Excluir as colunas e linhas vazias
## Passo 3: Análise Inicial
 - Verificar se os dados do desafio estão corretos e se temos uma base grande o suficiente para a analise.
## Passo 4: Análise Mais completa
 - Comparar cada coluna da tabela com a coluna de cancelamento para identificar fatores relevantes.

# Conclusões e Ações

- Clientes com contrato mensal tem MUITO mais chances de cancelar.
  - Podemos fazer promoções para que o cliente migre para o contrato anual.

- Familias tendem a cancelar menos que clientes avulsos.
  - Podemos investir em promoções para linhas adicionais.

- Muitos clientes cancelam nos PRIMEIROS meses.
  - A primeira experiencia pode estar sendo ruim, devemos verificar isso.
  - Talvez a forma de captação possa estar trazendo clientes desqualificados.
  - Podemos criar bonus nos primeiros meses como incentivo para manter os clientes.

- Quanto MENOS serviços o cliente tem, MAIORES as chances de cancelamento.
  -Podemos criar combos de serviços, por valores similares ao serviço principal, aumentando a chance de reter os clientes.

- Há um problema claro no serviço de FIBRA.
  - É preciso identificar porque a fibra da empresa tem as maiores taxas de cancelamento, para poder agir sobre o problema.

- Clientes que pagam no BOLETO tem as maiores chances de cancelar.
  - Podemos criar descontos para as outras formas de pagamento.
