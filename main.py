import requests

from config import TOKEN


BASE_URL = F'https://api.telegram.org/bot{TOKEN}'


def get_me() -> dict:
    get_me_url = f'{BASE_URL}/getMe'
    
    response = requests.get(get_me_url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Telegram server xatolik qaytardi!')


def get_updates() -> list[dict]:
    get_updates_url = f'{BASE_URL}/getUpdates'
    
    response = requests.get(get_updates_url)

    if response.status_code == 200:
        return response.json()['result']
    else:
        raise Exception('Telegram server xatolik qaytardi!')
    

def send_message() -> None:
    send_message_url = f'{BASE_URL}/sendMessage'
    
    params = {
        'chat_id': 1258594598,
        'text': 'Hello World'
    }
    requests.get(send_message_url, params=params)


send_message()
