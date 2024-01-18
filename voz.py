import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from googletrans import Translator
from languages import *
import pyttsx3
speak = pyttsx3.init()
voices = speak.getProperty('voices')
voice_id = 'english'
speak.setProperty('voice', voice_id)

st.title("Traductor Universal.oscar inc.")

stt_button = Button(label="Speak", width=100)

stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
 
    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)


# target_language = st.selectbox("Seleccione el idioma a traducir:", languages)
# target_language = st.selectbox("Seleccione el idioma a traducir:", "English")
if result:
    if "GET_TEXT" in result:
        source_text = result.get("GET_TEXT")
        st.write(source_text)

        
        # translate = st.button('Traducir')
        # if translate:
        translator = Translator()
        out = translator.translate(source_text,dest="English")
        st.write(out.text)
        salida = out.text
        speak.say(salida)
        speak.runAndWait()

