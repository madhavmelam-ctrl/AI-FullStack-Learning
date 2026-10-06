# Day 4 — Free AI APIs

## Objective

The objective of Day 4 was to research AI providers that offer free API access, free quotas, or trial access and understand how an application communicates with an AI model through an API.

The AI providers explored were:

- Google Gemini
- Groq
- Hugging Face
- OpenRouter
- Mistral AI

---

# What is an AI API?

An AI API allows an application to communicate with an AI model over the internet.

The basic architecture is:

User  
↓  
Python Application  
↓  
AI SDK / HTTP Request  
↓  
AI Provider API  
↓  
AI Model  
↓  
Inference  
↓  
JSON Response  
↓  
Python Application  
↓  
User

The application sends information such as:

- Model name
- User prompt
- Generation settings

The AI provider processes the request using the selected model and sends the generated response back to the application.

---

# API Key

Most cloud AI providers use an API key to authenticate requests.

An API key should never be hardcoded directly inside source code.

Instead, it should be stored using an environment variable or a `.env` file.

Example:

```python
import os

api_key = os.getenv("API_KEY")

```

During local development, API keys can be stored in a `.env` file.

The `.env` file should be added to `.gitignore` so that secret API keys are not accidentally uploaded to GitHub.

---

# How Python Communicates with an AI API

The general communication flow is:

Python Application  
↓  
SDK / HTTPS Request  
↓  
AI Provider  
↓  
AI Model  
↓  
Generated Response  
↓  
JSON / SDK Response  
↓  
Python Application

For example, if the application sends:

`Explain recursion in Python.`

the prompt is sent to the AI provider.

The provider sends the prompt to the selected model, performs inference, and returns the generated response to the Python application.

---

# 1. Google Gemini API

Google provides Gemini models that can be accessed programmatically through its AI API and SDK.

During the practical experiment, I connected a Python application to the Gemini API.

I learned how to:

- Configure an API key
- Select a Gemini model
- Send prompts
- Receive generated responses
- Measure response time
- Read token usage
- Handle model availability errors

Gemini was successfully used during the practical experiments.

I also learned that cloud model availability can change, so an application should be able to handle unavailable models.

---

# 2. Groq API

Groq provides cloud inference APIs for supported AI models.

During the practical experiment, I used the Groq Python SDK.

The basic flow was:

Python Application  
↓  
Groq SDK  
↓  
Groq API  
↓  
Selected Model  
↓  
Generated Response

I successfully sent prompts and received responses using Groq.

I also learned that **Groq and Grok are different**.

Groq is an AI inference platform, while Grok is an AI model family associated with xAI.

During the later model-comparison experiment, Groq was used with:

`openai/gpt-oss-120b`

---

# 3. Hugging Face

Hugging Face provides a large ecosystem of AI models and AI development tools.

Models in the Hugging Face ecosystem can be:

- Downloaded
- Run locally
- Used through hosted inference
- Accessed programmatically

During the practical experiment, I used the Hugging Face Python inference client.

Initially, I encountered an SDK method error:

`'ProxyClientChat' object has no attribute 'completion'`

The client call was corrected to use the appropriate chat completions interface.

After correcting the SDK call, the API worked successfully.

During later testing, I used:

`Qwen/Qwen2.5-72B-Instruct`

This experiment taught me that understanding the correct SDK methods is important when integrating AI services.

---

# 4. OpenRouter

OpenRouter provides access to multiple AI models through a common API interface.

This allows developers to access different models using a similar API structure.

During the practical experiment, I connected OpenRouter using an OpenAI-compatible Python client.

An initially selected model endpoint was unavailable and returned an error.

The configuration was then changed to:

`openrouter/free`

After changing the route, the request worked successfully.

I learned that:

- Model availability can change.
- Applications should handle unavailable models.
- Routing services can provide access to different models.
- `openrouter/free` is not one fixed underlying model.

---

# 5. Mistral AI

Mistral AI provides API access to its AI models.

During the practical experiment, I configured the Mistral Python SDK.

The model tested was:

`mistral-small-latest`

The API request reached the service but returned a rate-limit error.

This was still an important practical result because it demonstrated that cloud APIs can reject requests because of provider limits.

Applications therefore need proper error handling.

---

# Free Model Download vs Free API Access

One of the most important concepts I learned was:

**Free to download and free API access are not the same thing.**

## Open / Downloadable Model

Open Model  
↓  
Download  
↓  
Run Locally  
↓  
Use Own Hardware  
↓  
Potentially No Per-Request API Cost

When a model runs locally, the user provides the required hardware resources.

## Cloud API

Application  
↓  
Internet  
↓  
Cloud AI Provider  
↓  
AI Model  
↓  
Response

A cloud provider may provide a free quota.

However, free quotas can have usage and rate limits.

---

# Free Quota

A free quota is an amount of API usage that a provider allows without payment.

A quota may be based on:

- Number of requests
- Number of tokens
- Requests per minute
- Tokens per minute
- Daily usage

Free quotas and limits can change over time.

Therefore, provider documentation should be checked when building an application.

---

# Rate Limits

A rate limit controls how much API usage is allowed during a particular period.

Examples include:

- Requests per minute
- Requests per day
- Input tokens per minute
- Output tokens per minute

If the limit is exceeded, the API may return a rate-limit error.

I encountered this practically while testing the Mistral API.

---

# Input and Output Tokens

## Input Tokens

Input tokens are the tokens sent to the AI model.

They can include:

- User prompt
- Instructions
- Conversation history
- Context
- Documents

## Output Tokens

Output tokens are the tokens generated by the model.

Token usage is important because cloud AI services may use tokens when calculating usage limits and costs.

---

# Streaming

Streaming allows an application to receive the AI response gradually instead of waiting for the entire response to finish.

Example:

AI Model  
↓  
First Part  
↓  
Next Part  
↓  
Next Part  
↓  
Completed Response

Streaming can make an AI application feel more responsive.

---

# Tool Calling

Some AI models support tool or function calling.

This allows an AI model to request an external function or application tool.

Example:

User  
↓  
AI Model  
↓  
Tool Request  
↓  
Application Function / API  
↓  
Tool Result  
↓  
AI Model  
↓  
Final Response

Tool calling is an important concept when building AI agents.

---

# Vision

Some AI models can process images in addition to text.

Example:

User  
↓  
Text + Image  
↓  
Multimodal AI Model  
↓  
Analysis  
↓  
Response

Vision capability depends on the specific model selected.

---

# Error Handling

AI API requests do not always succeed.

During the practical experiments, I encountered different types of errors, including:

- Authentication problems
- Model unavailable / model not found
- Rate-limit errors
- Incorrect SDK method usage
- Provider availability problems

Therefore, AI applications should include error handling.

Example:

```python
try:
    # Send request to AI API
    pass

except Exception as error:
    print("API request failed:", error)
```

Error handling prevents one failed API request from unexpectedly crashing the entire application.

---

# API Security

API keys are sensitive credentials.

Important security practices include:

- Never hardcode API keys in Python files.
- Store API keys in environment variables.
- Use `.env` during local development.
- Add `.env` to `.gitignore`.
- Never upload API keys to GitHub.
- Never include API keys in documentation.
- Revoke and replace an API key if it is accidentally exposed.

Example `.gitignore`:

```text
.env
__pycache__/
*.pyc
```

---

# Provider Comparison

| Provider | Practical Result | Important Learning |
|---|---|---|
| Google Gemini | Successful | API integration, model selection and token usage |
| Groq | Successful | SDK integration and cloud inference |
| Hugging Face | Successful after SDK fix | Hosted inference and SDK debugging |
| OpenRouter | Successful after changing route | Multi-model routing and model availability |
| Mistral AI | Rate-limit error encountered | Rate limits and API error handling |

---

# What I Learned on Day 4

On Day 4, I learned how applications communicate with cloud AI models using APIs.

I understood the architecture:

Python Application  
↓  
SDK / HTTPS Request  
↓  
AI Provider  
↓  
AI Model  
↓  
Inference  
↓  
Response

I learned about:

- API authentication
- API keys
- Environment variables
- Free API quotas
- Rate limits
- Input tokens
- Output tokens
- Streaming
- Tool calling
- Vision capabilities
- Model availability
- Error handling

I also understood that an AI model and an AI provider are not necessarily the same thing.

A model performs AI inference, while a provider supplies the infrastructure and API used to access the model.

---

# What I Did on Day 4

I performed practical API experiments using Python.

I:

- Configured API credentials using environment variables.
- Tested Google Gemini.
- Tested Groq.
- Tested Hugging Face.
- Tested OpenRouter.
- Tested Mistral AI.
- Sent prompts from Python to cloud AI models.
- Received and displayed AI responses.
- Worked with token usage information.
- Debugged an incorrect Hugging Face SDK call.
- Handled unavailable model endpoints.
- Encountered and studied a real rate-limit error.
- Learned how to protect API credentials using `.env` and `.gitignore`.

---

# Key Takeaway

An AI model is the intelligence that generates a response.

An API is the communication mechanism that allows an application to access that intelligence.

Different AI providers have different models, quotas, rate limits, capabilities and availability.

Therefore, when building AI applications, developers must consider model quality, API reliability, security, token usage, limits and error handling.