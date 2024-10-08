from typing import Any

from pydantic import BaseModel


class EmailInteractorAuth(BaseModel):
    from_addr: str
    mail_host: str
    mail_port: int
    mail_username: str
    mail_password: str
    secure: Any
