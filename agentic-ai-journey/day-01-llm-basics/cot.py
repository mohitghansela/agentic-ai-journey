#Chain of Tought prompting
from dotenv import load_dotenv  
from openai import OpenAI  

load_dotenv()  
client = OpenAI()  

System_prompt = """
You are a helpful assistant.
Always solve problems step-by-step.
Explain your reasoning clearly before giving the final answer.
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
            "content": "If a = 10 and b = 5, what is (a + b) * 2? Solve step-by-step.",
        }
    ]
)

print(response.choices[0].message.content)