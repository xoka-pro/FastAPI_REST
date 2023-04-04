from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date
    additional_info: Optional[str]

    class Config:
        orm_mode = True


class BirthdayResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    birthday: date
