import smtplib
from imap_tools import MailBox
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class Mail:
    def __init__(self, email_address: str, email_password: str, ) -> None:
        self.email_address = email_address
        self.email_password = email_password
    
    def start_polling(self) -> None:
        print('Working')

    def send_message(self, to: str, subject: str, message:str):
        ...

class Gmail(Mail):
    def __init__(self, email_address: str, email_password: str, email_token: str) -> None:
        super().__init__(email_address, email_password)
        self.gmail_token = email_token
        self.smpt_server = smtplib.SMTP('smtp.gmail.com', 587)
        # self.imap_server = imaplib.IMAP4('imap.gmail.com', 993)
        self.imap_server = MailBox('imap.gmail.com', 993)

    def __init__smtp_server__(self):
        self.smpt_server.starttls()

    def send_message(self, to: str, subject: str, message: str):
        try:
            self.smpt_server.login(self.email_address, self.email_password)
            msg = MIMEText(message)
            msg['Subject'] = subject
            self.smpt_server.sendmail(self.email_address, to, msg.as_string())
        except Exception as e:
            print(e)

    def get_messages(self) -> list[str]:
        try:
            mailbox = []
            with self.imap_server.login(self.email_address, self.email_password, 'Inbox') as mb:
                for msg in mb.fetch(limit=5, reverse=True, mark_seen=False):
                    message = f'{msg.subject} {msg.date} {msg.flags} {msg.text}'
                    if len(message) > 4096:
                        for x in range(0, len(message), 4095):
                            mailbox.append(message[x:x+4095])
                            break
            return mailbox
        except Exception as e:
            print(e)

class MailRu(Mail):
    def __init__(self, email_address: str, email_password: str, email_token: str) -> None:
        super().__init__(email_address, email_password)
        self.gmail_token = email_token


class Outlook(Mail):
    def __init__(self, email_address: str, email_password: str, email_token: str) -> None:
        super().__init__(email_address, email_password)
        self.gmail_token = email_token
