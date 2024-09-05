import os
import urllib.request
import ftplib

from env import Env


def Download() -> None:
    env = Env()
    __download_Kosatec(env.KOSATEC_URL)
    __download_Wortmann(
        env.WORTMANN_FTP_SERVER,
        env.WORTMANN_FTP_SERVER_USER,
        env.WORTMANN_FTP_SERVER_PASSWORD,
    )


def __delete_file(path: str) -> None:
    if os.path.isfile(path):
        os.remove(path)


def __download_Kosatec(url: str):
    file = "kosatec.csv"
    __delete_file(file)
    urllib.request.urlretrieve(url, file)


def __download_Wortmann(Server: str, User: str, Pass: str):
    ftp = ftplib.FTP(Server)
    ftp.login(User, Pass)
    content = "content.csv"
    productcatalog = "productcatalog.csv"
    images = "productimages.zip"
    __delete_file(content)
    __delete_file(productcatalog)
    __delete_file(images)

    ftp.retrbinary("RETR Preisliste/content.csv", open(content, "wb").write)
    ftp.retrbinary(
        "RETR Preisliste/productcatalog.csv", open(productcatalog, "wb").write
    )
    ftp.retrbinary("RETR Produktbilder/productimages.zip", open(images, "wb").write)
    ftp.close()
