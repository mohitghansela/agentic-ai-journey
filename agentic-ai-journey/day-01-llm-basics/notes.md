# Day 1 - LLM Basics

## What is LLM?
Large Language Model trained on huge text data.

## How it works?
- Input → Tokenization
- Tokens → Embeddings
- Transformer processes
- Output generated

## Practical - Tokenization using tiktoken

- Used tiktoken library for real LLM tokenization
- Tokens are not words, they are subword units
- Model understands numbers (token IDs), not raw text

## Observation
- Token output is numbers (IDs)
- Same text can produce different tokens

## Experiment
Short vs long words → different token counts
