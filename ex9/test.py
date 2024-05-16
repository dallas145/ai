import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

try:
    print('Try to remove old output...')
    os.remove('./chat.md')
    print('Old output file removed.')
except OSError:
    print('file: chat.md not found, create one.')

models = ['llama3-70b-8192', 'llama3-8b-8192', 'mixtral-8x7b-32768']

print("----- Choose model -----")
print("[1] llama3-70b-8192")
print("[2] llama3-8b-8192 (default)")
print("[3] mixtral-8x7b-32768")
choice = input("Pick a model(default:2): ")
if choice == '':
    choice = 2
elif choice not in ["1","2","3"]:
    print("Invalid value, use default.")
    choice = 2

question = "Hello!"
model_type = models[int( choice ) - 1]
while question != "exit":
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                # "content": "Explain the importance of fast language models",
                "content": question,
            }
        ],
        model=model_type,
    )

    with open('chat.md', 'a', encoding='UTF-8') as f:
        f.write("## Prompt: \n" + \
                question + "\n\n" + \
                "## Response: \n" + \
                chat_completion.choices[0].message.content + \
                "\n\n")

    print("\n" + chat_completion.choices[0].message.content + "\n")
    question = input("Prompt(exit to exit): ")
