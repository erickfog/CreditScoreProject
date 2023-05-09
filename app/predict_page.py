import streamlit as st
import pickle
import numpy as np
import uuid

def load_model():
    with open('../model/creditscore.pkl' , 'rb') as file:
        data =  pickle.load(file)

    return data

data = load_model()

classificator = data['model']

def show_predict_page():
    st.title("Previsão de Inadimplência no Cartão de Crédito")
    st.write("""Inteligência Artificial Aplicada a Personalização de crédito.""")

    limit_bal = st.slider("Limite de Crédito Disponível:" , 1000, 100000, 5000)

    age = st.number_input('Idade:', 20)

    pay_0 = [ 'pago em dia', 'atraso 1 mês', 
            'atraso 2 meses', 'atraso 3 meses', 
            'atraso 4 meses', 'atraso 5 meses', 
            'atraso 6 meses', 'atraso 7 meses', 'atraso 8 meses']

    st.subheader("Informe o status de pagamento da sua fatura do mês 6 do anopassado.") 
    pay = { 'pago em dia': -1, 'atraso 1 mês': 1, 'atraso 2 meses': 2, 
            'atraso 3 meses': 3, 'atraso 4 meses': 4, 'atraso 5 meses': 5, 
            'atraso 6 meses': 6, 'atraso 7 meses': 7, 'atraso 8 meses': 8}
    pay_0 = st.selectbox( 'Informe os atrasos',pay.keys() )
    val_pay = pay[pay_0]

    sum_bill = st.number_input("Qual valor total das últimas seis faturas:")
    avg_bill = int(sum_bill/6.0)
    max_bill = st.number_input("Qual maior valor pago de fatura:")
    sum_pay = st.number_input("Qual valor total pago nos últimos seis meses:")
    avg_pay = int(sum_pay/6.0)
    max_pay = st.number_input("Qual valor mais alto pago em faturas:")

    ok = st.button('Previsão')
    if ok:
        X = np.array([[limit_bal,age,val_pay,sum_bill,avg_bill,max_bill,sum_pay,avg_pay,max_pay]])

        predicao = classificator.predict(X)[0]
        if predicao == 1:
            st.subheader("O seu cliente será inadimplente.")
        else:
            st.subheader("O seu cliente não será indadimplente.")

        proba = classificator.predict_proba(X)[:,1][0]
        score=0
        score = int(proba*1000)
        st.metric(label='Score',value=score)
