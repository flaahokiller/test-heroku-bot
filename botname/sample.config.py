#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

class Config:
    if "worker.%d" not in os.environ.get('DYNO', "NotTodayMate"):
        API_ID = 0  # int: Your tg api id from (my.telegram.org)
        API_HASH = ""  # str: Your tg api hash from (my.telegram.org)
        PREFIX = ["/", "!", "?"]  # list/str: command prefix of ur choice
        DEBUG = False  # bool: For debugging purposes
        OWNER_ID = 0  # int: Your ID probably.
        SSESSION = "" # str: Session file name.
    else:
        API_ID = os.environ.get('API_ID')
        API_HASH = os.environ.get('API_HASH')
        OWNER_ID = os.environ.get('OWNER_ID')
        PREFIX = os.environ.get('PREFIX')
        DEBUG = os.environ.get('DEBUG')
        SSESSION = os.environ.get('SSESSION')
