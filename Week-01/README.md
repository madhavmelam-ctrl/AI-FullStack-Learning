# AI Full-Stack Learning — Week 01

## Overview

Week 1 focused on understanding the AI model ecosystem and learning how AI models can be used inside applications.

The week included both theoretical research and practical experiments with local AI models and cloud AI APIs.

Topics covered included:

- AI and Machine Learning fundamentals
- Large Language Models
- Transformers
- Tokens and context windows
- Inference and training
- Fine-tuning and quantization
- Multimodal AI
- Open-weight AI models
- Local AI runtimes
- Cloud AI APIs
- API authentication and security
- Token usage
- Model comparison
- Response-time measurement
- Structured output
- Long-context testing

---

## Week 01 Project Structure

```text
Week-01/
│
├── Documentation/
│   ├── 01_AI_Model_Fundamentals.md
│   ├── 02_Free_AI_Models.md
│   ├── 03_Local_AI_Runtimes.md
│   ├── 04_Free_AI_APIs.md
│   └── 05_Model_Comparison.md
│
├── Research/
│   ├── AI_Model_Comparison.xlsx
│   └── AI_Tool_Comparison.xlsx
│
├── Experiments/
│   ├── local_ai_test.py
│   ├── api_test.py
│   └── model_comparison.py
│
└── README.md
```

---

## Day 1 — AI Model Fundamentals

Day 1 focused on understanding the basic AI model ecosystem.

Concepts studied included:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Generative AI
- Large Language Models
- Transformers
- Neural Networks
- Parameters
- Tokens
- Context Windows
- Inference
- Training
- Fine-tuning
- Quantization
- Multimodal AI

The basic application architecture studied was:

User  
↓  
Application  
↓  
AI Framework / SDK  
↓  
API or Local Runtime  
↓  
AI Model  
↓  
Inference  
↓  
Response  
↓  
Application  
↓  
User

---

## Day 2 — Free and Open AI Models

Day 2 focused on researching major AI model families.

Models researched included:

- Llama
- Qwen
- Gemma
- Mistral
- DeepSeek
- Phi

An important concept learned was:

**Free to download does not necessarily mean free API access.**

Open-weight models can often be downloaded and executed locally, while cloud APIs may provide only limited free quotas.

Several models were also downloaded and tested locally using Ollama.

---

## Day 3 — Local AI Runtimes

Day 3 focused on tools used to run AI models locally.

Tools researched included:

- Ollama
- llama.cpp
- LM Studio
- Hugging Face Transformers
- vLLM

Ollama was installed and used for practical experiments.

The local Ollama API was accessed through:

```text
http://localhost:11434
```

The `local_ai_test.py` experiment successfully sent a prompt to a locally running model and recorded the generated response, response time and token information.

---

## Day 4 — Free AI APIs

Day 4 focused on cloud AI APIs.

Providers explored included:

- Google Gemini
- Groq
- Hugging Face
- OpenRouter
- Mistral AI

The experiments covered:

- API authentication
- Environment variables
- Python SDKs
- API requests
- Model selection
- Token usage
- Rate limits
- Provider errors
- Streaming
- Tool calling
- Vision capabilities
- API security

The `api_test.py` experiment successfully connected a Python application to a cloud AI model and recorded the response and token usage.

---

## Day 5 — AI Model Research Lab

Day 5 focused on comparing different AI models/providers using practical experiments.

The research lab tested:

1. General knowledge
2. Coding
3. Reasoning
4. Structured JSON output
5. Long-context understanding

Providers/models used in the comparison included:

- Google Gemini
- Groq
- Hugging Face
- OpenRouter

For each experiment, information such as response time and token usage was recorded.

The experiments demonstrated that model selection should be based on application requirements rather than assuming that one model is best for every task.

---

## Experiments

### local_ai_test.py

Tests a locally running Ollama model through its HTTP API.

The experiment records:

- AI response
- Response time
- Input tokens
- Output tokens

### api_test.py

Tests a cloud AI API from Python.

The experiment demonstrates:

- API authentication
- Environment variables
- Prompt submission
- AI response handling
- Response-time measurement
- Token usage

### model_comparison.py

Runs the AI Model Research Lab.

The experiment compares multiple AI providers using different prompt categories and records performance information.

---

## Research Files

### AI_Model_Comparison.xlsx

Contains research comparing major AI model families such as:

- Llama
- Qwen
- Gemma
- Mistral
- DeepSeek
- Phi

### AI_Tool_Comparison.xlsx

Contains research comparing local AI tools such as:

- Ollama
- llama.cpp
- LM Studio
- Hugging Face Transformers
- vLLM

---

## Security

API keys must never be hardcoded into Python source files.

API credentials are stored using environment variables in a local `.env` file.

The `.env` file must not be uploaded to a public repository.

Example:

```text
GEMINI_API_KEY=your_api_key
```

The actual API key is intentionally not included in this repository.

---

## Key Learning

The most important learning from Week 1 is that an AI application consists of more than just an AI model.

A complete AI application may involve:

Application  
↓  
AI SDK / Framework  
↓  
Local Runtime or Cloud API  
↓  
AI Model  
↓  
Inference  
↓  
Response

Different models and providers have different strengths, limitations, hardware requirements, context capabilities, response times, token usage and availability.

Therefore, AI models should be evaluated using practical application-specific experiments before selecting them for a project.

---

## Week 01 Status

**Completed**

Week 1 documentation, research and practical AI experiments were completed successfully.


## Git Practice

Learning Git and GitHub practically.

### Feature Branch Test

This text was created inside the feature/git-learning branch.