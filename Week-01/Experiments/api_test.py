import os
import time
from dotenv import load_dotenv
from google import genai

# Load API key from Week-01/.env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY was not found in .env")
    exit()

# Create Gemini client
client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash"
PROMPT = "Explain what an AI API is in simple terms."

print("Cloud AI API Test")
print("-" * 50)
print("Provider: Google Gemini")
print("Model:", MODEL)
print("Prompt:", PROMPT)
print("-" * 50)

try:
    start_time = time.time()

    response = client.models.generate_content(
        model=MODEL,
        contents=PROMPT
    )

    end_time = time.time()

    print("\nAI Response:")
    print(response.text)

    print("\nResponse Time:")
    print(f"{end_time - start_time:.2f} seconds")

    if response.usage_metadata:
        print("\nToken Information:")
        print(
            "Input Tokens:",
            response.usage_metadata.prompt_token_count
        )
        print(
            "Output Tokens:",
            response.usage_metadata.candidates_token_count
        )
        print(
            "Total Tokens:",
            response.usage_metadata.total_token_count
        )

except Exception as error:
    print("\nAPI Request Failed:")
    print(error)