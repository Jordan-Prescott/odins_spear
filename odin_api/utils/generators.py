import string 
import secrets
import random

from datetime import datetime

def generate_password(length=8):
    """_summary_

    Parameters:
        length (int, optional): _description_. Defaults to 8.

    Returns:
        _type_: _description_
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_timestamp():
    """_summary_

    Returns:
        _type_: _description_
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_random_code(length=6):
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

