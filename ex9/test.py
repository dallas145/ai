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

question = "Hello!"

while question != "exit":
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                # "content": "Explain the importance of fast language models",
                "content": question,
            }
        ],
        model="llama3-8b-8192",
    )

    with open('chat.md', 'w', encoding='UTF-8') as f:
        f.write("Prompt: \n" + \
                question + "\n\n" + \
                "Response: \n" + \
                chat_completion.choices[0].message.content + \
                "\n\n")

    print("\n" + chat_completion.choices[0].message.content + "\n")
    question = input("Prompt(exit to exit): ")