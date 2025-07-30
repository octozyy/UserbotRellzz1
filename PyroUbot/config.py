import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "7669174024").split()))

API_ID = int(os.getenv("API_ID", "24499500"))

API_HASH = os.getenv("API_HASH", "17fa8f7a04f45059441fa4a85c189064")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8324427618:AAH9eN-2nG6eK9mjT2JUfz1pgk6ZboeFBxg")

OWNER_ID = int(os.getenv("OWNER_ID", "7606652292"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002547370737").split()))

RMBG_API = os.getenv("RMBG_API", "VegrZSZEnnAsufcGsaxECDv6")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://wtfbruh:KontolXD#123@fsub.brzgete.mongodb.net/?retryWrites=true&w=majority&appName=fsub")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002547370737"))
