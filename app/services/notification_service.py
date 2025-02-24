import requests

TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_CHAT_ID'

def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': 'TELEGRAM_CHAT_ID',
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()


def send_welcome_email(email: str):
    print(f"Sending welcome email to {email}")


def handle_user_registered_event(event: dict):
    if event['eventType'] == 'UserRegistered':
        send_welcome_email(event['email'])

        username = event.get('username', 'User')
        welcome_message = f"Привет, {username}! Добро пожаловать в наш чат!"
        send_telegram_message(welcome_message)