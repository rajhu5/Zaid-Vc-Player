## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME" ,"BQCPOD2gQoFVcRJ0Q3QNS36-zzu1nLMwKBqXvu2-iAE5mMLypfcBccWCQr8FIhxKcRqydw5t0M0rkzm88k3xPWZeuRcb8X-kYJPvESRBQocg4rr_PouyCYO_MyYi4tC8BKlvcpnLyRnsi-Wc0t4cbwBBud39rZFPfEsXXDabRdt034QC8IMU9I8IhS3BM_0OXdsp-xUDJaRRuQfEcscURZMXG-z_Y0an7HzvCMiqrjBROmqJfJXu8RZc4mfyLVvogTrbvi1B3hgQTPxm48O_T3Jgq0NUblD368jOBgQQT3m6fPBu7GN7iVNAvZ0N777isCdYwYteZt-52FeedyZPyOMAAAAAAYRq1wgA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "6566716594:AAFOawRrge9OY_CO-Hf48CM4BNTXofDtOc8")
BOT_NAME = getenv("BOT_NAME", "Jedh")

API_ID = int(getenv("API_ID", "28645948"))
API_HASH = getenv("API_HASH", "0d1cca3a9f4f4beb7ae8508f05ec4fcd")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://ainul99050:575751ai@cluster0.ozzd6ua.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "𝐏𝐫𝐢𝐧𝐜𝐞 𝐜𝐡𝐚𝐫𝐦𝐢𝐧𝐠👑")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Drama_boy2")
ALIVE_NAME = getenv("ALIVE_NAME", "Zaid")
BOT_USERNAME = getenv("BOT_USERNAME", "Music_princy_x_bot")
OWNER_ID = getenv("OWNER_ID", "6425682035")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝐏𝐫𝐢𝐧𝐜𝐞 𝐜𝐡𝐚𝐫𝐦𝐢𝐧𝐠👑")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME" ,None)
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
