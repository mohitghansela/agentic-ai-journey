# 📚 Day 1 - LLM Fundamentals

## 🧠 What is LLM?

LLM (Large Language Model) is a deep learning model trained on massive amounts of text data.

It learns patterns in language and predicts the **next token (word/subword)** based on context.

Example:
"I love playing ___" → Model predicts: "cricket"

---

## ⚙️ How LLM Works?

1. Input text is provided
2. Text is converted into **tokens**
3. Tokens are converted into **embeddings (vectors)**
4. Passed through **Transformer layers**
5. Model predicts next token
6. Output is generated token-by-token

---

## 🔤 What is Tokenization?

Tokenization is the process of breaking text into smaller units called **tokens**.

* Tokens are not always full words
* They can be subwords or parts of words
* Each token is converted into a numerical ID

Example:
"Hello AI" → [token IDs]

💡 Important:
LLMs do not understand text directly — they work on numbers (tokens).

---

## 🤖 GPT Full Form

**GPT = Generative Pre-trained Transformer**

* **Generative** → generates text
* **Pre-trained** → trained on large datasets
* **Transformer** → uses transformer architecture

---

## 🚀 Transformer Breakthrough

Before transformers, models like RNNs and LSTMs were used:

❌ Problems:

* Slow (sequential processing)
* Hard to handle long context
* Memory limitations

✅ Transformers solved this by:

* Processing all tokens **in parallel**
* Capturing long-range relationships
* Using **attention mechanism**

👉 This breakthrough made modern LLMs possible.

---

## 📊 Vector Embeddings

Embeddings convert tokens into **vectors (lists of numbers)**.

* Each token → vector representation
* Similar words → similar vectors

Example:

* "King" ≈ "Queen"
* "Dog" ≠ "Car"

💡 Embeddings help the model understand **meaning and relationships** between words.

---

## 📍 Positional Encoding

Transformers process tokens in parallel, so they don't know the order of words.

Positional encoding is added to embeddings to provide:

* Position of each word in a sentence

Example:
"I love AI" ≠ "AI love I"

💡 Without positional encoding, model cannot understand sequence order.

---

## 🎯 Multi-Head Attention

### 🔍 What is Attention?

Attention allows the model to focus on important words in a sentence.

Example:
"The animal didn't cross the road because it was tired"

👉 "it" refers to "animal"

---

### ⚡ What is Multi-Head Attention?

Instead of using a single attention mechanism, transformers use multiple attention heads.

Each head focuses on different aspects:

* One focuses on grammar
* One on meaning
* One on relationships

💡 This improves understanding of complex language patterns.

---

## 🧪 Practical - Tokenization using tiktoken

* Used `tiktoken` library for real LLM tokenization
* Converted text → tokens using `encode()`
* Converted tokens → text using `decode()`

---

## 🔍 Observations

* Tokens are numerical IDs
* Tokenization is not always word-by-word
* Same sentence can be split differently
* Longer text produces more tokens

---

## 💡 Final Pipeline (Complete Flow)

Text → Tokenization → Embeddings → Positional Encoding → Transformer (Multi-Head Attention) → Output Tokens

---

## 🧠 Key Takeaways

* LLM predicts next token using probability
* Tokens are the core unit of processing
* Transformers are the backbone of modern AI
* Attention mechanism is the most powerful concept
* Embeddings help represent meaning
* Positional encoding helps maintain word order

---
🚀 API Setup & Integration (OpenAI)
🧠 What is OpenAI API?

OpenAI API allows your code to interact with AI models like GPT.

👉 You can:

Generate text
Build chatbots
Create AI apps
🔑 API Key

API key is a secret token used for authentication.

Identifies your account
Tracks usage

⚠️ Never share it publicly

💰 Billing Setup
Added ~$5 credit
Required to use API
Without credits → error (429)
⚙️ Project Setup
📁 Folder Structure
hello_world/
│── 01.py
│── .env
🔧 Virtual Environment
Create
python -m venv venv
Activate (PowerShell)
.\venv\Scripts\Activate
📦 Install Dependencies
pip install openai python-dotenv
📁 .env File
OPENAI_API_KEY=your_api_key_here

💡 Keeps API key secure

🤖 First OpenAI Program
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Create client
client = OpenAI()

# Send request
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Hey There I am Mohit Ghansela"}
    ]
)

# Print response
print(response.choices[0].message.content)
⚙️ Code Explanation
load_dotenv()

Loads API key from .env

OpenAI()

Creates client to connect with OpenAI

chat.completions.create()

Sends request to model

model="gpt-4o-mini"
Fast
Low cost
Beginner friendly
messages
{"role": "user", "content": "Hello"}
response.choices[0].message.content

Extracts model output

❌ Errors Faced & Fixes
🔴 Module Not Found
pip install openai python-dotenv
🔴 401 Authentication Error
Cause: wrong/restricted key
Fix: generate new key
🔴 429 Quota Error
Cause: no credits
Fix: add billing
🔴 Env Not Loading
Fix:
from dotenv import load_dotenv
load_dotenv()
💡 Best Practices
Use .env for API key ✅
Use virtual environment ✅
Don’t hardcode secrets ❌
Add .env to .gitignore ✅
🔄 Integration Flow
User Input → Python Code → OpenAI API → Model → Response → Output
