# Copyright (C) 2021 kenkannih/Pengganti-Bot
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Pengganti-Bot
import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Client(
    "Maintenance-Bot",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)

updatesc = os.environ["UPDATES_CHANNEL"]
supportc = os.environ["SUPPORT_CHAT"]

BOT_TEXT = """
┏━━━━━━༻❁༺━━━━━━┓\n 
  Hai {} , Bot Ini Sedang\n
  Dalam Pemeliharaan.\n
  Anda tidak dapat Menggunakan\n 
  Bot Ini Sekarang. Kami sarankan\n
  Bergabung di Channel atau\n
  Group support Bot Ini,  Agar\n 
  Mendapatkan info Jika\n
  Bot siap digunakan kembali.\n
┗━━━━━━༻❁༺━━━━━━┛
"""

BOT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 📣", url=f"https://telegram.me/{updatesc}"),
            InlineKeyboardButton(text="👥 ɢʀᴏᴜᴘ", url=f"https://telegram.me/{supportc}"),
        ]
    ]
)


@bot.on_message(filters.private & filters.text)
async def start(bot, update):
    text = BOT_TEXT.format(update.from_user.mention)
    reply_markup = BOT_BUTTONS
    await update.reply_text(
        text=text, disable_web_page_preview=True, reply_markup=reply_markup
    )

logging.info("Bot is online.")
bot.run()
