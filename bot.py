# Copyright (C) 2021 kenkannih/Pengganti-Bot
#
# Apache License Version 2.0, January 2004 http://www.apache.org/licenses/

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
・✦▭▭▭▭✧◦✦◦✧▭▭▭▭✦ ・
\nHai {} , Bot Ini Sedang Dalam Pemeliharaan.
Anda Tidak Dapat Menggunakan Bot Ini
Sekarang. Kami sarankan bergabung di Channel atau Group support Bot Ini, Agar mendapatkan info Jika Bot Ini Sudah Siap digunakan kembali.\n
・✦▭▭▭▭✧◦✦◦✧▭▭▭▭✦ ・
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
