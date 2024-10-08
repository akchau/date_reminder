import datetime
import logging
from email.message import EmailMessage
import pytz
import smtplib

from src.services.email_interactor.email_interactor_types import EmailInteractorAuth


logger = logging.getLogger(__file__)


class EmailInteractor:
    def __init__(self, auth_data: EmailInteractorAuth):
        self.from_addr = auth_data.from_addr
        self.mail_host = auth_data.mail_host
        self.mail_port = auth_data.mail_port
        self.username = auth_data.mail_username
        self.password = auth_data.mail_password
        self.secure = auth_data.secure
        self.timeout = 10.0

    def send_message(self, subject: str, message: str, toaddrs: list[str]):
        """
        Подключается к SMTP серверу почты и отправляет сообщение адресатам.

        :param toaddrs:
        :param message:
        :param subject:
        :param filepath:
        """
        smtp = smtplib.SMTP_SSL(self.mail_host, self.mail_port, timeout=self.timeout)
        msg = EmailMessage()
        msg['From'] = self.from_addr
        msg['To'] = ','.join(toaddrs)
        msg['Subject'] = subject
        msg['Date'] = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        msg.set_content(message)
        if self.username:
            smtp.login(self.username, self.password)
        smtp.send_message(msg)
        smtp.quit()

