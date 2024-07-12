import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
BASE_URL = os.getenv("BASE_URL")
KOSATEC_URL = os.getenv("KOSATEC_URL")
WORTMANN_FTP_SERVER = os.getenv("WORTMANN_FTP_SERVER")
WORTMANN_FTP_SERVER_USER = os.getenv("WORTMANN_FTP_SERVER_USER")
WORTMANN_FTP_SERVER_PASSWORD = os.getenv("WORTMANN_FTP_SERVER_PASSWORD")
SALES_CHANNEL_ID = os.getenv("SALES_CHANNEL_ID")
MAIN_CATEGORY_ID = os.getenv("MAIN_CATEGORY_ID")
TAX_ID = os.getenv("TAX_ID")
CURRENCY_ID = os.getenv("CURRENCY_ID")
MEDIA_FOLDER_ID = os.getenv("MEDIA_FOLDER_ID")
LIEFERZEIT_ID = os.getenv("LIEFERZEIT_ID")
MY_NAMESPACE = os.getenv("MY_NAMESPACE")
SSH_HOST = os.getenv("SSH_HOST")
SSH_USER = os.getenv("SSH_USER")
SSH_PASS = os.getenv("SSH_PASS")
FTP_PATH = os.getenv("FTP_PATH")
FTP_SHOP_PATH = os.getenv("FTP_SHOP_PATH")
CDN_PICTURE_PATH = os.getenv("CDN_PICTURE_PATH")

# Check if ENV Vars are present.
if len(CLIENT_ID) < 1:
    raise Exception("CLIENT_ID not configured")
if len(CLIENT_SECRET) < 1:
    raise Exception("CLIENT_SECRET not configured")
if len(BASE_URL) < 1:
    raise Exception("BASE_URL not configured")
if len(KOSATEC_URL) < 1:
    raise Exception("KOSATEC_URL not configured")
if len(WORTMANN_FTP_SERVER) < 1:
    raise Exception("WORTMANN_FTP_SERVER not configured")
if len(WORTMANN_FTP_SERVER_USER) < 1:
    raise Exception("WORTMANN_FTP_SERVER_USER not configured")
if len(WORTMANN_FTP_SERVER_PASSWORD) < 1:
    raise Exception("WORTMANN_FTP_SERVER_PASSWORD not configured")
if len(SALES_CHANNEL_ID) < 1:
    raise Exception("SALES_CHANNEL_ID not configured")
if len(MAIN_CATEGORY_ID) < 1:
    raise Exception("MAIN_CATEGORY_ID not configured")
if len(TAX_ID) < 1:
    raise Exception("TAX_ID not configured")
if len(CURRENCY_ID) < 1:
    raise Exception("CURRENCY_ID not configured")
if len(MEDIA_FOLDER_ID) < 1:
    raise Exception("MEDIA_FOLDER_ID not configured")
if len(LIEFERZEIT_ID) < 1:
    raise Exception("LIEFERZEIT_ID not configured")
if len(MY_NAMESPACE) < 1:
    raise Exception("MY_NAMESPACE not configured")
if len(SSH_HOST) < 1:
    raise Exception("SSH_HOST not configured")
if len(SSH_USER) < 1:
    raise Exception("SSH_USER not configured")
if len(SSH_PASS) < 1:
    raise Exception("SSH_PASS not configured")
if len(FTP_PATH) < 1:
    raise Exception("FTP_PATH not configured")
if len(FTP_SHOP_PATH) < 1:
    raise Exception("FTP_SHOP_PATH not configured")
if len(CDN_PICTURE_PATH) < 1:
    raise Exception("CDN_PICTURE_PATH not configured")


DEFAULT_AUFSCHLAG = 20
DEFAULT_MIN_PREIS = 9.90

WORTMANN_KATEGORIEN_IGNORE: list[str] = [
    "CLOUD_BACKUP",
    "Werbegeschenke",
    "Eingabe Adapter",
    "Optische- und Bandlaufwerke",
    "Netzteile & USVs",
    "AV-Zubehör",
    "Netzwerkzubehör",
    "CLOUD_IAAS",
    "Netzteil / Akku",
    "Systemzubehör",
    "Speicheradapter",
    "Verkaufsförderung",
    "Kartenleser",
    "System- & Stromkabel",
    "Mäuse",
    "Tastaturen",
    "Ersatzteile",
    "LCD Messeware",
    "Ausgabe Zubehör",
    "Bridges & Router",
    "Modems",
    "SERVER",
    "Schulungen",
    "CLOUD_SAAS",
    "Monitore",
    "TERRA CLOUD",
]
