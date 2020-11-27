#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

import logging, os, sys
from botname.config import Config
from pyrogram import Client

# set logging
if Config.DEBUG is True:
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
if "worker.%d" not in os.environ.get('DYNO', "NotTodayMate"):
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH
    pfx = Config.PREFIX
    owner = Config.OWNER_ID
    ssession = Config.SSESSION

else:
    API_ID = Heroku_Config.API_ID
    API_HASH = Heroku_Config.API_HASH
    pfx = Heroku_Config.PREFIX
    owner = Heroku_Config.OWNER_ID
    ssession = Heroku_Config.SSESSION

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
