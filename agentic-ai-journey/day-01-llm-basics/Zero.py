from dotenv import load_dotenv  
from openai import OpenAI  

load_dotenv()  
client = OpenAI()  

# Strong system prompt (strict control)
System_prompt = """
You are a coding assistant.

Rules:
- Only answer programming/coding-related questions (Python, Java, errors, code, etc.)
- Do NOT answer maths or general questions
- If the question is not coding-related, reply exactly:
"Sorry, I can only help with coding questions."

Do not break these rules.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": System_prompt,
        },
        {
            "role": "user",
            "content": "i want you to write a program related to the my name mohit in reverse ",
        }
    ]
)

print(response.choices[0].message.content)