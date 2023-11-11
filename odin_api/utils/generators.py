from datetime import datetime

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")