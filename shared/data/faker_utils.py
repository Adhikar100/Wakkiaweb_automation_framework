from __future__ import annotations
import random
import string

def random_email(domain: str = "example.com") -> str:
    user = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{user}@{domain}"

def random_phone(prefix: str = "98") -> str:
    rest = "".join(random.choices(string.digits, k=8))
    return f"{prefix}{rest}"
