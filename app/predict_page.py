import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('../saved_steps.pkl' , 'rb') as file:
        data =  pickle.load(file)

    return data

data = load_model()

classificator = data['model']

def show_predict_page():
    st.title("Crédito Personalizado Open Finance")
    st.write("""Inteligência Artificial Aplicada a Personalização de crédito via Open Finance.""")
    st.write("""Informe os seguintes Dados""")

    limit_bal = st.slider("Limite de Crédito" , 1000, 100000, 5000)

    age = st.number_input('Idade:')

    pay_amt6 = st.number_input('Valor pago na última fatura: ')

    ok = st.button('Veja se será inadinplente')
    if ok:
        X = np.array([[limit_bal,age,pay_amt6]])

        predicao = classificator.predict(X)[0]
        if predicao == 1:
            st.subheader("O seu cliente será inadimplente.")
        else:
            st.subheader("O seu cliente não será indadimplente.")
