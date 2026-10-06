import os
import sys
import time
import json
import csv
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError
from groq import Groq, GroqError
from huggingface_hub import InferenceClient
from huggingface_hub.errors import HfHubHTTPError
from openai import OpenAI, OpenAIError

# Ensure UTF-8 output encoding on Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Load environment variables from the .env file
load_dotenv()

# Define the 4 benchmark tests for the AI Model Research Lab
TESTS = [
    {
        "name": "TEST 1 — General Knowledge",
        "prompt": "Explain recursion in Python."
    },
    {
        "name": "TEST 2 — Coding",
        "prompt": "Write a Python function that removes duplicate items from a list."
    },
    {
        "name": "TEST 3 — Reasoning",
        "prompt": "A shop gives a 20% discount on a ₹500 product. What is the final price? Explain your reasoning."
    },
    {
        "name": "TEST 4 — Structured Output",
        "prompt": 'Explain Python lists and return ONLY valid JSON in this exact structure:\n{"title":"","summary":"","keywords":[]}'
    }
]

# Define Test 5 — Long Context
TEST_5 = {
    "name": "TEST 5 — Long Context",
    "prompt": """Read the following passage carefully and answer the questions at the end.

PASSAGE:

A software company named NovaTech is developing an AI-powered
customer support platform for small businesses.

The platform receives customer questions through a website.
When a customer submits a question, the application first checks
whether the question can be answered using information stored in
the company's knowledge base.

If relevant information is found, the application sends the
customer's question together with the retrieved information to
an AI language model.

The AI model then generates a response based on the supplied
context.

NovaTech currently tests three different ways of running AI
models.

The first approach uses cloud AI APIs. Cloud APIs are easy to
integrate and provide access to powerful models, but they may
have usage costs, rate limits, and require an internet connection.

The second approach uses local AI models through Ollama. Local
models can run directly on company computers and provide better
control over private data. However, their performance depends on
the available CPU, RAM, and GPU.

The third approach uses open-weight models hosted by external
inference providers. This allows NovaTech to experiment with
different models without purchasing powerful local hardware.

During testing, the engineering team discovered that choosing an
AI model based only on response quality was not sufficient.

They decided to measure several factors:

- Response accuracy
- Response time
- Token usage
- Cost
- Context-window size
- Hardware requirements
- Privacy
- Reliability

The team also learned that an AI model and an AI provider are not
the same thing. A model performs the inference, while a provider
supplies infrastructure or an API through which applications can
access the model.

For example, the same open model may be available through several
different inference providers.

NovaTech eventually plans to build an AI routing system. The
router will examine each customer request and decide which model
should process it.

Simple questions may be sent to smaller and faster models, while
complex questions may be sent to more capable models.

If a cloud provider becomes temporarily unavailable, the router
should be able to send the request to another available model.

The company's goal is not to find one model that is best at
everything. Instead, it wants to understand the strengths,
weaknesses, costs, speed, privacy characteristics, and reliability
of different AI deployment approaches.

QUESTIONS:

1. What is NovaTech building?

2. What are the three AI deployment approaches being tested?

3. List the eight factors the engineering team decided to measure.

4. What is the difference between an AI model and an AI provider
   according to the passage?

5. Why does NovaTech want to build an AI routing system?

6. According to the passage, what should happen if a cloud
   provider becomes temporarily unavailable?

Answer using ONLY information from the passage."""
}


def check_json_validity(response_text: str) -> str:
    """
    Checks if the response text contains valid JSON.
    Returns 'Yes' or 'No'.
    """
    if not response_text:
        return "No"
    
    cleaned = response_text.strip()
    # Handle markdown code blocks if present
    if cleaned.startswith("```"):
        lines = cleaned.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()

    try:
        json.loads(cleaned)
        return "Yes"
    except json.JSONDecodeError:
        return "No"


def run_gemini_test(test_name: str, prompt: str) -> dict:
    provider = "Google Gemini"
    model_name = os.getenv("GEMINI_MODEL_NAME", "gemini-3.5-flash")
    api_key = os.getenv("GEMINI_API_KEY")

    result = {
        "Test": test_name,
        "Provider": provider,
        "Model": model_name,
        "Prompt": prompt,
        "Response": "",
        "Response Time Seconds": "N/A",
        "Input Tokens": "N/A",
        "Output Tokens": "N/A",
        "Total Tokens": "N/A",
        "JSON Valid": "N/A"
    }

    if not api_key or api_key == "your_api_key_here":
        result["Response"] = "Error: GEMINI_API_KEY not set properly."
        return result

    try:
        client = genai.Client(api_key=api_key)
        start_time = time.perf_counter()
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
        )
        end_time = time.perf_counter()
        
        result["Response Time Seconds"] = round(end_time - start_time, 4)
        result["Response"] = response.text if hasattr(response, "text") else str(response)

        if hasattr(response, "usage_metadata") and response.usage_metadata:
            usage = response.usage_metadata
            result["Input Tokens"] = getattr(usage, "prompt_token_count", "N/A")
            result["Output Tokens"] = getattr(usage, "candidates_token_count", "N/A")
            result["Total Tokens"] = getattr(usage, "total_token_count", "N/A")

        if "TEST 4" in test_name:
            result["JSON Valid"] = check_json_validity(result["Response"])

    except APIError as e:
        result["Response"] = f"API Error: {e}"
    except Exception as e:
        result["Response"] = f"Unexpected Error: {e}"

    return result


def run_groq_test(test_name: str, prompt: str) -> dict:
    provider = "Groq"
    model_name = "openai/gpt-oss-120b"
    api_key = os.getenv("GROQ_API_KEY")

    result = {
        "Test": test_name,
        "Provider": provider,
        "Model": model_name,
        "Prompt": prompt,
        "Response": "",
        "Response Time Seconds": "N/A",
        "Input Tokens": "N/A",
        "Output Tokens": "N/A",
        "Total Tokens": "N/A",
        "JSON Valid": "N/A"
    }

    if not api_key or api_key == "your_api_key_here":
        result["Response"] = "Error: GROQ_API_KEY not set properly."
        return result

    try:
        client = Groq(api_key=api_key)
        start_time = time.perf_counter()
        completion = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
        )
        end_time = time.perf_counter()

        result["Response Time Seconds"] = round(end_time - start_time, 4)
        result["Response"] = completion.choices[0].message.content

        if hasattr(completion, "usage") and completion.usage:
            usage = completion.usage
            result["Input Tokens"] = getattr(usage, "prompt_tokens", "N/A")
            result["Output Tokens"] = getattr(usage, "completion_tokens", "N/A")
            result["Total Tokens"] = getattr(usage, "total_tokens", "N/A")

        if "TEST 4" in test_name:
            result["JSON Valid"] = check_json_validity(result["Response"])

    except GroqError as e:
        result["Response"] = f"Groq API Error: {e}"
    except Exception as e:
        result["Response"] = f"Unexpected Error: {e}"

    return result


def run_huggingface_test(test_name: str, prompt: str) -> dict:
    provider = "Hugging Face"
    model_name = "Qwen/Qwen2.5-72B-Instruct"
    token = os.getenv("HF_TOKEN")

    result = {
        "Test": test_name,
        "Provider": provider,
        "Model": model_name,
        "Prompt": prompt,
        "Response": "",
        "Response Time Seconds": "N/A",
        "Input Tokens": "N/A",
        "Output Tokens": "N/A",
        "Total Tokens": "N/A",
        "JSON Valid": "N/A"
    }

    if not token or token == "your_api_key_here":
        result["Response"] = "Error: HF_TOKEN not set properly."
        return result

    try:
        client = InferenceClient(model=model_name, token=token)
        start_time = time.perf_counter()
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024,
        )
        end_time = time.perf_counter()

        result["Response Time Seconds"] = round(end_time - start_time, 4)
        result["Response"] = completion.choices[0].message.content

        if hasattr(completion, "usage") and completion.usage:
            usage = completion.usage
            result["Input Tokens"] = getattr(usage, "prompt_tokens", "N/A")
            result["Output Tokens"] = getattr(usage, "completion_tokens", "N/A")
            result["Total Tokens"] = getattr(usage, "total_tokens", "N/A")

        if "TEST 4" in test_name:
            result["JSON Valid"] = check_json_validity(result["Response"])

    except HfHubHTTPError as e:
        result["Response"] = f"Hugging Face API Error: {e}"
    except Exception as e:
        result["Response"] = f"Unexpected Error: {e}"

    return result


def run_openrouter_test(test_name: str, prompt: str) -> dict:
    provider = "OpenRouter"
    model_name = "openrouter/free"
    api_key = os.getenv("OPENROUTER_API_KEY")

    result = {
        "Test": test_name,
        "Provider": provider,
        "Model": model_name,
        "Prompt": prompt,
        "Response": "",
        "Response Time Seconds": "N/A",
        "Input Tokens": "N/A",
        "Output Tokens": "N/A",
        "Total Tokens": "N/A",
        "JSON Valid": "N/A"
    }

    if not api_key or api_key == "your_api_key_here":
        result["Response"] = "Error: OPENROUTER_API_KEY not set properly."
        return result

    try:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )
        start_time = time.perf_counter()
        completion = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
        )
        end_time = time.perf_counter()

        result["Response Time Seconds"] = round(end_time - start_time, 4)
        result["Response"] = completion.choices[0].message.content

        if hasattr(completion, "usage") and completion.usage:
            usage = completion.usage
            result["Input Tokens"] = getattr(usage, "prompt_tokens", "N/A")
            result["Output Tokens"] = getattr(usage, "completion_tokens", "N/A")
            result["Total Tokens"] = getattr(usage, "total_tokens", "N/A")

        if "TEST 4" in test_name:
            result["JSON Valid"] = check_json_validity(result["Response"])

    except OpenAIError as e:
        result["Response"] = f"OpenRouter API Error: {e}"
    except Exception as e:
        result["Response"] = f"Unexpected Error: {e}"

    return result


def run_test_5():
    """
    Runs ONLY Test 5 (Long Context) across all four providers
    and saves the results to day5_test5_results.json and day5_test5_results.csv.
    """
    test_name = TEST_5["name"]
    prompt = TEST_5["prompt"]
    all_results = []

    print(f"\n==================== {test_name} ====================")
    print(f"Prompt length: {len(prompt)} characters\n")

    # 1. Gemini
    print(f"Running Google Gemini...")
    res_gemini = run_gemini_test(test_name, prompt)
    all_results.append(res_gemini)
    print_result_summary(res_gemini)

    # 2. Groq
    print(f"Running Groq...")
    res_groq = run_groq_test(test_name, prompt)
    all_results.append(res_groq)
    print_result_summary(res_groq)

    # 3. Hugging Face
    print(f"Running Hugging Face...")
    res_hf = run_huggingface_test(test_name, prompt)
    all_results.append(res_hf)
    print_result_summary(res_hf)

    # 4. OpenRouter
    print(f"Running OpenRouter...")
    res_or = run_openrouter_test(test_name, prompt)
    all_results.append(res_or)
    print_result_summary(res_or)

    # Save Test 5 results to dedicated JSON and CSV files
    json_filename = "day5_test5_results.json"
    csv_filename = "day5_test5_results.csv"

    print(f"\nSaving Test 5 results to {json_filename} and {csv_filename}...")

    # Save JSON
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=4, ensure_ascii=False)

    # Save CSV
    csv_columns = [
        "Test",
        "Provider",
        "Model",
        "Prompt",
        "Response",
        "Response Time Seconds",
        "Input Tokens",
        "Output Tokens",
        "Total Tokens",
        "JSON Valid"
    ]

    with open(csv_filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        writer.writeheader()
        for data in all_results:
            writer.writerow(data)

    print("Test 5 completed successfully.")


def main():
    # By default or when run directly, you can run all tests or check arguments.
    # To run ONLY Test 5 as requested:
    run_test_5()


def print_result_summary(res: dict):
    print(f"  Provider     : {res['Provider']}")
    print(f"  Model        : {res['Model']}")
    print(f"  Response Time: {res['Response Time Seconds']} seconds")
    print(f"  Tokens       : In={res['Input Tokens']}, Out={res['Output Tokens']}, Total={res['Total Tokens']}")
    if res['JSON Valid'] != "N/A":
        print(f"  JSON Valid   : {res['JSON Valid']}")
    print("-" * 50)


if __name__ == "__main__":
    main()



