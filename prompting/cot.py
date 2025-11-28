# chain of thougth

import json
import os
import time

from dotenv import load_dotenv
from typing_extensions import runtime

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("Set api key properly ")


try:
    from openai import OpenAI
except Exception:
    raise RuntimeError("Please install openaAI librarys ")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Clear, valid instructions for the model
SYSTEM_PROMPT = """
You are an assistant that responds with a single JSON object per reply.
The JSON object must have exactly two keys:
  - "step": one of "START", "Plan", "OUTPUT"
  - "content": a string describing the step content

Example flow (this is an example; do not include extra text outside the JSON):
{"step":"START","content":"User asked to compute 2+3*5/10"}
{"step":"Plan","content":"Apply BODMAS: first do multiplication 3*5=15"}
{"step":"Plan","content":"Then do division 15/10=1.5"}
{"step":"Plan","content":"Finally add 2 + 1.5 = 3.5"}
{"step":"OUTPUT","content":"3.5"}

Important:
- Reply only with the JSON object, nothing else.
- If you produce additional explanation, it will break the JSON parsing.
"""


# finding text inside json output given by ai/LLM
def extract_json(text):
    """Extract JSON even if the model adds stray text."""
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end < start:
        raise ValueError("Could not find JSON object in response.")
    return json.loads(text[start : end + 1])


message_history = [{"role": "system", "content": SYSTEM_PROMPT}]

user_query = input("👉 ")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=message_history,
    )

    raw = response.choices[0].message.content

    # Try parsing JSON
    try:
        parsed = extract_json(raw)
    except Exception:
        print("❌ Model returned invalid JSON:")
        print(raw)
        break

    # Add to history
    message_history.append({"role": "assistant", "content": raw})

    step = parsed.get("step")
    content = parsed.get("content", "")

    if step == "START":
        print("🚀 START:", content)
    elif step == "Plan":
        print("🧭 PLAN:", content)
    elif step == "OUTPUT":
        print("🎉 OUTPUT:", content)
        break
    else:
        print("⚠️ Unknown step:", parsed)
        break

