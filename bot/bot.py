import logging
from .config import TELEGRAM_BOT_TOKEN as token # Get telegram bot token
from .utils import register_handlers
from .management.handlers import register_service, start, check_inbox
from .management.bot_commands import start_command, register_command, check_inbox_command
from telebot import TeleBot, types

logger = logging.getLogger(__name__)

try:
    bot = TeleBot(token)
    register_handlers(bot, True, [['register'], ['start'], ['check']], ['text', 'text', 'text'], register_service, start, check_inbox)
    bot.set_my_commands([start_command, register_command, check_inbox_command])
except Exception as e:
    logger.exception(e)

