import os
from dotenv import load_dotenv


class WortmannLogin:
    def __init__(self, Server: str, User: str, Pass: str):
        self.Server: str = Server
        self.User: str = User
        self.Pass: str = Pass

    def Getserver(self) -> str:
        return self.Server

    def GetUser(self) -> str:
        return self.User

    def GetPass(self) -> str:
        return self.Pass


class Env:
    def __init__(self):
        self.CLIENT_ID: str
        self.CLIENT_SECRET: str
        self.BASE_URL: str
        self.KOSATEC_URL: str
        self.WORTMANN_FTP_SERVER: str
        self.WORTMANN_FTP_SERVER_USER: str
        self.WORTMANN_FTP_SERVER_PASSWORD: str
        self.SALES_CHANNEL_ID: str
        self.MAIN_CATEGORY_ID: str
        self.TAX_ID: str
        self.CURRENCY_ID: str
        self.MEDIA_FOLDER_ID: str
        self.LIEFERZEIT_ID: str
        self.MY_NAMESPACE: str
        self.SSH_HOST: str
        self.SSH_USER: str
        self.SSH_PASS: str
        self.SSH_PATH: str
        self.FTP_PATH: str
        self.FTP_SHOP_PATH: str
        self.CDN_PICTURE_PATH: str

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

        if not CLIENT_ID or len(CLIENT_ID) < 1:
            raise Exception("CLIENT_ID not configured")
        if not CLIENT_SECRET or len(CLIENT_SECRET) < 1:
            raise Exception("CLIENT_SECRET not configured")
        if not BASE_URL or len(BASE_URL) < 1:
            raise Exception("BASE_URL not configured")
        if not KOSATEC_URL or len(KOSATEC_URL) < 1:
            raise Exception("KOSATEC_URL not configured")
        if not WORTMANN_FTP_SERVER or len(WORTMANN_FTP_SERVER) < 1:
            raise Exception("WORTMANN_FTP_SERVER not configured")
        if not WORTMANN_FTP_SERVER_USER or len(WORTMANN_FTP_SERVER_USER) < 1:
            raise Exception("WORTMANN_FTP_SERVER_USER not configured")
        if not WORTMANN_FTP_SERVER_PASSWORD or len(WORTMANN_FTP_SERVER_PASSWORD) < 1:
            raise Exception("WORTMANN_FTP_SERVER_PASSWORD not configured")
        if not SALES_CHANNEL_ID or len(SALES_CHANNEL_ID) < 1:
            raise Exception("SALES_CHANNEL_ID not configured")
        if not MAIN_CATEGORY_ID or len(MAIN_CATEGORY_ID) < 1:
            raise Exception("MAIN_CATEGORY_ID not configured")
        if not TAX_ID or len(TAX_ID) < 1:
            raise Exception("TAX_ID not configured")
        if not CURRENCY_ID or len(CURRENCY_ID) < 1:
            raise Exception("CURRENCY_ID not configured")
        if not MEDIA_FOLDER_ID or len(MEDIA_FOLDER_ID) < 1:
            raise Exception("MEDIA_FOLDER_ID not configured")
        if not LIEFERZEIT_ID or len(LIEFERZEIT_ID) < 1:
            raise Exception("LIEFERZEIT_ID not configured")
        if not MY_NAMESPACE or len(MY_NAMESPACE) < 1:
            raise Exception("MY_NAMESPACE not configured")
        if not SSH_HOST or len(SSH_HOST) < 1:
            raise Exception("SSH_HOST not configured")
        if not SSH_USER or len(SSH_USER) < 1:
            raise Exception("SSH_USER not configured")
        if not SSH_PASS or len(SSH_PASS) < 1:
            raise Exception("SSH_PASS not configured")
        if not FTP_PATH or len(FTP_PATH) < 1:
            raise Exception("FTP_PATH not configured")
        if not FTP_SHOP_PATH or len(FTP_SHOP_PATH) < 1:
            raise Exception("FTP_SHOP_PATH not configured")
        if not CDN_PICTURE_PATH or len(CDN_PICTURE_PATH) < 1:
            raise Exception("CDN_PICTURE_PATH not configured")

        self.CLIENT_ID = CLIENT_ID
        self.CLIENT_SECRET = CLIENT_SECRET
        self.BASE_URL = BASE_URL
        self.KOSATEC_URL = KOSATEC_URL
        self.WORTMANN_FTP_SERVER = WORTMANN_FTP_SERVER
        self.WORTMANN_FTP_SERVER_USER = WORTMANN_FTP_SERVER_USER
        self.WORTMANN_FTP_SERVER_PASSWORD = WORTMANN_FTP_SERVER_PASSWORD
        self.SALES_CHANNEL_ID = SALES_CHANNEL_ID
        self.MAIN_CATEGORY_ID = MAIN_CATEGORY_ID
        self.TAX_ID = TAX_ID
        self.CURRENCY_ID = CURRENCY_ID
        self.MEDIA_FOLDER_ID = MEDIA_FOLDER_ID
        self.LIEFERZEIT_ID = LIEFERZEIT_ID
        self.MY_NAMESPACE = MY_NAMESPACE
        self.SSH_HOST = SSH_HOST
        self.SSH_USER = SSH_USER
        self.SSH_PASS = SSH_PASS
        self.FTP_PATH = FTP_PATH
        self.FTP_SHOP_PATH = FTP_SHOP_PATH
        self.CDN_PICTURE_PATH = CDN_PICTURE_PATH
