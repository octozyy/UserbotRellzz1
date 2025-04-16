import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "6433540918").split()))

API_ID = int(os.getenv("API_ID", "20897598"))

API_HASH = os.getenv("API_HASH", "93acdbdc4b23c0398bd2042d5ee3865e")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7925263569:AAHM_2Mdfywt8uC2xIC4WW9Sf2PKujE5L80")

OWNER_ID = int(os.getenv("OWNER_ID", "6433540918"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002264332582").split()))

RMBG_API = os.getenv("RMBG_API", "VegrZSZEnnAsufcGsaxECDv6")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://xyraacode:xyraacode@cluster0.8vn5ika.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002272808648"))
