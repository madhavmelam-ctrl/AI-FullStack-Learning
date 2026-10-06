# Day 2 — Research Free AI Models

## Objective

The objective of Day 2 was to research major free and open-weight AI models that can be used for application development.

The main model families studied were:

- Llama
- Qwen
- Gemma
- Mistral
- DeepSeek
- Phi

---

# Open Models and Free APIs

One of the most important things I learned is that:

**Free to download does not mean free API access.**

These are two different ways of using AI models.

## Local Model

Open Model  
↓  
Download Model  
↓  
Run Locally  
↓  
Use Local CPU/GPU  
↓  
Potentially No API Cost

The model runs on the user's own computer.

The main cost is the hardware and electricity required to run the model.

---

## Cloud API

Cloud Model  
↓  
API Provider  
↓  
Send Request Through Internet  
↓  
Provider Runs Model  
↓  
Receive Response

A cloud provider may offer a free quota, but usage beyond that quota may require payment.

---

# 1. Llama

**Organization:** Meta

Llama is a family of open-weight large language models.

It can be used for tasks such as:

- Text generation
- Question answering
- Coding
- Reasoning
- Application development

Llama models can be downloaded and executed locally using tools such as Ollama.

During the practical experiment, I downloaded and tested:

`llama3.2:1b`

Approximate local download size:

`1.3 GB`

---

# 2. Qwen

**Organization:** Alibaba

Qwen is a family of AI models designed for multiple tasks including text generation, coding and reasoning.

Some Qwen models also support multimodal capabilities.

During the practical experiment, I downloaded:

`qwen3:4b`

Approximate local download size:

`2.5 GB`

Qwen was one of the larger models tested locally during this experiment.

---

# 3. Gemma

**Organization:** Google

Gemma is Google's family of open models.

Gemma models are designed to provide useful AI capabilities while also having smaller variants that can run on local hardware.

During the practical experiment, I downloaded:

`gemma3:1b`

Approximate local download size:

`815 MB`

This made it one of the smaller models tested during the experiment.

---

# 4. Mistral

**Organization:** Mistral AI

Mistral provides AI models designed for language understanding, generation, coding and reasoning.

Mistral models can be used through APIs, and some models can also be downloaded and run using local AI tools.

A Mistral 7B model was considered during the local-model experiment, but the download was not completed.

---

# 5. DeepSeek

**Organization:** DeepSeek

DeepSeek develops models focused on capabilities such as reasoning and coding.

During the practical experiment, I downloaded:

`deepseek-r1:1.5b`

Approximate local download size:

`1.1 GB`

This allowed me to experiment with a smaller reasoning-focused model locally.

---

# 6. Phi

**Organization:** Microsoft

Phi is Microsoft's family of small language models.

These models are designed to provide useful AI capabilities while being smaller than many very large LLMs.

During the practical experiment, I downloaded:

`phi4-mini`

Approximate local download size:

`2.5 GB`

---

# Model Comparison

| Model Family | Organization | Open-Weight Models | Text | Coding | Reasoning | Local Execution |
|---|---|---|---|---|---|---|
| Llama | Meta | Yes | Yes | Yes | Yes | Yes |
| Qwen | Alibaba | Yes | Yes | Yes | Yes | Yes |
| Gemma | Google | Yes | Yes | Yes | Yes | Yes |
| Mistral | Mistral AI | Yes | Yes | Yes | Yes | Yes |
| DeepSeek | DeepSeek | Yes | Yes | Yes | Yes | Yes |
| Phi | Microsoft | Yes | Yes | Yes | Yes | Yes |

Exact capabilities depend on the specific model and version selected.

---

# Model Size

AI model families contain different model sizes.

For example:

1B = approximately one billion parameters  
4B = approximately four billion parameters  
7B = approximately seven billion parameters

Generally, larger models require more:

- RAM
- GPU memory
- Storage
- Computing power

Smaller and quantized models are therefore useful for running AI locally on normal computers.

---

# Quantized Models

Quantization reduces the precision used to store model parameters.

This can reduce:

- Model file size
- RAM usage
- GPU memory requirements

This makes larger AI models easier to run on consumer hardware.

There can sometimes be a trade-off between reduced resource usage and model quality.

---

# Context Length

Context length determines how much information a model can process in a single interaction.

During local experiments in VS Code, different models displayed different supported context values.

The exact usable context can depend on:

- Model
- Model version
- Runtime
- Hardware
- Configuration

Therefore, model documentation should be checked before choosing a model for an application.

---

# Hardware Requirements

Local model hardware requirements depend on:

- Number of parameters
- Quantization
- Context length
- CPU performance
- Available RAM
- GPU
- GPU memory

Small models can often run on CPU-based computers, although generation may be slower.

Larger models benefit significantly from GPU acceleration.

---

# Practical Experiment

I installed Ollama on Windows and used it to download and test multiple models locally.

Models downloaded during the experiment included:

- llama3.2:1b
- qwen3:4b
- gemma3:1b
- deepseek-r1:1.5b
- phi4-mini

This experiment demonstrated that open models can be downloaded and executed locally without sending every request to a paid cloud API.

---

# Local Models vs Cloud Models

## Local Models

Advantages:

- Can work without paying per API request
- Greater control over model execution
- Data can remain on the local machine
- Useful for experimentation

Limitations:

- Requires sufficient hardware
- Larger models can be slow
- Model files consume storage
- User is responsible for setup and maintenance

## Cloud Models

Advantages:

- Powerful infrastructure
- Easy API integration
- No need to run large models locally
- Can provide access to larger models

Limitations:

- Internet connection is required
- Free quotas may be limited
- Usage may eventually cost money
- Data is sent to an external service

---

# What I Learned on Day 2

I learned that an AI model being open-weight or free to download does not automatically mean that its cloud API is free.

I researched major model families including Llama, Qwen, Gemma, Mistral, DeepSeek and Phi.

I also learned how model size, context length, quantization and hardware requirements affect local AI execution.

Most importantly, I practically downloaded and experimented with multiple AI models using Ollama.