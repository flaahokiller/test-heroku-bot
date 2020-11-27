#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

import logging, os, sys
from pyrogram import Client

# Heroku Checker
if not os.environ.get('DYNO'):
    from botname.config import Config
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH
    pfx = Config.PREFIX
    owner = Config.OWNER_ID
    ssession = Config.SSESSION
    DEBUG = Config.DEBUG

else:
    API_ID = int(os.environ.get('API_ID'))
    API_HASH = str(os.environ.get('API_HASH'))
    pfx = list(os.environ.get('PREFIX'))
    owner = int(os.environ.get('OWNER_ID'))
    ssession = str(os.environ.get('SSESSION'))
    DEBUG = bool(os.environ.get('DEBUG'))

# set logging
if DEBUG is True:
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
    )

else:
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

LOG = logging.getLogger(__name__)

# Check python version
if sys.version_info[0] < 3 or sys.version_info[1] < 7:
    LOG.info("You must have python version 3.7 or more! shutting down...")
    sys.exit(1)


class BotName(Client):
    """
    Custom BotName client class derived from
    pyrogram.Client class.
    """

    def __init__(self, name):
        self.name = name.lower()
        super().__init__(
            session_name=ssession,
            api_id=API_ID,
            api_hash=API_HASH,
        )

    async def start(self):
        """Starts the client."""

        await super().start()

    async def stop(self, *args):
        """Stops the client"""

        await super().stop()

    async def restart(self):
        """Restarts the bot."""

        await self.stop()
        os.execl(
            sys.executable,
            sys.executable,
            "-m",
            self.__class__.__name__.lower(),
        )
        sys.exit()


# Create instance of botname.
botname = BotName("botname")
