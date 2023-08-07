from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/75f5ef6999e79aabcccea.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/2a794cf3556a1f5ef8d93.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/the_nightt_club")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_tcs")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
