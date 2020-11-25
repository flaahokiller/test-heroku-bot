#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
from pyrogram import filters
from pyrogram.types import Message
from botname import botname, pfx, owner

loop = asyncio.get_event_loop()

@botname.on_message(filters.user(owner) & filters.command("reboot", pfx))
async def reboot(_, msg: Message):
    await msg.reply_text("Rebooting...")
    asyncio.get_event_loop().create_task(botname.restart())
