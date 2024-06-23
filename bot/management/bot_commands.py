from telebot import types

start_command = types.BotCommand(command='start', description='Start bot')
register_command = types.BotCommand(command='register', description='Register service')
check_inbox_command = types.BotCommand(command='check inbox', description='Checks last 5 messages from inbox')