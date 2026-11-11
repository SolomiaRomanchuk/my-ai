from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

stream = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": "Tell a short story about a Python developer"
        }
    ],
    stream=True,
)

for chunk in stream:
    piece = chunk.choices[0].delta.content
    if piece:
        print(piece, end="", flush=True)

print()