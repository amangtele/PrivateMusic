import os
import shutil

from pyrogram import filters
from pyrogram.types import Message

from AmangMusic.misc import SUDOERS
from AmangMusic import app




@app.on_message(
    filters.command("clear")
    & SUDOERS
    & ~filters.forwarded
    & ~filters.via_bot
)
  
d = "downloads"
c = "cache"
shutil.rmtree(d)
shutil.rmtree(c)
os.mkdir(c)
os.mkdir(d)
await message.reply_text("yey")
