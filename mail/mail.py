import os
from dotenv import load_dotenv
from services.mail import Gmail

load_dotenv('./envs/.dev.env')


GMAIL_APP_PASSWORD = os.environ['GMAIL_APP_PASSWORD']
print(GMAIL_APP_PASSWORD)

gmail = Gmail('edige.mazhit.2004@gmail.com', GMAIL_APP_PASSWORD, None)
gmail.__init__smtp_server__()
# gmail.send_message('edige.mazhit.2004@gmail.com', 'Test', 'Hello dude')
print(gmail.get_messages())