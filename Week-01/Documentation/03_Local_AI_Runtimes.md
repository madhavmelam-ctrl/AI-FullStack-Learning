# Day 3 — Local AI Runtimes

## Objective

The objective of Day 3 was to understand how open AI models can be downloaded and executed locally instead of using only cloud APIs.

I researched major tools used for running AI models locally or on self-managed infrastructure.

The tools studied were:

- Ollama
- llama.cpp
- LM Studio
- Hugging Face Transformers
- vLLM

---

# What is a Local AI Runtime?

A local AI runtime is software that allows an AI model to run on a user's own computer or server.

Instead of:

Application
↓
Internet
↓
Cloud AI API
↓
AI Model

we can use:

Application
↓
Local AI Runtime
↓
Local AI Model
↓
Response

This can reduce dependence on external cloud APIs.

---

# 1. Ollama

Ollama is a tool that makes it easier to download, run and manage AI models locally.

It provides a simple command-line interface and a local API.

Example:

ollama run llama3.2:1b

Ollama can run models such as:

- Llama
- Qwen
- Gemma
- DeepSeek
- Phi
- Mistral

During my practical experiment, I used Ollama on Windows.

The local API was available at:

http://localhost:11434

This means another application, such as a Python program, can communicate with the locally running model.

---

# 2. llama.cpp

llama.cpp is an open-source project designed to run large language models efficiently on local hardware.

It is commonly associated with GGUF model files and supports quantized models.

Advantages include:

- CPU execution
- GPU acceleration options
- Quantized models
- Lower hardware requirements
- Local inference

It is useful when developers want more control over local model execution.

---

# 3. LM Studio

LM Studio provides a graphical interface for downloading and running AI models locally.

It is useful for users who prefer a GUI instead of mainly using command-line tools.

It can be used to:

- Search for models
- Download models
- Run local chats
- Configure model settings
- Provide a local API/server

LM Studio is useful for experimenting with local models without requiring extensive command-line knowledge.

---

# 4. Hugging Face Transformers

Transformers is a library from Hugging Face that allows developers to work with many pretrained AI models using programming languages such as Python.

It provides greater programmatic control over:

- Model loading
- Tokenization
- Inference
- Generation settings
- AI application development

Compared with tools such as Ollama and LM Studio, Transformers often requires more Python and machine-learning knowledge.

---

# 5. vLLM

vLLM is an inference and serving system designed for efficiently serving large language models.

It is especially useful when models need to serve multiple requests efficiently on suitable hardware.

It is more focused on high-performance model serving than beginner-level desktop experimentation.

---

# Local AI Tool Comparison

| Tool | Main Purpose | Interface | Beginner Friendly | Local API | Typical Use |
|---|---|---|---|---|---|
| Ollama | Run local models easily | CLI/API | Yes | Yes | Local development |
| llama.cpp | Efficient local inference | CLI/Library | Medium | Possible | Lightweight/custom inference |
| LM Studio | Desktop local AI | GUI | Yes | Yes | Easy model experimentation |
| Hugging Face Transformers | Programmatic AI development | Python | Medium | Application dependent | Model development/testing |
| vLLM | High-performance model serving | Server/API | Advanced | Yes | Production inference |

---

# Practical Experiment with Ollama

I installed Ollama on Windows and downloaded several models.

Models used during the experiment included:

- llama3.2:1b
- qwen3:4b
- gemma3:1b
- deepseek-r1:1.5b
- phi4-mini

This allowed me to compare different open models running locally.

I also learned that larger models generally require more RAM, storage and computing resources.

---

# Local API

One important concept I learned was that a local AI model can still be accessed through an API.

For example:

Python Application
↓
HTTP Request
↓
Ollama Local API
↓
Local AI Model
↓
Generated Response
↓
Python Application

Therefore, an AI application does not always need to communicate with a cloud provider.

It can communicate with a model running on the same computer.

---

# Local vs Cloud AI

## Local AI

Advantages:

- Greater control
- Can avoid per-request API charges
- Data can remain on local hardware
- Can work without depending on a cloud AI provider

Limitations:

- Requires suitable hardware
- Large models can be slow
- Requires local setup
- User manages the models and runtime

## Cloud AI

Advantages:

- Easy access to powerful models
- Provider manages infrastructure
- No need to download large model files
- Easier to scale in many situations

Limitations:

- Requires internet access
- API limits may apply
- Usage can cost money
- Requests are processed by an external service

---

# What I Learned on Day 3

I learned that open AI models can be executed locally using different AI runtimes.

I researched Ollama, llama.cpp, LM Studio, Hugging Face Transformers and vLLM.

I also practically used Ollama to download and run multiple AI models on Windows.

The most important concept I learned was that a locally running model can expose an API, allowing normal applications to communicate with it in a similar way to a cloud AI API.

---

# What I Did on Day 3

- Installed and used Ollama.
- Downloaded multiple local AI models.
- Tested local model execution.
- Explored model context settings.
- Learned how the Ollama local API works.
- Compared major local AI runtimes.