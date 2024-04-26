from ollama import chat

def stream_chat(user_msg):
    messages = [
    {
        'role': 'user',
        'content': user_msg,
    },
    ]

    for part in chat('llama3', messages=messages, stream=True):
        print(part['message']['content'], end='', flush=True)

    # end with a newline
    print()


def full_chat(user_msg):
    messages = [{
        'role': 'user',
        'content': user_msg,
    }]

    response = chat('llama3', messages=messages)
    print(response['message']['content'])