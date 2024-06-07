from bot.bot import bot
from log.logger import configure_logging
import logging

def main():
    configure_logging()
    logger = logging.getLogger(__name__)
    logger.info('Initializing bot...')
    try:
        logger.info('Bot is ready...')
        bot.infinity_polling()
    except Exception as e:
        logger.exception(e)

if __name__ == '__main__':
    main()