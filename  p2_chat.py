
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

MODEL = "qwen2.5:3b"

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "Ти помічник з подорожей за кордон. "
        "Допомагай обирати міста, планувати маршрути "
        "та складати бюджет. Відповідай українською, коротко."
    )
}

messages = [SYSTEM_PROMPT.copy()]

while True:
    text = input("you: ").strip()

    if text.lower() in ("exit", "quit"):
        break

    if text == "/reset":
        messages = [SYSTEM_PROMPT.copy()]
        print("bot: Історію очищено!")
        continue

    if not text:
        continue

    messages.append({"role": "user", "content": text})

    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True,
        stream_options={"include_usage": True}
    )

    answer = ""
    total_tokens = None

    print("bot: ", end="", flush=True)

    for chunk in stream:
        if chunk.choices:
            piece = chunk.choices[0].delta.content
            if piece:
                print(piece, end="", flush=True)
                answer += piece

        if chunk.usage is not None:
            total_tokens = chunk.usage.total_tokens

    print()

    messages.append({
        "role": "assistant",
        "content": answer
    })

    print(f"(history: {len(messages)} messages)")

    if total_tokens is not None:
        print(f"(tokens: {total_tokens})")
    else:
        print("(tokens: usage unavailable)")
