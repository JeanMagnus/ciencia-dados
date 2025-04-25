# 🔥 Análise Inicial do Dataset "Forest Fires in Brazil"

## 📌 Introdução

O presente trabalho tem como objetivo a análise do dataset *Forest Fires in Brazil*, que contém registros oficiais de focos de incêndios em todos os estados brasileiros entre os anos de 1998 e 2017. Os dados foram coletados e disponibilizados pelo INPE (Instituto Nacional de Pesquisas Espaciais) e estão acessíveis na plataforma Kaggle.

A análise de incêndios florestais é de extrema importância, especialmente no contexto brasileiro, onde biomas como a Amazônia e o Cerrado sofrem intensamente com queimadas ilegais e desmatamento. Investigar padrões temporais, sazonais e geográficos desses eventos pode apoiar políticas públicas de preservação ambiental, identificar regiões críticas e auxiliar na tomada de decisão de órgãos ambientais.

---

## 🧾 Sobre o Dataset

O arquivo utilizado tem o nome `amazon.csv` e contém 6.454 registros. Cada linha representa a ocorrência de incêndios em um estado brasileiro em determinado mês e ano.

As colunas presentes no dataset são:

| Coluna  | Tipo     | Descrição |
|---------|----------|-----------|
| `year`  | Numérico | Ano do registro do incêndio |
| `state` | Texto    | Estado brasileiro onde o incêndio ocorreu |
| `month` | Texto    | Mês do registro do incêndio |
| `number`| Numérico | Número de focos de incêndio registrados |
| `date`  | Texto    | Combinação do mês e ano no formato `mm/yyyy` |

---

## 🛠️ Verificação de Dados Faltantes

Para garantir a integridade das análises futuras, foi realizada uma inspeção inicial para identificar a presença de valores ausentes no dataset. Abaixo, segue o código utilizado em Python (utilizando a biblioteca `pandas`):

```python
import pandas as pd

# Carregar o dataset com encoding adequado
df = pd.read_csv('amazon.csv', encoding='latin1')

# Verificar a quantidade de valores ausentes por coluna
print(df.isnull().sum())

```

## 📈 Resultado obtido


A análise preliminar mostra que nenhuma coluna do dataset apresenta valores ausentes. Isso é extremamente positivo, pois elimina a necessidade de técnicas de imputação ou exclusão de dados. A consistência do dataset permite avançar diretamente para etapas mais complexas, como visualização, agrupamentos e análises estatísticas, sem prejuízo de qualidade ou necessidade de tratamento para ausência de dados.

## 🔍 Possíveis Análises Futuras
Com base na estrutura do dataset, diversas análises podem ser realizadas, tais como:

- Tendência temporal: evolução dos incêndios florestais ao longo dos anos;

- Distribuição mensal: identificação de padrões sazonais na ocorrência dos focos;

- Comparação geográfica: análise entre os estados ou regiões brasileiras;

- Análise estatística: cálculo de médias, desvios, outliers por estado e por mês;

- Mapas e visualizações: uso de gráficos e mapas para representar espacialmente os dados;

- Análise de políticas públicas: investigar impactos de ações governamentais em anos específicos.

## 🧠 Considerações Finais

O dataset escolhido oferece grande potencial para investigar padrões e tendências dos incêndios florestais no Brasil. Sua riqueza temporal e geográfica permite análises profundas que podem contribuir com a conservação ambiental e formulação de estratégias de combate às queimadas ilegais.

Nos próximos passos, serão realizadas visualizações e análises mais aprofundadas, com o objetivo de extrair informações relevantes e propor insights com base nos dados.