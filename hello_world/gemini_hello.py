from google import genai
from dotenv import load_dotenv

# loading api keys for this gemini

load_dotenv()

client = genai.Client(api_key="AIzaSyAI8khvbFa5bpc1uvROCIVZUiHHaAhOSeM")


response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)

print(response.text)

