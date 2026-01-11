# Proyecto: Colección de scripts Python

## Resumen
-Este repositorio sirve como bitacora de aprendizaje Aquí agrupo prácticas, ejercicios de lógica y pequeños scripts que voy creando mientras estudio.

## Requisitos
- Python 3.8+
- (Opcional) Flask para la app: ver [app/app.py](app/app.py)
- (Opcional) NLTK y Google GenAI para el chatbot: ver [Chatbot/Chatbot.py](Chatbot/Chatbot.py)

## Archivos principales
- [app/app.py](app/app.py) — Aplicación Flask (ruta `/`, función `home`).
- [Chatbot/Chatbot.py](Chatbot/Chatbot.py) — Chatbot escolar (usa NLTK y GenAI).
- [neuron.py](neuron.py) — Implementación simple de neurona y capa: [`neuron.Neuron`](neuron.py), [`neuron.Layer`](neuron.py).
- [activos.py](activos.py) — Clase para activos: [`activos.Activo`](activos.py).
- [Materias/main.py](Materias/main.py) y [Materias/materias.py](Materias/materias.py) — Gestión de materias y la clase [`Materias.signature`](Materias/materias.py).
- [promedio.py](promedio.py) — Calculador de promedios (función [`promedio.bienvenida`](promedio.py)).
- [calculator_2.py](calculator_2.py) — Calculadora con operaciones básicas (ej. [`calculator_2.suma`](calculator_2.py)).
- [adivina.py](adivina.py) — Juego "adivina el número".
- [reclubot.py](reclubot.py) — Evaluador de soft skills interactivo.
- [jarvis.py](jarvis.py) — Asistente por texto/voz (pyttsx3).
- [Formula.py](Formula.py) — Utilidades geométricas.
- [calculatar_num_primos.py](calculatar_num_primos.py) — Verifica números primos.
- [RFC.py](RFC.py) — Generador simple de RFC.

## Cómo ejecutar
- Chatbot: python Chatbot/Chatbot.py
- Ejecutar un script: python <archivo>.py

Hecho con 🐍 por **Sebastian Partida**