import tiktoken

# Load tokenizer for GPT model
enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Mohit Ghansela"

# Convert text to tokens
tokens = enc.encode(text)

print("Tokens:", tokens)

# Decode back to text
decoded_text = enc.decode(tokens)
print("Decoded:", decoded_text)

# Experiment
print(enc.encode("AI"))
print(enc.encode("Artificial Intelligence"))
