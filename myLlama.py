from ollama import chat as llama_chat

def chat(user_msg,stream=True):
    messages = [
    {
        'role': 'user',
        'content': user_msg,
    },
    ]

    for part in llama_chat('llama3', messages=messages, stream=stream):
        print(part['message']['content'], end='', flush=True)

    # end with a newline
    print()
