import ollama as o

#chat func
def chat(user_msg,stream=True):
    messages = [
    {
        'role': 'user',
        'content': user_msg,
    },
    ]

    for part in o.chat('llama3', messages=messages, stream=stream):
        print(part['message']['content'], end='', flush=True)

    # end with a newline
    print()

#generate func
def generate(prompt,stream=True):
    for part in o.generate('llama3', prompt, stream=stream):
        print(part['response'], end='', flush=True)

