# import pyttsx3

# engine = pyttsx3.init()

# for voice in engine.getProperty('voices'):
#     print(voice)
# from googletrans import Translator

# translator = Translator()
# traduccion = translator.translate("hola como estas", dest= "en")
# print(traduccion.text)

import streamlit as st 
from gtts import gTTS
from io import BytesIO
sound_file = BytesIO()
st.title("Reproductor")
repro = st.text_area("ingresar texto")

if repro:
    tts = gTTS(repro, lang='en')
    tts.write_to_fp(sound_file)
    st.audio(sound_file)