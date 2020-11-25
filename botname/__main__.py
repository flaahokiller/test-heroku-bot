#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio, importlib
from pyrogram import filters, idle
from pyrogram.types import Message
from botname import botname, pfx, LOG
from botname.funcs import ALL_FUNCS

# Import all funcs in main
for func_name in ALL_FUNCS:
    importlib.import_module("botname.funcs." + func_name)

loop = asyncio.get_event_loop()

BANNER = r"""
BOTNAME

is up & running
"""


@botname.on_message(filters.command("start", pfx))
async def start(_, msg: Message):
    await msg.reply_text("Me up!")


async def main():
    """starts the bot"""
    await botname.start()
    LOG.info("%s", BANNER)
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(main())
