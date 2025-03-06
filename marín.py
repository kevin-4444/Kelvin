
pip install nltkfrom nltk.chat.util import Chat, reflections

# Definir pares de patrones y respuestas
pairs = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, ¿cómo estás?",]
    ],
    [
        r"hola|hey|buenas",
        ["Hola, ¿qué tal?", "Hey, ¿cómo te va?", "Hola, ¿cómo estás?"]
    ],
    [
        r"¿cómo estás?",
        ["Estoy bien, gracias por preguntar. ¿Y tú?",]
    ],
    [
        r"adiós|chao|nos vemos",
        ["Adiós, ¡que tengas un buen día!", "Chao, ¡cuídate!", "Nos vemos, ¡hasta luego!"]
    ],
    [
        r"gracias|muchas gracias",
        ["De nada, ¿en qué más puedo ayudarte?", "¡De nada!", "Para servirte."]
    ],
    [
        r"¿qué puedes hacer?",
        ["Puedo responder preguntas básicas y mantener una conversación simple. ¿En qué puedo ayudarte?",]
    ],
    # Agrega más pares de patrones y respuestas según tus necesidades
]

# Reflejos para manejar pronombres
reflections.update({
    "estoy": "estás",
    "soy": "eres",
    "mi": "tu",
    "yo": "tú"
})

# Crear el chatbot
chatbot = Chat(pairs, reflections)

# Función principal para chatear con el chatbot
def chat():
    print("Chatbot: ¡Hola! Soy tu chatbot personal. Pregúntame algo o escribe '.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ["salir", "exit"]:
            print("Chatbot: ¡Adiós!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot: ", response)

# Ejecutar el chatbot
if __name__ == "__main__":
    chat()