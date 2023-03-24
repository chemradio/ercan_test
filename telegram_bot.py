import requests

from config import SEND_MESSAGE_TELEGRAM_API_ENDPOINT, TELEGRAM_RECEPIENTS


def send_ad(ad: dict) -> None:
    for chat_id in TELEGRAM_RECEPIENTS:
        params = {
            "chat_id": chat_id,
            "text": f"NEW JOB!!\n\n{ad['link']}",  # \n\n{ad.get('budget')}  \n{ad['title']}
        }
        requests.post(SEND_MESSAGE_TELEGRAM_API_ENDPOINT, params=params)
