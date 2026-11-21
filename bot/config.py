import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("BOT_TOKEN")

if not token:
    raise ValueError("unable to read bot token")

BOT_TOKEN = token