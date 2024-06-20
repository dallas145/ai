import os
from groq import Groq

def main_loop(choice, language, logfile, log=False):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    content = input("Content(exit to exit): ")

    if(language == "english"):
        question = f"Please translate \"{content}\" to English."
    
    if(language == "chinese"):
        question = f"請將以下句子翻譯成中文 \"{content}\""

    models = ['llama3-70b-8192', 'llama3-8b-8192', 'mixtral-8x7b-32768', 'gemma-7b-it']
    model_type = models[int( choice ) - 1]
    while content != "!exit":
        if(language == "english"):
            question = f"Please translate \'{content}\' to English."
        
        if(language == "chinese"):
            question = f"請將以下句子翻譯成中文 \'{content}\'"
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a translator, you will answer me in the following format: Source languge is: [source language] then one blank line then [answer] without any greetings."
                },
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model=model_type,
        )

        if log:
            if not os.path.exists("./logs"):
                os.mkdir("./logs")
            with open(f'./logs/{logfile}.md', 'a', encoding='UTF-8') as f:
                f.write("## User input: \n" + \
                        question + "\n\n" + \
                        f"## {model_type} Output: \n" + \
                        chat_completion.choices[0].message.content + \
                        "\n\n")

        print("\n" + chat_completion.choices[0].message.content + "\n")
        content = input("Content(!exit to exit): ")

def main_noloop(choice, content, language):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )
    
    if(language == "english"):
        question = f"Please translate \"{content}\" to English."
    
    if(language == "chinese"):
        question = f"請將以下句子翻譯成中文 \"{content}\""

    models = ['llama3-70b-8192', 'llama3-8b-8192', 'mixtral-8x7b-32768', 'gemma-7b-it']
    model_type = models[int( choice ) - 1]
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a translator, you will answer me in the following format: Source languge is: [source language] then one blank line then [answer] without any greetings."
            },
            {
                "role": "user",
                "content": question,
            }
        ],
        model=model_type,
    )

    print("\n" + chat_completion.choices[0].message.content + "\n")

if __name__ == "__main__":
    main_loop(1, "chinese")