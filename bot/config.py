import os
from dotenv import load_dotenv

load_dotenv('./envs/.dev.env')


TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
GMAIL_APP_PASSWORD = os.environ['GMAIL_APP_PASSWORD']