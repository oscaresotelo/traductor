# import streamlit as st
# from bokeh.models.widgets import Button
# from bokeh.models import CustomJS
# from streamlit_bokeh_events import streamlit_bokeh_events
# from googletrans import Translator
# from languages import *
# import pyttsx3

# speak = pyttsx3.init()
# voices = speak.getProperty('voices')
# voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
# speak.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
# translator = Translator()
# st.title("Traductor Universal.oscar inc.")

# stt_button = Button(label="Speak", width=100)

# stt_button.js_on_event("button_click", CustomJS(code="""
#     var recognition = new webkitSpeechRecognition();
#     recognition.continuous = true;
#     recognition.interimResults = true;
 
#     recognition.onresult = function (e) {
#         var value = "";
#         for (var i = e.resultIndex; i < e.results.length; ++i) {
#             if (e.results[i].isFinal) {
#                 value += e.results[i][0].transcript;
#             }
#         }
#         if ( value != "") {
#             document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
#         }
#     }
#     recognition.start();
#     """))

# result = streamlit_bokeh_events(
#     stt_button,
#     events="GET_TEXT",
#     key="listen",
#     refresh_on_update=False,
#     override_height=90,
#     debounce_time=10)

# if result:
#     if "GET_TEXT" in result:
#         source_text = result.get("GET_TEXT")
#         st.write(source_text)

import speech_recognition as sr


def escuchar():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        # talk("Cual es tu pedido...")
        # print("cual es tu pedido...")
        recognizer.adjust_for_ambient_noise(source)
        
        try:
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=15)
            print("Reconociendo...")
            texto = recognizer.recognize_google(audio, language="es-ES")
            print(f"Texto reconocido: {texto}")
        except sr.UnknownValueError:
            speech_recognition("No se pudo entender el audio.")
            return None

if __name__ == "__main__":
    while True:
        resultado = escuchar()
        if resultado is not None:
            # Aquí puedes agregar lógica adicional basada en el texto reconocido
            pass
