from google import genai
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

GEMINI_API_KEY = "AIzaSyA2BiPDCzDZwkJS-pqJ_4z_2wGZd8t3fLQ"

client = genai.Client(api_key=GEMINI_API_KEY) 

while True:
    pregunta = input("En que puedo ayudarte? ")
    words = word_tokenize(pregunta)
    stop_words = set(stopwords.words("spanish"))

    filter_words = (words for word in words if word.lower not in stop_words)

    

    if pregunta == "salir":
        break
    try:
        if pregunta == "":
            print("Por favor, introduce una pregunta.")
            continue
    except:
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=pregunta
    )

    print(f"\nRespuesta: {response.text} ")