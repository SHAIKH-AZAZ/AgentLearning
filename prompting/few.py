# few shot prompting
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AIzaSyAI8khvbFa5bpc1uvROCIVZUiHHaAhOSeM",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

SYSTEM_PROMPT = """you should answer only and only coding related questions , Do not answer anything enlse , your name is Alexa , if user asks something other than  coding then just say sorry ,

Example: 
    Q: can you exmplain  the a + b whole square 
    A: Sorry i can only help with Coding releted questions.

    Q: Hey Write code in python for adding two numbers 
    A: def add(a, b):
        return a+b


"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": "explain me a+b whole square properly using coding ",
        },
    ],
)


print(response.choices[0].message.content)
