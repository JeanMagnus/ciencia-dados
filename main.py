import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import numpy as np # Necessário para o gráfico radar

# --- Configurações Iniciais do Streamlit ---
st.set_page_config(layout="wide") # Opcional: define o layout da página para largura total
st.title("Saúde Mental no Setor de Tecnologia: Uma Análise Exploratória")

st.write("""
    Este é um sistema web interativo para explorar os insights do meu trabalho de Análise Exploratória de Dados (EDA)
    sobre saúde mental no setor de tecnologia. A base de dados utilizada é da Open Sourcing Mental Illness (OSMI).
""")

# --- Carregamento dos Dados ---
# Mantendo o carregamento do GitHub para facilitar a demonstração e o deploy
@st.cache_data # Cache para carregar os dados apenas uma vez
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/JeanMagnus/ciencia-dados/main/survey.csv')
    return df

df = load_data()

st.subheader("Pré-visualização dos Dados")
st.dataframe(df.head())

st.subheader("Estatísticas Descritivas")
st.write(df.describe())

# --- Padronização da Coluna de Gênero (seu código) ---
# Listas de termos conforme sua definição
male_terms = [
    'cis male', 'cis man', 'm', 'mail', 'make', 'mal', 'male', 'male (cis)',
    'malr', 'man', 'cis male', 'm', 'maile', 'male', 'msle'
]

female_terms = [
    'cis female', 'f', 'femake', 'female', 'female (cis)', 'woman',
    'cis-female/femme', 'f', 'femail', 'female', 'woman'
]

trans_terms = [
    'female (trans)', 'trans woman', 'trans-female', 'male to female', 'transfemale'
]

nonbinary_terms = [
    'a little about you', 'agender', 'all', 'androgyne', 'enby', 'genderqueer',
    'guy (-ish) ^_^', 'nah', 'neuter', 'fluid', 'male leaning androgynous',
    'non-binary', 'ostensibly male, unsure what that really means', 'p',
    'queer', 'queer/she/they', 'something kinda male?', 'male-ish', 'nonbinary'
]

# Função de classificação
def classify_gender_custom(g):
    g = str(g).strip().lower()
    if g in male_terms:
        return 'Homem'
    elif g in female_terms:
        return 'Mulher'
    elif g in trans_terms:
        return 'Trans'
    elif g in nonbinary_terms:
        return 'Não-binárie'
    else:
        return 'Outro'

df['Gender_clean'] = df['Gender'].apply(classify_gender_custom)

# --- Análise de Histórico Familiar ---
st.header("Análise de Histórico Familiar")
df['family_history'] = df['family_history'].str.strip().str.capitalize()
df = df[df['family_history'].isin(['Yes', 'No'])]

# Gráfico de Pizza (usando Plotly para interatividade)
history_counts = df['family_history'].value_counts().reset_index()
history_counts.columns = ['Histórico Familiar', 'Count']
fig_pie = px.pie(
    history_counts,
    values='Count',
    names='Histórico Familiar',
    title='Histórico Familiar de Problemas Mentais',
    color_discrete_sequence=['#66b3ff', '#ff9999']
)
st.plotly_chart(fig_pie)

st.write("""
    A maioria dos profissionais entrevistados não tem histórico familiar de problemas mentais (60.9%),
    mas uma parcela significativa possui esse antecedente (39.1%). Isso destaca a importância de
    considerar fatores familiares ao discutir saúde mental no ambiente de trabalho.
""")

# --- Tratamento x Histórico Familiar ---
st.header("Tratamento x Histórico Familiar")
df['treatment'] = df['treatment'].str.strip().str.capitalize()
df = df[df['treatment'].isin(['Yes', 'No'])]

cross_tab = pd.crosstab(df['family_history'], df['treatment'])
cross_tab_reset = cross_tab.reset_index().melt(id_vars='family_history',
                                                var_name='treatment',
                                                value_name='count')

fig_bar_history_treat = px.bar(
    cross_tab_reset,
    x='family_history',
    y='count',
    color='treatment',
    barmode='group',
    title='Tratamento x Histórico Familiar de Problemas Mentais',
    labels={'family_history': 'Histórico Familiar', 'count': 'Quantidade de Pessoas', 'treatment': 'Procurou Tratamento'},
    color_discrete_map={'Yes': '#82E0AA', 'No': '#F1948A'} # Cores mais claras para combinar com Streamlit
)
st.plotly_chart(fig_bar_history_treat)

st.write("""
    **Análise:** Pessoas com histórico familiar de problemas mentais têm uma probabilidade muito maior de buscar tratamento (74,2%).
    Entre aqueles sem histórico familiar, o cenário se inverte: 35,5%.
    Uma possível explicação para esse dado seria que quem tem contato próximo com familiares que enfrentam
    transtornos mentais costuma desenvolver uma maior conscientização sobre o tema.
""")

# --- Relação entre Ambiente de Trabalho e Busca por Tratamento ---
st.header("Ambiente de Trabalho x Busca por Tratamento")
df['remote_work'] = df['remote_work'].str.strip().str.capitalize()
df_remote = df[df['remote_work'].isin(['Yes', 'No'])]

remote_treat = pd.crosstab(df_remote['remote_work'], df_remote['treatment'])
remote_treat_reset = remote_treat.reset_index().melt(id_vars='remote_work', var_name='treatment', value_name='count')

fig_bar_remote_treat = px.bar(
    remote_treat_reset,
    x='remote_work',
    y='count',
    color='treatment',
    barmode='group',
    title='Ambiente de Trabalho x Busca por Tratamento',
    labels={'remote_work': 'Trabalho Remoto?', 'count': 'Quantidade de Pessoas', 'treatment': 'Procurou Tratamento'},
    color_discrete_map={'Yes': '#82E0AA', 'No': '#F1948A'}
)
st.plotly_chart(fig_bar_remote_treat)

st.write("""
    Entre os trabalhadores presenciais, 49,7% procuraram tratamento psicológico,
    enquanto 50,3% não buscaram. Já entre os remotos, 52,7% buscaram ajuda, enquanto 47,3% não recorreram.
    Há uma diferença de aproximadamente 3 pontos percentuais, com uma leve tendência de maior busca por apoio
    psicológico entre os trabalhadores remotos.
""")

# --- Análise de Diferenças por País ---
st.header("Análise de Diferenças por País")
top_paises = df['Country'].value_counts().head(10)
df_top_paises = df[df['Country'].isin(top_paises.index)]

pais_treat = pd.crosstab(df_top_paises['Country'], df_top_paises['treatment'])
pais_treat_reset = pais_treat.reset_index().melt(id_vars='Country',
                                                var_name='treatment',
                                                value_name='count')

fig_bar_pais_treat = px.bar(
    pais_treat_reset,
    x='Country',
    y='count',
    color='treatment',
    barmode='stack', # Gráfico empilhado
    title='Tratamento por País (Top 10)',
    labels={'Country': 'País', 'count': 'Quantidade', 'treatment': 'Procurou Tratamento'},
    color_discrete_map={'Yes': '#82E0AA', 'No': '#F1948A'}
)
st.plotly_chart(fig_bar_pais_treat)

st.write("""
    O gráfico mostra que os Estados Unidos e o Reino Unido têm os maiores números de pessoas que buscaram tratamento.
    Em seguida, aparecem Canadá e Alemanha, com números intermediários. Já países como Índia, Austrália e Brasil
    apresentam números menores.
""")

# --- Faixa Etária ---
st.header("Faixa Etária das Pessoas que Mais Procuraram Tratamento")
df_age = df[(df['Age'] >= 15) & (df['Age'] <= 80)].copy()

bins = [15, 24, 34, 44, 54, 64, 80]
labels_age = ['15-24', '25-34', '35-44', '45-54', '55-64', '65-80']
df_age['faixa_etaria'] = pd.cut(df_age['Age'], bins=bins, labels=labels_age)

faixa_treat = pd.crosstab(df_age['faixa_etaria'], df_age['treatment'])
faixa_treat_reset = faixa_treat.reset_index().melt(id_vars='faixa_etaria', var_name='treatment', value_name='count')

fig_bar_age_treat = px.bar(
    faixa_treat_reset,
    x='faixa_etaria',
    y='count',
    color='treatment',
    barmode='stack', # Gráfico empilhado
    title='Tratamento por Faixa Etária',
    labels={'faixa_etaria': 'Faixa Etária', 'count': 'Quantidade', 'treatment': 'Procurou Tratamento'},
    color_discrete_map={'Yes': '#82E0AA', 'No': '#F1948A'}
)
st.plotly_chart(fig_bar_age_treat)

st.write("""
    O gráfico mostra que a faixa etária 25-34 anos tem o maior número de indivíduos,
    mas a maioria não procurou tratamento. Conforme a idade aumenta, o número total
    de pessoas diminui, mas a proporção entre quem procurou e quem não procurou tratamento varia.
""")

# --- Gênero das Pessoas que Procuraram Tratamento ---
st.header("Gênero das Pessoas que Procuraram Tratamento")

genero_treat = pd.crosstab(df['Gender_clean'], df['treatment'])
genero_treat = genero_treat[['Yes', 'No']] # Garante a ordem

genero_treat_reset = genero_treat.reset_index().melt(id_vars='Gender_clean',
                                                    var_name='treatment',
                                                    value_name='count')

fig_bar_gender_treat = px.bar(
    genero_treat_reset,
    x='Gender_clean',
    y='count',
    color='treatment',
    barmode='stack',
    title='Tratamento por Gênero',
    labels={'Gender_clean': 'Gênero', 'count': 'Quantidade', 'treatment': 'Procurou Tratamento'},
    color_discrete_map={'Yes': '#cccccc', 'No': '#f4a3a3'} # Suas cores originais
)
st.plotly_chart(fig_bar_gender_treat)

st.write("""
    Há uma diferença significativa na busca por tratamento entre os grupos analisados.
    Os homens, em sua maioria, não procuraram ajuda, enquanto entre as mulheres, uma proporção
    maior tomou a iniciativa de buscar tratamento. Já entre pessoas não-binárias e trans,
    os números são bem reduzidos, e pouquíssimos indivíduos desses grupos procuraram tratamento.
""")

# --- Gráfico Radar (Adaptado e Generalizado) ---
st.header("Percepção de Apoio à Saúde Mental por Gênero (Proporcional)")

# Função para gerar gráfico radar
def plot_radar_chart(group_labels, feature_labels, group_values, title):
    angles = np.linspace(0, 2 * np.pi, len(feature_labels), endpoint=False).tolist()
    angles += angles[:1]  # Fechar o círculo

    fig = px.line_polar(
        r=group_values[0],
        theta=feature_labels,
        line_close=True,
        title=title
    )
    for i, values in enumerate(group_values):
        fig.add_trace(
            px.line_polar(
                r=values,
                theta=feature_labels,
                line_close=True
            ).data[0]
        )
        fig.data[i].name = group_labels[i] # Nome para a legenda

    fig.update_traces(fill='toself')
    return fig

colunas_apoio = ['benefits', 'care_options', 'seek_help', 'anonymity']
labels_em_portugues = [
    'Acesso a benefícios',
    'Opções de cuidado',
    'Pode buscar ajuda',
    'Anonimato garantido'
]

grupo_labels = ['Homem', 'Mulher', 'Trans/NB']
grupo_valores = []

for grupo in grupo_labels:
    if grupo == 'Trans/NB':
        grupo_df = df[df['Gender_clean'].isin(['Trans', 'Não-binárie'])]
    else:
        grupo_df = df[df['Gender_clean'] == grupo]
    proporcoes = []
    for col in colunas_apoio:
        prop = grupo_df[col].value_counts(normalize=True).get('Yes', 0) * 100
        proporcoes.append(prop)
    grupo_valores.append(proporcoes)

# Plotar gráfico radar com labels em português usando Plotly
fig_radar = plot_radar_chart(grupo_labels, labels_em_portugues, grupo_valores, 'Percepção de Apoio à Saúde Mental por Gênero')
st.plotly_chart(fig_radar)

st.write("""
    Esse gráfico mostra como diferentes grupos percebem o apoio disponível. Pessoas trans e não binárias
    sentem que o anonimato é mais importante para elas, enquanto na parte de benefícios, opções de cuidado
    e buscar ajuda, os três grupos têm percepções parecidas, sem grandes diferenças entre masculino e feminino.
""")

# --- Análise de Correlação ---
st.header("Análise de Correlação")

cols_corr = [
    'treatment', 'benefits', 'care_options', 'seek_help', 'anonymity',
    'family_history', 'remote_work'
]

labels_pt_corr = {
    'treatment': 'Tratamento',
    'benefits': 'Benefícios',
    'care_options': 'Opções de cuidado',
    'seek_help': 'Busca por ajuda',
    'anonymity': 'Anonimato',
    'family_history': 'Histórico familiar',
    'remote_work': 'Trabalho remoto'
}

df_corr = df[cols_corr].copy()

# Conversão de Yes/No para 1/0
for col in cols_corr:
    if df_corr[col].dtype == 'object': # Verifica se a coluna é de tipo 'object' (string)
        df_corr[col] = df_corr[col].map({'Yes': 1, 'No': 0})

df_corr = df_corr.dropna()
corr_matrix = df_corr.corr()

# Renomear as colunas e índices para português
corr_matrix.index = corr_matrix.index.map(labels_pt_corr)
corr_matrix.columns = corr_matrix.columns.map(labels_pt_corr)

# Heatmap usando Plotly
fig_heatmap = px.imshow(
    corr_matrix,
    text_auto=True, # Adiciona os valores da correlação
    aspect="auto",
    color_continuous_scale='RdBu', # 'coolwarm' equivalente no Plotly
    title='Matriz de Correlação do Apoio e Tratamento de Saúde Mental Geral'
)
st.plotly_chart(fig_heatmap)

st.write("""
    A matriz de correlação mostra que a busca por tratamento está mais ligada ao histórico familiar (0.37)
    e ao acesso a opções de cuidado (0.26). Ter benefícios (0.14) e sentir que pode pedir ajuda (0.10)
    têm uma relação bem mais fraca. Já anonimato (0.06) e trabalho remoto (0.01) quase não influenciam.
    No geral, só o histórico e o acesso a cuidados mostram uma ligação mais evidente com a decisão de procurar ajuda.
""")