from openai import OpenAI

client = OpenAI()

messages = [
    {"role": "system", "content": "Eres un asistente útil y conciso."}
]

print("Chat GPT-4.1 (escribe 'salir' para terminar)\n")

while True:
    user_input = input("Tú: ")

    if user_input.lower() == "salir":
        print("Chat finalizado.")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages,
        temperature=0.7
    )

    assistant_reply = response.choices[0].message.content
    print(f"GPT: {assistant_reply}\n")

    messages.append({"role": "assistant", "content": assistant_reply})
