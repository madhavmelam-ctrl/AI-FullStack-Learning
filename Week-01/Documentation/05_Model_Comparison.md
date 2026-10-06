# Day 5 — AI Model Comparison

## Objective

The objective of Day 5 was to build an AI Model Research Lab and practically compare different AI models/providers using the same types of prompts.

For each test, I recorded:

- Model / Provider
- Response
- Response time
- Input tokens
- Output tokens
- Total token usage
- Quality observations

The models/providers tested were:

- Google Gemini — `gemini-3.5-flash`
- Groq — `openai/gpt-oss-120b`
- Hugging Face — `Qwen/Qwen2.5-72B-Instruct`
- OpenRouter — `openrouter/free`

---

# AI Model Research Lab

The basic experiment architecture was:

Prompt  
↓  
Python Model Research Lab  
↓  
Multiple AI Providers  
↓  
AI Models  
↓  
Responses  
↓  
Response Time + Token Usage + Quality Analysis

This allowed the same type of task to be compared across different AI systems.

---

# Models Tested

| Provider | Model / Route | Model Size Note |
|---|---|---|
| Google Gemini | gemini-3.5-flash | Parameter count not determined in this experiment |
| Groq | openai/gpt-oss-120b | 120B-class model based on model name |
| Hugging Face | Qwen/Qwen2.5-72B-Instruct | 72B-class model based on model name |
| OpenRouter | openrouter/free | Routing option; underlying model may vary |

`openrouter/free` is a routing option rather than one fixed underlying model.

---

# Testing Method

Five different types of tests were performed:

1. General Knowledge
2. Coding
3. Reasoning
4. Structured Output
5. Long Context

The program measured response time using Python and recorded token usage returned by the APIs.

Errors were also recorded so that one failed provider would not stop the complete experiment.

---

# Test 1 — General Knowledge

## Prompt

`Explain recursion in Python.`

## Results

| Provider | Response Time | Input Tokens | Output Tokens | Total Tokens |
|---|---:|---:|---:|---:|
| Gemini | 40.3995 s | 6 | 1242 | 2369 |
| Groq | 4.7061 s | 76 | 2006 | 2082 |
| Hugging Face | 40.2021 s | 14 | 952 | 966 |
| OpenRouter | 5.8743 s | 25 | 720 | 745 |

## Observation

All four services produced useful explanations of recursion.

The responses covered important concepts such as:

- Recursive function calls
- Base case
- Recursive case

Groq produced the fastest response in this particular test.

---

# Test 2 — Coding

## Prompt

`Write a Python function that removes duplicate items from a list.`

## Results

| Provider | Response Time | Input Tokens | Output Tokens | Total Tokens |
|---|---:|---:|---:|---:|
| Gemini | 19.9899 s | 13 | 427 | 994 |
| Groq | 2.0359 s | 83 | 774 | 857 |
| Hugging Face | 16.6406 s | 20 | 369 | 389 |
| OpenRouter | 14.5761 s | 12 | 1687 | 1699 |

## Observation

All providers generated usable Python solutions.

The solutions used approaches such as:

- Using a set
- Using a seen-set
- Preserving the original list order

Groq produced the fastest response in this particular coding test.

---

# Test 3 — Reasoning

## Prompt

`A shop gives a 20% discount on a ₹500 product. What is the final price? Explain your reasoning.`

## Expected Result

20% of ₹500 = ₹100

₹500 - ₹100 = ₹400

Final price = **₹400**

## Results

| Provider | Response Time | Input Tokens | Output Tokens | Total Tokens | Result |
|---|---:|---:|---:|---:|---|
| Gemini | N/A | N/A | N/A | N/A | API unavailable |
| Groq | 0.9941 s | 95 | 252 | 347 | Correct |
| Hugging Face | 6.0864 s | 35 | 201 | 236 | Correct |
| OpenRouter | 1.3370 s | 24 | 192 | 216 | Correct |

## Observation

Groq, Hugging Face and OpenRouter correctly calculated the final price as ₹400.

Gemini returned a `503 UNAVAILABLE` / high-demand error during this particular test.

This was an API availability failure and should not be considered a reasoning failure by the model.

The Python program continued testing the other providers even though one provider failed.

---

# Test 4 — Structured Output

## Prompt

The models were asked to explain Python lists and return only valid JSON using the required structure:

```json
{
  "title": "",
  "summary": "",
  "keywords": []
}
```

## Results

| Provider | Response Time | Input Tokens | Output Tokens | Total Tokens | JSON Valid |
|---|---:|---:|---:|---:|---|
| Gemini | 16.9301 s | 23 | 114 | 509 | Yes |
| Groq | 0.7783 s | 92 | 174 | 266 | Yes |
| Hugging Face | 3.8835 s | 30 | 115 | 145 | Yes |
| OpenRouter | 1.9631 s | 21 | 431 | 452 | Yes |

## JSON Validation

The program validated the responses using Python JSON parsing.

Example:

```python
import json

try:
    json.loads(response)
    print("Valid JSON")
except json.JSONDecodeError:
    print("Invalid JSON")
```

All four providers successfully returned valid JSON during this test.

This demonstrated that AI output can be programmatically validated before another application uses it.

---

# Test 5 — Long Context

The final experiment tested how the models handled a larger amount of supplied context.

A fictional company called NovaTech was used.

NovaTech was building an AI customer-support platform.

The system:

- Checks a knowledge base
- Retrieves relevant information
- Sends the user's question and retrieved context to an LLM

Three AI deployment approaches were described:

1. Cloud AI APIs
2. Local models using Ollama
3. Open-weight models hosted by external inference providers

NovaTech was comparing eight factors:

1. Response accuracy
2. Response time
3. Token usage
4. Cost
5. Context-window size
6. Hardware requirements
7. Privacy
8. Reliability

The passage also explained the difference between an AI model and an AI provider.

NovaTech planned to build an AI routing system where simple questions could be sent to smaller and faster models while complex questions could be sent to more capable models.

The system would also use fallback behavior if a cloud provider became unavailable.

## Questions

The models were asked:

1. What is NovaTech building?
2. What three AI deployment approaches are being considered?
3. What eight factors are being compared?
4. What is the difference between a model and a provider?
5. Why does NovaTech want to build an AI routing system?
6. What happens if a cloud provider becomes unavailable?

The models were instructed to answer using only the supplied passage.

## Results

| Provider | Response Time | Input Tokens | Output Tokens | Total Tokens |
|---|---:|---:|---:|---:|
| Gemini | 5.3384 s | 611 | 321 | 1845 |
| Groq | 1.9404 s | 650 | 477 | 1127 |
| Hugging Face | 11.1007 s | 591 | 237 | 828 |
| OpenRouter | 7.6432 s | 601 | 779 | 1380 |

## Observation

The long-context test used significantly more input tokens than the shorter tests.

This demonstrated that providing more information or documents to an AI model increases token usage.

Groq produced the fastest response in this particular Test 5 run.

---

# Response Time Comparison

Response time varied significantly between providers.

In these particular experiments, Groq produced the fastest successful response in each measured test.

However, this does not mean that Groq will always be the fastest.

AI response time can depend on:

- Provider load
- Network conditions
- Selected model
- Prompt size
- Context size
- Output length
- Provider infrastructure

Therefore, the results represent this experiment only and should not be treated as a universal model ranking.

---

# Token Usage

Token usage also varied between providers.

Different models and providers may tokenize prompts differently and may report usage differently.

The experiment showed that longer context generally results in higher input-token usage.

Token usage is important because it can affect:

- API limits
- Cost
- Context-window usage
- Application performance

Some API-reported total-token values in the experiment did not equal a simple calculation of input tokens plus output tokens.

The API-reported values were recorded without manually modifying them.

---

# Error Handling

An important part of the research lab was making sure that one provider failure did not stop the entire experiment.

Conceptually:

```python
try:
    # Send request to provider
    # Record response and metrics

except Exception as error:
    # Record error
    # Continue with other providers
```

This was useful when Gemini temporarily returned an availability error during the reasoning test.

Real AI applications should be designed to handle temporary provider failures.

---

# Quality Evaluation

The models/providers were evaluated using practical criteria such as:

- Correctness
- Clarity
- Instruction following
- Coding usefulness
- Reasoning correctness
- JSON validity
- Long-context handling
- Response time
- Token usage
- Reliability

Model evaluation should not depend on only one metric.

For example, the fastest response is not automatically the best response if the quality is poor.

---

# Model vs Provider

An important concept reinforced during this experiment was the difference between an AI model and an AI provider.

## AI Model

The AI model performs inference and generates the response.

## AI Provider

The provider supplies the infrastructure and API that applications use to access models.

The architecture can be represented as:

Application  
↓  
Provider API  
↓  
AI Model  
↓  
Inference  
↓  
Provider  
↓  
Application

This means model performance and provider performance are not always the same thing.

A capable model may still be temporarily inaccessible if the provider experiences an outage or high demand.

---

# Results Storage

The Python benchmark stored the experiment results in machine-readable files.

Tests 1–4 were exported to:

- `day5_model_results.json`
- `day5_model_results.csv`

Test 5 was exported separately to:

- `day5_test5_results.json`
- `day5_test5_results.csv`

Saving results makes it easier to compare models and analyze experiments later.

---

# What I Learned on Day 5

On Day 5, I learned how to compare AI models through practical experiments instead of relying only on model specifications.

I learned how to evaluate AI systems based on:

- Response quality
- Response time
- Token usage
- Coding ability
- Reasoning
- Structured output
- Long-context handling
- Reliability

I also learned that an AI model and an AI provider are different.

A model may be capable of answering a question correctly, while the provider's API may temporarily fail because of high demand or another infrastructure problem.

I also learned that longer context increases token usage and that AI applications need proper error handling.

---

# What I Did on Day 5

I built an AI Model Research Lab using Python.

I:

- Connected multiple AI providers.
- Tested Google Gemini.
- Tested Groq.
- Tested Hugging Face.
- Tested OpenRouter.
- Sent comparable prompts to multiple models/providers.
- Measured response time.
- Recorded input tokens.
- Recorded output tokens.
- Recorded total token usage.
- Tested general knowledge.
- Tested Python coding.
- Tested mathematical reasoning.
- Tested structured JSON output.
- Validated JSON programmatically.
- Performed a long-context test.
- Handled provider errors.
- Exported experiment results to JSON and CSV files.
- Compared the results and recorded observations.

---

# Key Takeaway

There is no single AI model that is automatically best for every application.

The best model depends on the application's requirements.

Important factors include:

- Accuracy
- Quality
- Speed
- Token usage
- Cost
- Context requirements
- Reliability
- Privacy
- Hardware requirements

The best way to choose an AI model is to test suitable models using prompts and workloads that represent the real application.