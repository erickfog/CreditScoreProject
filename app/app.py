import streamlit as st
from streamlit_option_menu import option_menu
from predict_page import show_predict_page
from explore_page import show_explore_page

st.title("Plataforma de Inteligência de Dados")

with st.sidebar:
    page = option_menu("Open Finance Menu", ["Predição","Insights Open Finance"], 
        icons=[ 'robot' , 'house'], menu_icon="cast", default_index=1)

if page=='Insights Open Finance':
    show_explore_page()
else: 
    show_predict_page()
