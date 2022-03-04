import os
from os import getenv
from dotenv import load_dotenv

START_IMAGE = "https://camo.githubusercontent.com/05e1f71fec76a5067c2becc6dfcd9cb593e6b9c023ead6f17e69cc709be40368/68747470733a2f2f74656c656772612e70682f66696c652f3631613565333134383561373765373732363734302e6a7067"
admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
SESSION_NAME = getenv("SESSION_NAME", "session")

# mandatory vars
BOT_NAME = getenv("BOT_NAME")
OWNER_USERNAME = getenv("OWNER_USERNAME")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/santhosh-podili/santhoshpodili")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "santhuvc")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "santhubotupadates")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/ce7dec913a00dc2d76bb9.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/ad1f8bcc4d044d3f25fb3.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/7569d601b34af1bb14570.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/35700a88d56fd6064822a.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/63300139d232dc12452ab.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/19814cb8155e0a06a1da9.jpg")
START_IMG_URL = getenv("START_IMG_URL", START_IMAGE)
