from dotenv import load_dotenv  
from openai import OpenAI  

load_dotenv()  
client = OpenAI()  

System_prompt = """
You are a coding assistant.
Solve problems in Python only.
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
            "content": """
Solve the following like examples:

Example 1:
Input: a = 2, b = 3
Output:
print(2 + 3)

Example 2:
Input: a = 5, b = 7
Output:
print(5 + 7)

Now solve:
Input: a = 10, b = 4
"""
        }
    ]
)

print(response.choices[0].message.content)