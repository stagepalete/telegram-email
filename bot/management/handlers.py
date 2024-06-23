from telebot import TeleBot
from telebot.types import Message
from .next_step_handlers import get_mail_service
from ..utils import load_messages
import logging
from mail.services.mail import Gmail
from ..config import GMAIL_APP_PASSWORD

def start(message: Message, bot: TeleBot):
    logger = logging.getLogger(__name__)
    logger.info('Start command was executed')
    try:
        bot.send_message(message.chat.id, load_messages('greeting'))
    except Exception as e:
        logger.exception(e)

def register_service(message: Message, bot: TeleBot):
    logger = logging.getLogger(__name__)
    logger.info('Register command was executed')
    try:
        user_input = bot.send_message(message.chat.id, 'Please enter service name from the list:\n1) gmail\n2)outlook\n3) mailru')
        bot.register_next_step_handler(user_input, get_mail_service, bot)
    except Exception as e:
        logger.exception(e)


def check_inbox(message: Message, bot: TeleBot):
    logger = logging.getLogger(__name__)
    logger.info('Check Inbox command was executed')
    try:
        gmail = Gmail('edige.mazhit.2004@gmail.com', GMAIL_APP_PASSWORD, None)
        gmail.__init__smtp_server__()
        mailbox = gmail.get_messages()
        for msg in mailbox:
            bot.send_message(message.chat.id, msg)
    except Exception as e:
        print(e)