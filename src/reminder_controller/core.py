import logging

from src.services.email_interactor.core import EmailInteractor
from src.services.email_interactor.email_interactor_types import EmailInteractorAuth

logger = logging.getLogger(__name__)


class DateReminder:

    def __init__(self, email_auth: EmailInteractorAuth, email: str):
        self.__email_interactor = EmailInteractor(auth_data=email_auth)
        self.__target_email = email

    def daily_reminder(self):
        self.__email_interactor.send_message(
            subject="Ежедневное напоминание",
            message="Здесь будет информация о напоминаемых датах",
            toaddrs=[self.__target_email]
        )
