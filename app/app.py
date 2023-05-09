import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from predict_page import show_predict_page
from explore_page import show_explore_page

image = Image.open('../img/front_img.png')

st.title("Plataforma de Inteligência de Dados")
st.image(image,caption='Plataforma Credit as a Service',output_format='PNG')

with st.sidebar:
    page = option_menu("Open Finance Menu", ["Predição","Insights Open Finance"], 
        icons=[ 'robot' , 'house'], menu_icon="cast", default_index=1)

#if page=='Insights Open Finance':
#    show_explore_page()
#else: 
show_predict_page()
