from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. Answer in Ukrainian, briefly."
        },
        {
            "role": "user",
            "content": "What is API in programing?"
        },
    ],
    temperature=0.3,
)

print(response.choices[0].message.content)
print("tokens:", response.usage.total_tokens)