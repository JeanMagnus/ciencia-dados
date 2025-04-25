# 📊 Projeto de Análise de Dados – Parte I

## 🧠 Introdução

Neste projeto, será utilizado o dataset **"Mental Health in Tech Survey"**, disponível no Kaggle, que reúne respostas de profissionais da área de tecnologia sobre saúde mental no ambiente de trabalho. A pesquisa foi organizada pela **OSMI (Open Sourcing Mental Illness)**, organização que promove conscientização sobre saúde mental, especialmente em ambientes técnicos.

A análise desse tipo de dado é extremamente relevante, pois a saúde mental vem se tornando um tema central nas discussões sobre qualidade de vida no trabalho. Identificar padrões, barreiras ao tratamento e relações com condições laborais pode ajudar empresas e profissionais a tomarem decisões mais conscientes e humanizadas.

## 🗃️ Sobre o Dataset

- **Fonte:** [Kaggle - Mental Health in Tech Survey](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey)
- **Formato:** CSV
- **Total de linhas:** Aproximadamente 1.400
- **Total de colunas:** 27
- **Tipo de dados:** Qualitativos e quantitativos

## 📌 Variáveis de Interesse

Algumas variáveis selecionadas para análise incluem:

| Coluna                    | Descrição                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| `Age`                    | Idade do participante                                                     |
| `Gender`                 | Gênero do participante                                                    |
| `Country`                | País de residência                                                        |
| `self_employed`          | Indica se o participante trabalha por conta própria                       |
| `family_history`         | Histórico familiar de problemas de saúde mental                          |
| `treatment`              | Já procurou tratamento para saúde mental?                                 |
| `work_interfere`         | A saúde mental interfere no trabalho?                                     |
| `no_employees`           | Tamanho da empresa                                                        |
| `remote_work`            | Trabalha remotamente?                                                     |
| `benefits`               | A empresa oferece suporte psicológico?                                    |
| `care_options`           | Existem opções de cuidado mental na empresa?                              |
| `wellness_program`       | A empresa oferece programas de bem-estar?                                 |

## 🔍 Detecção de Dados Faltantes

Para verificar a existência de dados ausentes, foi utilizado o seguinte código em Python:

```python
import pandas as pd

# Carregar o dataset
df = pd.read_csv('survey.csv')

# Verificar a quantidade de valores nulos por coluna
print(df.isnull().sum())
```

### ✅ Resultado obtido:

```
state                         515
self_employed                  18
work_interfere                264
comments                     1095
Todas as outras colunas      0 valores ausentes
```

## 🛠️ Tratamento de Dados (Pré-processamento)

Para as análises futuras, serão realizados os seguintes tratamentos:

- **Remoção ou imputação de dados ausentes:**
  - `work_interfere` e `self_employed`: preenchimento com a moda
  - `state`: pode ser descartada caso o foco não seja específico nos EUA
  - `comments`: será desconsiderada por conter dados não estruturados e opcionais

- **Padronização de valores textuais:**
  - Ex: normalizar valores da coluna `Gender`, que aparecem de formas variadas

- **Codificação de variáveis categóricas** para análises quantitativas (ex: Label Encoding ou One-Hot Encoding)

- **Remoção de outliers**, especialmente na coluna `Age`, que contém valores extremos (ex: < 10 anos ou > 100)

## 🔮 Possíveis Análises Futuras

Com o dataset limpo e preparado, será possível realizar diversas análises, como:

- Comparação entre **profissionais com e sem histórico familiar de problemas mentais**
- Relação entre **ambiente de trabalho remoto/presencial** e a **busca por tratamento**
- Investigação sobre o **impacto do suporte da empresa (benefits, care_options)** na saúde mental
- Análise de **diferenças por país, idade e gênero**
- Visualizações de distribuição e correlação entre variáveis

Essas análises poderão gerar insights valiosos sobre como melhorar o suporte à saúde mental no setor de tecnologia.

## 📌 Conclusão

O dataset da OSMI é uma rica fonte de dados sobre saúde mental no setor de tecnologia. Através de uma análise bem conduzida, será possível extrair informações relevantes que podem contribuir tanto para a comunidade profissional quanto para decisões empresariais mais responsáveis.
