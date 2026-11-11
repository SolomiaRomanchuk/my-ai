from datetime import date

from openai import OpenAI
from pydantic import BaseModel, Field, ValidationError

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)


class TripRequest(BaseModel):
    city: str
    date: date
    days: int = Field(ge=1)


SYSTEM = (
    "Extract trip details from the user's message. "
    'Return only JSON: {"city": str, "date": "YYYY-MM-DD", "days": int}. '
    "Today is 2026-11-03."
)

response = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[
        {"role": "system", "content": SYSTEM},
        {
            "role": "user",
            "content": "Хочу до Львова 7 листопада на 2 дні"
        },
    ],
    response_format={"type": "json_object"},
    temperature=0,
)

answer = response.choices[0].message.content
print("raw:", answer)

try:
    trip = TripRequest.model_validate_json(answer)
    print("ok:", trip.city, trip.date, trip.days)
except ValidationError as e:
    print("model returned bad data:", e)