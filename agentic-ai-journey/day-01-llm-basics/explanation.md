# 🧠 My Understanding of Tokenization

Tokenization is a fundamental step in how Large Language Models (LLMs) process text.

LLMs do not understand raw text like humans. Instead, they convert text into **tokens**, which are numerical representations of smaller pieces of text (words, subwords, or characters).

---

## 🔍 Why Tokenization is Important

* Models can only process numbers, not text
* Tokenization converts text → numbers
* All computations inside the model happen on these numbers

---

## ⚙️ Code Explanation

### 1. Importing the Library

```python
import tiktoken
```

We use the `tiktoken` library, which provides tokenizers used by modern LLMs.

---

### 2. Loading the Tokenizer

```python
enc = tiktoken.encoding_for_model("gpt-4o")
```

This line loads the tokenizer specific to the **GPT-4o model**.

Different models use different tokenization strategies, so using the correct tokenizer is important.

---

### 3. Input Text

```python
text = "Hey There! My name is Mohit Ghansela"
```

This is the raw text that we want to process.

---

### 4. Encoding (Text → Tokens)

```python
tokens = enc.encode(text)
```

* This converts the input text into a list of numbers (token IDs)
* Each number represents a piece of the text

Example:

```
"Hello AI" → [15496, 1234]
```

---

### 5. Printing Tokens

```python
print("Tokens:", tokens)
```

This shows how the model sees the input — as numbers instead of text.

---

### 6. Decoding (Tokens → Text)

```python
decoded_text = enc.decode(tokens)
print("Decoded:", decoded_text)
```

* This converts tokens back into human-readable text
* Helps verify that encoding and decoding are working correctly

---

### 7. Experiment (Understanding Token Behavior)

```python
print(enc.encode("AI"))
print(enc.encode("Artificial Intelligence"))
```

This experiment shows that:

* Short text and long text produce different token counts
* Tokenization is not always word-by-word
* Sometimes a single word can be split into multiple tokens

---

## 🧪 Key Observations

* Tokens are not always equal to words
* LLMs operate entirely on token IDs
* Efficient tokenization helps models understand context better

---

## 💡 Final Insight

Tokenization is the bridge between human language and machine understanding.

Without tokenization, LLMs cannot process or generate meaningful text.
