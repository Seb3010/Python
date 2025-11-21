import nltk

nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

with open('words.txt', 'r', encoding='utf-8') as archivo:
    palabras_prohibidas = archivo.read().splitlines()

text = "Este es un ejemplo de texto en español."

words = word_tokenize(text)

stop_words = set(stopwords.words('spanish'))
filtered_words = [palabra for palabra in words if palabra.lower() not in stop_words]

for palabra in filtered_words:
    if palabra in palabras_prohibidas:
        texto_aceptado = False
    else:
        texto_aceptado = True

if texto_aceptado == True:
    print("El texto ha sido aceptado.")
else:
    print("El texto ha sido rechazado debido a la presencia de palabras no permitidas.")