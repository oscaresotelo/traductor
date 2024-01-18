# import pyttsx3

# engine = pyttsx3.init()

# for voice in engine.getProperty('voices'):
#     print(voice)
from googletrans import Translator

translator = Translator()
traduccion = translator.translate("hola como estas", dest= "en")
print(traduccion.text)