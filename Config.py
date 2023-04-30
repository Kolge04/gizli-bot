import os
from time import sleep
from pyrogram import Client
import logging
from dotenv import load_dotenv, set_key, unset_key
from os import getenv
from telethon import TelegramClient

class Config:

   API_ID = int(os.getenv("API_ID", "12210813"))
   API_HASH = os.getenv("API_HASH", "e42eeae11a2f96bcfc5ec3b46a30adad")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "5433537770:AAEs5_y6wFIuBDkjPmRWcjQGZ7FbL3VZ3ZY")
    
    
logging.basicConfig(level=logging.INFO)


api_id = API_ID
api_hash = API_HASH
bot_token = BOT_TOKEN
 
xaos = TelegramClient('Xaos', api_id, api_hash).start(bot_token=bot_token)
