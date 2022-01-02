# Copyright (c) 2021 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("1286763"))
    API_HASH = os.environ.get("676238949450c128a465ec4c0cc9c170")
    BOT_TOKEN = os.environ.get("729621416:AAF2Y7bnqtFUUnZOYaOZ9zUHV52y95HFhFk")
    LOGS_CHANNEL = int(os.environ.get("-1001648589085"))
    MONGODB_URL = os.environ.get("mongodb+srv://Goldstar:qwerty27052003@cluster0.osssn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    BOT_OWNER = int(os.environ.get("669114984"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
