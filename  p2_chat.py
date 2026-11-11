from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

MODEL = "qwen2.5:3b"

messages = [
    {
        "role": "system",
        "content": (
            "Ти помічник з подорожей за кордон. "
            "Допомагай обирати міста, планувати маршрути "
            "та складати бюджет. Відповідай українською, коротко."
        )
    }
]

while True:
    text = input("you: ")

    if text in ("exit", "quit"):
        break

    messages.append({"role": "user", "content": text})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    answer = response.choices[0].message.content

    messages.append({"role": "assistant", "content": answer})

    print("bot:", answer)
    print(f"(history: {len(messages)} messages)")