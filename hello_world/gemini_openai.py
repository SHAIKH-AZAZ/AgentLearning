from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": "You are an expert in maths and give responce to math questions olny , if query is not related to maths problem then say sorry i am unable to asnwer for this  please ask math related querys only ",
        },
        {
            "role": "user",
            "content": "hey help for a+b whole square ",
        },
    ],
)


print(response.choices[0].message.content)
