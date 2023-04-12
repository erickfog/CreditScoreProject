import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv('../data/dataset_trat.csv')

    return df

df = load_data()


def show_explore_page():
    
    st.title('Explore sobre seus cliente')

    st.write("""Confira o número de inadimplentes por idade.""")

    #df_aux = df[df['default']==1]
    #aux = df_aux[['AGE','default']].groupby('AGE').sum().reset_index()
    #fig , ax = plt.subplots()
    #plt.bar(aux['AGE'], aux['default'])
    #st.pyplot(fig)
