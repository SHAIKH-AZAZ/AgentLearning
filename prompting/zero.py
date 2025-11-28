# this zero shot prompting for something new things for testing
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AIzaSyAI8khvbFa5bpc1uvROCIVZUiHHaAhOSeM",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

SYSTEM_PROMPT = "You are an expert in maths and give responce to math questions olny , if query is not related to maths problem then say sorry i am unable to asnwer for this  please ask math related querys only "

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": "Can you tell me a joke ",
        },
    ],
)


print(response.choices[0].message.content)
