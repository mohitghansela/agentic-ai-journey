from dotenv import load_dotenv  
from openai import OpenAI  

# 🔹 Step 1: Load API key
load_dotenv()  

# 🔹 Step 2: Create client
client = OpenAI()  


# 🔹 Step 3: System Prompt (now supports 2 modes)
SYSTEM_PROMPT = """
You are an intelligent problem-solving assistant.

Guidelines:
- Understand the problem deeply
- If user asks for steps, explain step-by-step
- Otherwise, solve internally and give only final answer
- Keep answers clear and correct

Focus on accuracy and clarity.
"""


# 🔹 Step 4: Function
def ask_ai(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": question,
            }
        ]
    )
    return response.choices[0].message.content


# 🔹 Step 5: Interactive loop (REAL automation)
while True:
    
    # 👉 User se input lo
    user_input = input("\nAsk your question (type 'exit' to stop): ")

    # 👉 Exit condition
    if user_input.lower() == "exit":
        print("Goodbye")
        break

    # 👉 Optional: user choose kare thinking dekhni hai ya nahi
    show_steps = input("Do you want step-by-step reasoning? (yes/no): ")

    # 👉 Agar user "yes" bole → prompt modify karo
    if show_steps.lower() == "yes":
        user_input += " Solve step-by-step."

    # 👉 AI call
    answer = ask_ai(user_input)

    # 👉 Output
    print(f"\nAnswer: {answer}")