import requests


def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=payload)


token = "7571124904:AAEyoDMJOpDeHw4RurQUfzFM480J66KQGWss"
chat_id = -1002371814477
message = "Ola Mundo!!!"

send_telegram_message(token, chat_id, message)
