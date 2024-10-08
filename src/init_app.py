from dataclasses import dataclass
from typing import Type

from src.reminder_controller.core import DateReminder
from src.services.email_interactor.email_interactor_types import EmailInteractorAuth
from src.settings import settings


@dataclass
class AppDataClassesType:
    controller_class: Type[DateReminder]


@dataclass
class AppDataType:
    controller: DateReminder


AppDataClasses = AppDataClassesType(controller_class=DateReminder,)


__controller = AppDataClasses.controller_class(
    email_auth=EmailInteractorAuth(
        from_addr=settings.EMAIL,
        mail_host=settings.EMAIL_HOST,
        mail_port=settings.EMAIL_PORT,
        mail_username=settings.EMAIL_USERNAME,
        mail_password=settings.EMAIL_PASSWORD,
        secure=True
    ),
    email="gleb.lazarev20@yandex.ru"
)


def get_app_data() -> AppDataType:
    return AppDataType(
        controller=__controller,
    )