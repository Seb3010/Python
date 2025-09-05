import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

while True:
    command = input("")
    if command.lower() in ["Adios jarvis", "salir", "Adios"]:
        engine.say("Goodbye!")
        engine.runAndWait()
        break
    elif command.lower() in ["hola"]:
        engine.say("Hola soy jarvis, como puedo ayudarte hoy?")
        engine.runAndWait()
    elif command.lower() in ["¿Que hora es hoy?"]:
        from datetime import datetime
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        engine.say(f"son las {time}")
        engine.runAndWait()
    elif command.lower() in ["¿Que dia es?"]:
        from datetime import datetime
        today = datetime.now()
        date = today.strftime("%B %d, %Y")
        engine.say(f"hoy es, {date}")
        engine.runAndWait()