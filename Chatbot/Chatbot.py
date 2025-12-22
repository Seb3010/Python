from google import genai
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Descargar datos de NLTK si no existen (idempotente)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

CONTEXTOS = {
    "Matemáticas": {
        "keywords": {"ecuacion", "suma", "resta", "multiplicar", "dividir", "numero", "algebra", "calculo", "geometria"},
        "prompt": "Eres un profesor de matemáticas paciente y experto. Explica las soluciones paso a paso."
    },
    "Historia": {
        "keywords": {"historia", "guerra", "independencia", "revolucion", "año", "siglo", "rey", "presidente"},
        "prompt": "Eres un historiador experto. Contextualiza los eventos y explica sus causas y consecuencias."
    },
    "Ciencias": {
        "keywords": {"celula", "atomo", "energia", "fuerza", "quimica", "biologia", "fisica", "experimento"},
        "prompt": "Eres un profesor de ciencias. Explica los fenómenos naturales con ejemplos claros."
    },
    "Literatura": {
        "keywords": {"libro", "autor", "poema", "ensayo", "ortografia", "gramatica", "verbo"},
        "prompt": "Eres un experto en literatura y lengua española. Ayuda a analizar textos y mejorar la redacción."
    },
    "Programación": {
        "keywords": {"codigo", "python", "java", "error", "variable", "funcion", "bucle"},
        "prompt": "Eres un ingeniero de software senior. Ayuda a depurar código y explica conceptos de programación."
    }
}

def get_context(pregunta):
    """
    Analiza la pregunta y retorna un contexto basado en palabras clave.
    """
    words = word_tokenize(pregunta)
    stop_words = set(stopwords.words("spanish"))

    # Corregido: word.lower() y generador a lista
    filter_words = [word.lower() for word in words if word.lower() not in stop_words]

    for materia, data in CONTEXTOS.items():
        # Verificamos si alguna palabra clave está en las palabras filtradas
        # Usamos intersección de conjuntos para eficiencia
        if not data["keywords"].isdisjoint(filter_words):
            return data["prompt"]

    return "Eres un asistente escolar útil y motivador."

def main():
    GEMINI_API_KEY = "AIzaSyA2BiPDCzDZwkJS-pqJ_4z_2wGZd8t3fLQ"
    client = genai.Client(api_key=GEMINI_API_KEY) 

    print("Bienvenido al Chatbot Escolar. Escribe 'salir' para terminar.")

    while True:
        try:
            pregunta = input("En que puedo ayudarte? ")
        except (EOFError, KeyboardInterrupt):
            break

        if pregunta.lower() == "salir":
            break
        
        if not pregunta.strip():
            print("Por favor, introduce una pregunta.")
            continue

        contexto = get_context(pregunta)
        prompt_completo = f"Instrucción de sistema: {contexto}\n\nPregunta del usuario: {pregunta}"

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt_completo,
            )
            print(f"\nRespuesta: {response.text} ")
        except Exception as e:
            print(f"Error al conectar con la API: {e}")

if __name__ == "__main__":
    main()


    print
