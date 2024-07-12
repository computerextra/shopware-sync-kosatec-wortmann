from Files.Download import download_Kosatec, download_Wortmann
import time
from Files.Bilder import upload_wortmann_images, delete_images_from_ftp
from Files.CSV import parse_csv_files
from __config__ import MEDIA_FOLDER_ID
from Api.Hersteller import sync_manufacturer
from Api.Client import get_api_client
from lib_shopware6_api_base import Criteria
from Api.Kategorien import sync_categories
from Api.Endpoints import SYNC
from Api.Artikel import (
    update_products,
    delete_products,
    create_products,
    get_shop_products,
)
from typing import Any
import sys


def delete_all_media() -> None:
    print("Ziehe alle Medien")
    client = get_api_client()
    try:
        filter = Criteria()
        filter.filter.append(
            {"field": "mediaFolderId", "type": "equals", "value": MEDIA_FOLDER_ID}
        )
        data = client.request_post_paginated(
            "search/media",
            payload={
                "filter": [
                    {
                        "field": "mediaFolderId",
                        "type": "equals",
                        "value": MEDIA_FOLDER_ID,
                    }
                ]
            },
        )["data"]
        print(len(data))

        if data:
            count = 0
            payload: list[Any] = []
            for x in data:
                if count >= 750:
                    print(
                        f"Es werden {count} Bilder von insgesamt {len(data)} gelöscht."
                    )
                    try:
                        _ = client.request_post(
                            SYNC,
                            {
                                "Bulk-delete": {
                                    "entity": "media",
                                    "action": "delete",
                                    "payload": payload,
                                }
                            },
                        )
                        payload = []
                        count = 0
                    except Exception as e:
                        print(f"Fehler beim löschen: {e}")
                payload.append({"id": x["id"]})
                count += 1

            if count > 0:
                print(f"Es werden {count} Bilder von insgesamt {len(data)} gelöscht.")
                try:
                    _ = client.request_post(
                        SYNC,
                        {
                            "Bulk-delete": {
                                "entity": "media",
                                "action": "delete",
                                "payload": payload,
                            }
                        },
                    )
                except Exception as e:
                    print(f"Fehler beim löschen: {e}")
    except Exception as e:
        print(f"Fehler: {e}")
        exit(1)


def create_categories() -> None:
    print("Verarbeite Artikel Listen")
    artikel = parse_csv_files()
    print("Lege neue Kategorien an")
    sync_categories(artikel)


def main_without_download() -> None:
    print("Verarbeite Artikel Listen")
    artikel = parse_csv_files()
    print("Lege neue Hersteller an")
    sync_manufacturer(artikel.Hersteller)
    print("Lege neue Kategorien an")
    sync_categories(artikel)
    shop_artikel: Any = get_shop_products()
    print("Artikel Aktualisieren")
    updated: int = update_products(items=artikel, Alle_Artikel=shop_artikel)
    print("Neue Artikel Anlegen")
    new: int = create_products(items=artikel, Alle_Artikel=shop_artikel)
    print("Alte Artikel Löschen")
    deleted: int = delete_products(items=artikel, Alle_Artikel=shop_artikel)
    print(f"Neue Artikel: {new}")
    print(f"Aktualisierte Artikel: {updated}")
    print(f"Gelöschte Artikel: {deleted}")


def main():
    print("Download Kosatec Datei")
    download_Kosatec()
    print("Download Wortmann Dateien")
    download_Wortmann()
    print("Unzip und Upload Wortmann Bilder")
    upload_wortmann_images()
    print("Verarbeite Artikel Listen")
    artikel = parse_csv_files()
    print("Lege neue Hersteller an")
    sync_manufacturer(artikel.Hersteller)
    print("Lege neue Kategorien an")
    sync_categories(artikel)
    shop_artikel: Any = get_shop_products()
    print("Artikel Aktualisieren")
    updated: int = update_products(items=artikel, Alle_Artikel=shop_artikel)
    print("Neue Artikel Anlegen")
    new: int = create_products(items=artikel, Alle_Artikel=shop_artikel)
    print("Alte Artikel Löschen")
    deleted: int = delete_products(items=artikel, Alle_Artikel=shop_artikel)
    print(f"Neue Artikel: {new}")
    print(f"Aktualisierte Artikel: {updated}")
    print(f"Gelöschte Artikel: {deleted}")
    print("Bilder vom FTP Server löschen")
    delete_images_from_ftp()


if __name__ == "__main__":
    start = time.time()
    print("Ziehe Argumente.")
    print("Argument list", sys.argv)
    if len(sys.argv) > 1:
        if sys.argv[1] == "cat":
            create_categories()
        if sys.argv[1] == "del":
            delete_all_media()
        if sys.argv[1] == "main":
            main()
        if sys.argv[1] == "no-download":
            main_without_download()
    else:
        main()

    end = time.time()
    print(f"Runtime: {round((end - start), 2)}s")
    print(f"Runtime: {round(((end - start)/60), 2)}min")
    print(f"Runtime: {round(((end - start)/60/60), 2)}h")
