import time
import requests
from django.conf import settings
from celery import shared_task


@shared_task()
def send_telegram_notification(order_id, product_name, quantity, customer_username, phone_number):
    time.sleep(5)
    token = settings.TELEGRAM_BOT_TOKEN
    method = 'SendMessage'
    message_text = (f"New Order: {order_id}\n Product: {product_name}\n Quantity: {quantity}\n"
                    f"Client: {customer_username}\ntel: {phone_number}")
    response = requests.post(
        url=f'https://api.telegram.org/bot{token}/{method}',
        data={'chat_id': 00000000, 'text': message_text}
    ).json()
