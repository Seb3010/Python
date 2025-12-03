from google import genai

GEMINI_API_KEY = "AIzaSyA2BiPDCzDZwkJS-pqJ_4z_2wGZd8t3fLQ"

client = genai.Client(api_key=GEMINI_API_KEY) 

while True:
    pregunta = input("En que puedo ayudarte? ")
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
        contents=pregunta,
    )

    print(f"\nRespuesta: {response.text} ")