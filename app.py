import streamlit as st 
from googletrans import Translator
from languages import *


st.title("Traductor Universal.oscar inc.")
source_text = st.text_area("Texto A Traducir:")
target_language = st.selectbox("Seleccione el idioma a traducir:", languages)
translate = st.button('Traducir')
if translate:
    translator = Translator()
    out = translator.translate(source_text,dest=target_language)
    st.write(out.text)
    
                               







