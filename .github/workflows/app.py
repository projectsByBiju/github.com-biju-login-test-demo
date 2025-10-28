import os
from dotenv import load_dotenv

load_dotenv()

def login(email, password):
    return email == "admin@example.com" and password == os.getenv("ADMIN_PASS")

def register(email, password):
    return True