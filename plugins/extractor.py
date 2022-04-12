#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import filters
from pyrogram import Client as trojanz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import Config
from script import Script


@trojanz.on_message(filters.private & (filters.document | filters.video))
async def confirm_dwnld(client, message):
    if message.from_user.id not in Config.AUTH_USERS:
        return await message.reply("🚫 Mohon maaf, bot ini hanya bisa digunakan oleh orang tertentu saja.\n\n<i>Sorry, this bot only can used by authorized user.</i>\n\n<b>Owner</b>: @YasirArisM")

    media = message
    filetype = media.document or media.video

    if filetype.mime_type.startswith("video/"):
        await message.reply_text(
            "**What you want me to do??\n\nApa yang ingin kamu lakukan?**",
            quote=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text="Download and Process", callback_data="download_file")],
                [InlineKeyboardButton(text="Cancel", callback_data="close")]
            ])
        )
    else:
        await message.reply_text(
            "Invalid Media",
            quote=True
        )
