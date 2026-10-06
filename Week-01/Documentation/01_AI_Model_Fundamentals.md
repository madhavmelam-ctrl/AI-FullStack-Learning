# Day 1 — AI Model Fundamentals

## Objective

The objective of Day 1 was to understand the basic AI model ecosystem and learn what happens between a user's question and an AI-generated response.

---

## 1. Artificial Intelligence (AI)

Artificial Intelligence is the broad field of creating computer systems that can perform tasks that normally require human intelligence.

Examples include:
- Understanding language
- Recognizing images
- Solving problems
- Generating text
- Making predictions

---

## 2. Machine Learning (ML)

Machine Learning is a branch of AI where computers learn patterns from data instead of being explicitly programmed for every situation.

Example:

A spam detection system can learn from thousands of emails and identify whether a new email is spam.

---

## 3. Deep Learning

Deep Learning is a type of Machine Learning that uses neural networks with many layers.

It is commonly used in:
- Large Language Models
- Image recognition
- Speech recognition
- Generative AI

---

## 4. Generative AI

Generative AI is AI that can create new content.

It can generate:
- Text
- Code
- Images
- Audio
- Video

Examples include AI assistants and AI coding tools.

---

## 5. Large Language Model (LLM)

An LLM is an AI model trained on large amounts of text data.

It learns patterns in language and can generate responses based on the input it receives.

LLMs can be used for:
- Question answering
- Coding
- Summarization
- Translation
- Content generation
- Reasoning tasks

---

## 6. Transformer

A Transformer is a neural network architecture widely used in modern language models.

Transformers are effective at understanding relationships between different parts of an input sequence.

A major concept used by Transformers is **attention**.

---

## 7. Neural Network

A neural network is a computing system inspired by the way biological neurons process information.

It consists of interconnected layers that learn patterns from data.

Deep Learning models use neural networks with many layers.

---

## 8. Parameters

Parameters are numerical values inside an AI model that are learned during training.

They help determine how the model processes input and generates output.

Models can contain millions or billions of parameters.

---

## 9. Tokens

AI language models do not directly process text as complete sentences.

The text is divided into smaller units called **tokens**.

A token may represent:
- A word
- Part of a word
- A number
- Punctuation

The model processes these tokens to understand input and generate output.

---

## 10. Context Window

The context window is the amount of information a model can process at one time.

It includes information such as:
- User prompts
- Previous conversation content
- Instructions
- Documents
- Generated responses

A larger context window allows the model to work with more information at once.

---

## 11. Inference

Inference is the process of using a trained AI model to generate a response.

Example:

User asks a question  
↓  
Model processes the input  
↓  
Model generates an answer

The model is performing inference when it generates the answer.

---

## 12. Training

Training is the process where an AI model learns patterns from large amounts of data.

During training, the model's parameters are adjusted so that it becomes better at predicting appropriate outputs.

---

## 13. Fine-Tuning

Fine-tuning means taking an already trained model and training it further on specialized data.

For example, a general model could be fine-tuned using customer-support data to make it better at customer-support tasks.

---

## 14. Quantization

Quantization reduces the numerical precision used to represent a model's parameters.

This can reduce:
- Memory usage
- Storage requirements
- Hardware requirements

Quantized models can therefore be easier to run on local computers.

---

## 15. Multimodal AI

Multimodal AI can work with more than one type of information.

For example, a multimodal model may process:
- Text
- Images
- Audio
- Video

---

# AI Application Architecture

The basic architecture I learned is:

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

## Explanation

The user sends a request through an application.

The application uses an AI framework or SDK to communicate with an AI model.

The model may be accessed through a cloud API or through a local runtime.

The model performs inference and generates a response.

The response is returned to the application and displayed to the user.

---

# AI Model Capabilities

AI models can be grouped by the type of tasks or data they support.

AI Model

├── Text  
├── Code  
├── Vision  
├── Audio  
├── Image  
└── Multimodal

### Text
Models that understand and generate text.

### Code
Models that can understand, generate, explain, and debug programming code.

### Vision
Models that can understand and analyze images.

### Audio
Models that can process speech and other audio.

### Image
Models that can generate or manipulate images.

### Multimodal
Models that can work with multiple types of data such as text, images, and audio.

---

# What is an AI Model?

An AI model is a trained computational system that has learned patterns from data.

After training, the model can receive input and generate predictions or responses.

For language models, the input is converted into tokens. The model processes those tokens and predicts appropriate output tokens to generate a response.

---

# How Does an Application Communicate with an AI Model?

An application can communicate with an AI model mainly in two ways:

## Cloud API

The application sends a request over the internet to an AI provider.

Example flow:

Application  
↓  
API Request  
↓  
Cloud AI Model  
↓  
Generated Response  
↓  
Application

## Local Runtime

The AI model is downloaded and executed on the user's own computer using software such as a local AI runtime.

Example flow:

Application  
↓  
Local Runtime  
↓  
Local AI Model  
↓  
Generated Response  
↓  
Application

---

# What I Learned on Day 1

On Day 1, I learned the fundamental concepts behind modern AI systems, including AI, Machine Learning, Deep Learning, Generative AI, LLMs, Transformers, neural networks, parameters, tokens, context windows, inference, training, fine-tuning, quantization, and multimodal AI.

I also learned how an application communicates with an AI model through either a cloud API or a local runtime and how the generated response returns to the user.

