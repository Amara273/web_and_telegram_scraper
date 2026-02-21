import os
# 
from dotenv import load_dotenv
# 
from telethon import functions, types
from telethon.sync import TelegramClient
# 
from utils.handle_channel_discovery import handleChannel

load_dotenv()

API_ID : int = int(os.getenv("API_ID"))
API_HASH : str = os.getenv("API_HASH")

username : str = ""
channels_discovered : list[list] = []

with TelegramClient("session", API_ID, API_HASH) as client:
    result : TelegramClient.Chatslice = client(functions.channels.GetChannelRecommendationsRequest(
        channel = username
    ))

    for channel in result:
        channel_info : list = handleChannel(channel)
        channels_discovered.append(channel_info)