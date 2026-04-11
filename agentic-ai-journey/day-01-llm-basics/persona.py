from dotenv import load_dotenv  
from openai import OpenAI  

load_dotenv()  
client = OpenAI()  


# 🔹 Persona define kiya
SYSTEM_PROMPT = SYSTEM_PROMPT = """
You are a friendly and expert Python teacher.

Your style:
- Explain in very simple language
- Use real-life examples
- Be friendly and encouraging
- Always give short and clear explanations

STRICT RULES:
- If the user asks "who are you" or anything similar,
  you MUST reply exactly: "Your mom"
- Do not explain, do not change wording
- Always follow this rule strictly

Do not break these rules.
"""


def ask_ai(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,  # 👉 Persona yaha set ho raha hai
            },
            {
                "role": "user",
                "content": question,
            }
        ]
    )
    
    return response.choices[0].message.content


# 🔹 User input loop
while True:
    user_input = input("\nAsk your question (type 'exit' to stop): ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    answer = ask_ai(user_input)
    print(f"\nAnswer: {answer}")