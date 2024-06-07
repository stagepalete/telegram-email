from typing import Callable, List
from telebot import types, TeleBot
import logging
import os
import json

def register_handlers(bot: TeleBot, pass_bot: bool, commands: list[list[str]], content_types: list[str], *handlers: Callable) -> None:
    '''Registers all handlers to bot'''
    logger = logging.getLogger(__name__)
    try:
        for handler, command, content_type in zip(handlers, commands, content_types):
            bot.register_message_handler(handler, commands=command, pass_bot=pass_bot, content_types=content_type)
        logger.info('handlers registered')

    except Exception as e:
        logger.exception(e)
        
def save_value(data: dict, json_path: str = './src/user.json') -> None:
    logger = logging.getLogger(__name__)
    try:
        if os.path.exists(json_path) and os.path.getsize(json_path) > 0:
            with open(json_path, 'r', encoding='utf-8') as f:
                file_data = json.load(f)
        else:
            file_data = []
        
        for entry in file_data:
            if entry.get('user_chat_id') == data['user_chat_id']:
                entry.update(data)
                logger.info('User data updated')
                break
        else:
            file_data.append(data)
            logger.info('User data saved')
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(file_data, f, ensure_ascii=False, indent=4)
        
    
    except json.JSONDecodeError as e:
        logger.exception(e)
    except Exception as e:
        logger.exception(e)


def load_messages(key: str, json_path='./src/messages.json') -> str:
    '''Returns message from all mesasges list'''
    logger = logging.getLogger(__name__)
    try:
        if os.path.exists(json_path) and os.path.getsize(json_path) > 0:
            with open(json_path, 'r', encoding='utf-8') as f:
                file_data = json.load(f)
        else:
            file_data = []
        
        for entry in file_data:
            logger.info(f'Find {key} in messages')
            return entry.get(key)
        else:
            logger.warn(f'You did not give value for {key} in messages')
            return None
    except json.JSONDecodeError as e:
        logger.exception(e)
    except Exception as e:
        logger.exception(e)

def search_chat_id():
    ...