import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv('../data/dataset_trat.csv', sep=';')

    return df

df = load_data()


def show_explore_page():
    
    st.title('Explore os Dados dos Clientes')

    df1 = df
    button = st.selectbox("Perfil de Inadimplentes" , ("Inadimplentes" , "Não Inadimplentes") )

    aux = df1[df1['default']==1]
    aux1 = aux[['SEX','default']].groupby('SEX').sum().reset_index()
    sns.barplot(data=aux1 , x='SEX' , y='default');
    plt.xlabel('SEXO')
    plt.ylabel('Total de Inadimplentes')
    plt.show()
    st.pyplot(plt)

    aux2 = aux[['EDUCATION','default']].groupby('EDUCATION').sum().reset_index()
    sns.barplot(data=aux2 , x='EDUCATION' , y='default');
    plt.xlabel('EDUCAÇÃO')
    plt.ylabel('Total de Inadimplentes')
    st.pyplot(plt)

    aux3 = aux[['MARRIAGE','default']].groupby('MARRIAGE').sum().reset_index()
    sns.barplot(data=aux3 , x='MARRIAGE' , y='default');
    plt.xlabel("Estado Civil")
    plt.ylabel('Total de Inadimplentes')
    st.pyplot(plt)

    # Filtrando os dados para inadimplentes e não inadimplentes
    df4_aux1 = df1[df1['default']==1].copy()
    df4_aux0 = df1[df1['default']==0].copy()

    # Plotando o gráfico de densidade
    fig, ax = plt.subplots(figsize=(10,6))

    sns.kdeplot(df4_aux1['AGE'], shade=True, color='red', label='Inadimplentes', ax=ax)
    sns.kdeplot(df4_aux0['AGE'], shade=True, color='blue', label='Não inadimplentes', ax=ax)

    ax.set_xlabel('Idade')
    ax.set_ylabel('Densidade')
    ax.set_title('Distribuição de idade para inadimplentes e não inadimplentes')
    ax.legend()
    plt.show()
    st.pyplot(plt)

    # Filtrando os dados para inadimplentes e não inadimplentes
    df4_aux1 = df1[df1['default']==1].copy()
    df4_aux0 = df1[df1['default']==0].copy()

    # Plotando o gráfico de densidade
    fig, ax = plt.subplots(figsize=(10,6))

    sns.kdeplot(df4_aux1['LIMIT_BAL'], shade=True, color='red', label='Inadimplentes', ax=ax)
    sns.kdeplot(df4_aux0['LIMIT_BAL'], shade=True, color='blue', label='Não inadimplentes', ax=ax)

    ax.set_xlabel('Limite de Crédito Disponível')
    ax.set_ylabel('Densidade')
    ax.set_title('Distribuição de crédito para inadimplentes e não inadimplentes')
    ax.legend()

    plt.show()
    st.pyplot(plt)
