import os
# 
from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterDocument
# 
from dotenv import load_dotenv
# ]
from utils.sleep import sleep

load_dotenv()

API_ID : int = int(os.getenv('API_ID'))
API_HASH : str = os.getenv('API_HASH')
DOWNLOAD_FILE_PATH : str = ""

CHANNEL_USERNAME : str = ""

client = TelegramClient("session", API_ID, API_HASH)

for message in client.iter_message(CHANNEL_USERNAME, filter = InputMessagesFilterDocument):
    if message.file.ext == ".pdf":
        message.download_media(file = DOWNLOAD_FILE_PATH)
    sleep()
