import json
from ..utils import save_value
from telebot import TeleBot
from telebot.types import Message
import logging

def get_mail_service(message: Message, bot: TeleBot) -> None:
    '''Defines mail service'''
    logger = logging.getLogger(__name__)
    logger.info('Getting mail service name')
    try:
        service_map = {
            'gmail': 'gmail_token',
            'outlook': 'outlook_token',
            'mailru': 'mailru_token'
        }

        if message.text in service_map:
            token_key = service_map[message.text]
            user_input = bot.send_message(message.chat.id, f'Enter you {message.text} service token')
            bot.register_next_step_handler(user_input, get_mail_service_token, bot, token_key, message.text)
        else:
            bot.send_message(message.chat.id, '[ERROR] Invalid service name!')
            logger.error(f'Invalid service name provided: {message.text}')
            bot.register_next_step_handler(message, get_mail_service, bot)

    except Exception as e:
        logger.exception(e)

def get_mail_service_token(message: Message, bot: TeleBot, service_key: str, service_name: str, json_path: str = './src/user.json') -> None:
    '''Saves mail service token to json'''
    logger = logging.getLogger(__name__)
    logger.info('Getting mail service access token')
    
    try:
        if message.content_type == 'text':
            data = {
                'user_chat_id' : message.chat.id,
            }
            data[service_key] = message.text
            save_value(data)
            bot.send_message(message.chat.id, f"Token for {service_name} has been set.")
        else:
            bot.send_message(message.chat.id, '[ERROR] Invalid token. Please send a text message.')
            logger.error('Invalid access token type')
            bot.register_next_step_handler(message, get_mail_service_token, bot, service_key, service_name)
    except Exception as e:
        logger.exception(e)

