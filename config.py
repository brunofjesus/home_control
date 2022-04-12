import os
from typing import List, Sized
from dotenv import load_dotenv

load_dotenv()


def allowed_users() -> List[Sized]:
    return os.getenv("ALLOWED_USERS").split(",")


def token() -> str:
    return os.getenv("TOKEN")


def chat_id() -> str:
    return os.getenv("CHAT_ID")
