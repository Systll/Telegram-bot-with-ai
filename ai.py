import json
import requests
import os


history_file = 'history.json'

with open ('data/HF_TOKEN.txt', 'r') as file:
    ai_token = file.read()

API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {ai_token}",
}

def load_history():
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    return [{'role': 'system', 'content': 'Ты - бот для друзей. Помнишь всё общение.'}]

def save_history(history):
    with open(history_file, 'w', encoding='utf-8') as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

chat_history = load_history()

def query(user_name,message):
    global chat_history
    
    formated_message = f'{user_name}: {message}'
    
    chat_history.append({'role': 'user', 'content': formated_message})
    
    payload = {
        'messages': chat_history,
        'model': 'Qwen/Qwen2.5-7B-Instruct:together',
        'max_tokens': 500
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload).json()
        
        answer = response['choices'][0]['message']['content']
        chat_history.append({'role': 'assistant', 'content': answer})
        save_history(chat_history)
        
        return answer.strip()
    except Exception as e:
        return f'Ошибка: {e}'
        

