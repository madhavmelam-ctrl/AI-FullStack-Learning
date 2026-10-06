import requests
import time

# Ollama local API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# Local model installed through Ollama
MODEL = "llama3.2:1b"

# Test prompt
PROMPT = "Explain what an AI model is in simple terms."

data = {
    "model": MODEL,
    "prompt": PROMPT,
    "stream": False
}

print("Local AI Test")
print("-" * 50)
print("Model:", MODEL)
print("Prompt:", PROMPT)
print("-" * 50)

try:
    start_time = time.time()

    response = requests.post(
        OLLAMA_URL,
        json=data,
        timeout=120
    )

    response.raise_for_status()

    end_time = time.time()

    result = response.json()

    print("\nAI Response:")
    print(result.get("response", "No response received"))

    print("\nResponse Time:")
    print(f"{end_time - start_time:.2f} seconds")

    print("\nToken Information:")
    print("Input Tokens:", result.get("prompt_eval_count", "N/A"))
    print("Output Tokens:", result.get("eval_count", "N/A"))

except requests.exceptions.ConnectionError:
    print("\nError: Could not connect to Ollama.")
    print("Make sure Ollama is installed and running.")

except requests.exceptions.Timeout:
    print("\nError: The request timed out.")

except requests.exceptions.RequestException as error:
    print("\nAPI Error:", error)

except Exception as error:
    print("\nUnexpected Error:", error)