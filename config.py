from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","21328397"))
API_HASH = getenv("API_HASH","54bf853c5a9096943dd9515ce874f31f")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = int(getenv("OWNER_ID"," 5920701493 , 5886326864"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/75f5ef6999e79aabcccea.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/2a794cf3556a1f5ef8d93.jpg")

SESSION = getenv("SESSION"," BQFFcg0AvVsUjrIYkboXX5sVUclYcqZR6tLV4eu6U2HKdthu8Gw5nWV2RWOqWAizFCWQk5VrfcSblnjiR5F0IEGMwjhfDtKyWlbIkpwf6x3f0r373mc6b9GwHb4oCzn024Y4uEYKHjmPn2lVBtOfYiqXQxItQoau1e_3klUL1X6NHlpkjqNJ_55tTAl_yNqKHwOzu3TZRSl4sMSpR2FZ-Rv5QkYdlpV6hhBDo2Vx64YFv7jExQSeQVCcUgIzN1XMoM9CMJcb_y0nLQhxH_QTB8IlOHNgbqfZIDmbRg9nF03p3bLs_bddm1CQv7jijA2u-3aTZYc-WjQfzWzRHqQ4TbG9LbekKgAAAAF6WEqJAA ")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/the_nightt_club")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_tcs")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
