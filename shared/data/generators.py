from __future__ import annotations
from dataclasses import dataclass
from .faker_utils import random_email

@dataclass
class UserData:
    email: str
    password: str

def generate_user(password: str = "Password123!") -> UserData:
    return UserData(email=random_email(), password=password)
