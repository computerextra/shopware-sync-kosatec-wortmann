from __config__ import (
    KOSATEC_URL,
    WORTMANN_FTP_SERVER_USER,
    WORTMANN_FTP_SERVER_PASSWORD,
    WORTMANN_FTP_SERVER,
)
import urllib.request
import ftplib
from Helper import delete_file


def download_Kosatec():
    file = "kosatec.csv"
    delete_file(file)
    urllib.request.urlretrieve(KOSATEC_URL, file)


def download_Wortmann():
    ftp = ftplib.FTP(WORTMANN_FTP_SERVER)
    ftp.login(WORTMANN_FTP_SERVER_USER, WORTMANN_FTP_SERVER_PASSWORD)
    content = "content.csv"
    productcatalog = "productcatalog.csv"
    productimages = "productimages.zip"
    delete_file(content)
    delete_file(productcatalog)
    delete_file(productimages)

    ftp.retrbinary("RETR Preisliste/content.csv", open(content, "wb").write)
    ftp.retrbinary(
        "RETR Preisliste/productcatalog.csv", open(productcatalog, "wb").write
    )
    ftp.retrbinary(
        "RETR Produktbilder/productimages.zip", open(productimages, "wb").write
    )
    ftp.close()
