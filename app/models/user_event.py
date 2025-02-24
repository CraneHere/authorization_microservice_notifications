from pydantic import BaseModel

class UserEvent(BaseModel):
    eventType: str
    email: str

def process_user_event(event):
    username = event.get('username')
    if username:
        return f"Привет, {username}! Добро пожаловать в наш чат!"
    return "Ошибка: не найдено имя пользователя."