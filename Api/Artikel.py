from Files.CSV import CSV_Package, ImportArtikel
from Api.Client import get_api_client
from Api.Endpoints import SEARCH_PRODUCT, SYNC, PRODUCT
from Helper import Uuid, find_category, calculate_price
from Api.Tax import get_tax
from Api.Types import Shopware6NewProduct, Shopware6ProduktPreis
from Config.pickle_my_configs import get_config
from __config__ import (
    LIEFERZEIT_ID,
    CURRENCY_ID,
    TAX_ID,
    SALES_CHANNEL_ID,
    MEDIA_FOLDER_ID,
)
import time
import os
from typing import Any

MAX_UPLOAD = 500

tax = get_tax()


def update_products(items: CSV_Package, Alle_Artikel: Any) -> int:
    Artikel = __sort_products(items.Artikel, "update", Alle_Artikel)
    print(f"Es werden insgesamt {len(Artikel)} Artikel synchronisiert")
    count = 0
    payload = []

    config = get_config()
    for item in Artikel:
        if not item.Artikelnummer:
            continue
        if count >= MAX_UPLOAD:
            print(
                f"Es werden {count} von insgesamt {len(Artikel)} Artikeln aktualisiert."
            )
            __send_payload(payload)
            payload: list[Any] = []
            count = 0
        count += 1
        Kategorie = find_category(item)
        vkBrutto = 0
        if item.ek and len(item.ek) > 0:
            vkBrutto = calculate_price(item.ek, Kategorie, item.Artikelnummer)
        if item.vk and len(item.vk) > 0:
            vkBrutto = float(item.vk.replace(",", "."))
        vkNetto = vkBrutto / tax
        if config.Uvp and len(config.Uvp) > 0:
            for x in config.Uvp:
                if item.Artikelnummer == x.Artikelnummer:
                    vkBrutto = x.Brutto
                    vkNetto = x.Netto
        Bestand = int(item.Bestand) if item.Bestand else 0
        Aktiv = True if Bestand > 0 else False
        payload.append(
            {
                "id": Uuid(item.Artikelnummer),
                "deliveryTimeId": LIEFERZEIT_ID,
                "price": [
                    {
                        "currencyId": CURRENCY_ID,
                        "net": vkNetto,
                        "gross": vkBrutto,
                        "linked": True,
                        "listPrice": None,
                        "percentage": None,
                        "regulationPrice": None,
                        "extensions": [{}],
                        "apiAlias": "price",
                    }
                ],
                "stock": Bestand,
                "active": Aktiv,
            }
        )
    if len(payload) > 0:
        print(f"Es werden {count} von insgesamt {len(Artikel)} Artikeln aktualisiert.")
        __send_payload(payload)
    return len(Artikel)


def create_products(items: CSV_Package, Alle_Artikel: Any) -> int:
    client = get_api_client()
    Artikel = __sort_products(items.Artikel, "new", Alle_Artikel)
    count = 1
    for item in Artikel:
        print(f"Artikel {count} von {len(Artikel)} wird angelegt.")
        count += 1
        if not item.Artikelnummer:
            continue
        if not item.Name:
            continue
        NeuerArtikel = Shopware6NewProduct()
        NeuerArtikel.name = item.Name.strip()
        NeuerArtikel.id = Uuid(item.Artikelnummer)
        NeuerArtikel.taxId = TAX_ID
        NeuerArtikel.categories = [{"id": Uuid(find_category(item))}]
        vkBrutto: float = 0
        if item.ek and len(item.ek) > 0:
            vkBrutto = calculate_price(item.ek, find_category(item), item.Artikelnummer)
        if item.vk and len(item.vk) > 0:
            vkBrutto = float(item.vk.replace(",", "."))
        NeuerArtikel.price = []

        price = Shopware6ProduktPreis()
        price.currencyId = CURRENCY_ID
        price.net = vkBrutto / tax
        price.gross = float(vkBrutto)
        price.linked = True
        price.listPrice = None
        price.percentage = None
        price.regulationPrice = None
        price.extensions = [{}]
        price.apiAlias = "price"

        NeuerArtikel.visibilities = []
        NeuerArtikel.visibilities.append(
            {
                "salesChannelId": SALES_CHANNEL_ID,
                "visibility": 30,
            }
        )
        NeuerArtikel.productNumber = item.Artikelnummer
        NeuerArtikel.stock = int(item.Bestand) if item.Bestand else 0
        NeuerArtikel.active = True if NeuerArtikel.stock > 0 else False
        NeuerArtikel.manufacturerNumber = item.HerstellerNummer
        NeuerArtikel.shippingFree = False
        NeuerArtikel.description = item.Beschreibung
        if item.Hersteller:
            NeuerArtikel.manufacturer = {"id": Uuid(item.Hersteller)}
        else:
            continue
        product_payload = {
            "id": NeuerArtikel.id,
            "taxId": NeuerArtikel.taxId,
            "price": [
                {
                    "currencyId": price.currencyId,
                    "net": price.net,
                    "gross": price.gross,
                    "linked": price.linked,
                    "listPrice": price.listPrice,
                    "percentage": price.percentage,
                    "regulationPrice": price.regulationPrice,
                    "extensions": price.extensions,
                    "apiAlias": price.apiAlias,
                }
            ],
            "productNumber": NeuerArtikel.productNumber,
            "stock": NeuerArtikel.stock,
            "name": NeuerArtikel.name,
            "categories": NeuerArtikel.categories,
            "manufacturer": NeuerArtikel.manufacturer,
            "manufacturerNumber": NeuerArtikel.manufacturerNumber,
            "visibilities": NeuerArtikel.visibilities,
            "description": NeuerArtikel.description,
            "active": NeuerArtikel.active,
            "ean": NeuerArtikel.ean,
            "shippingFree": NeuerArtikel.shippingFree,
            "deliveryTimeId": LIEFERZEIT_ID,
        }
        try:
            _ = client.request_post(
                request_url=PRODUCT, payload=product_payload, content_type="json"
            )

            if item.Bilder and len(item.Bilder) > 0:
                BilderSplit = item.Bilder.split("|")
                if len(BilderSplit) > 0:
                    image_count = 1
                    for x in reversed(BilderSplit):
                        print(
                            f"Bild {image_count} von {len(BilderSplit)} wird angelegt."
                        )
                        image_count += 1
                        FileName = os.path.basename(x)
                        FileSuffix = os.path.splitext(FileName)[1][1:]
                        MediaId = Uuid(x)
                        ProductMediaId = Uuid(MediaId)
                        try:
                            _ = client.request_post(
                                "/media",
                                {"id": MediaId, "mediaFolderId": MEDIA_FOLDER_ID},
                            )
                            _ = client.request_post(
                                f"_action/media/{MediaId}/upload",
                                {"mediaId": MediaId, "url": x},
                                "json",
                                {"extension": FileSuffix, "fileName": FileName},
                            )
                            _ = client.request_post(
                                SYNC,
                                {
                                    "Bulk-Bilder": {
                                        "entity": "product_media",
                                        "action": "upsert",
                                        "payload": [
                                            {
                                                "id": ProductMediaId,
                                                "productId": NeuerArtikel.id,
                                                "mediaId": MediaId,
                                            }
                                        ],
                                    }
                                },
                            )
                        except Exception as e:
                            print(f"Artikel: {item.Artikelnummer}")
                            print(f"Bei Bild: {x}")
                            print(f"Fehler im anlegen von Medien: {e}")
                            continue

                    try:
                        print(f"Cover für Artikel {item.Artikelnummer} wird angelegt.")
                        CoverId = Uuid(Uuid(BilderSplit[0]))
                        _ = client.request_patch(
                            f"product/{NeuerArtikel.id}",
                            {"coverId": CoverId},
                            "json",
                        )
                    except Exception as e:
                        print(f"Fehler im anlegen von Cover: {e}")
                        continue

        except Exception as e:
            print(f"Fehler beim anlegen: {e}")
            exit(1)

    return len(Artikel)


def delete_products(items: CSV_Package, Alle_Artikel: Any) -> int:
    Artikel = __sort_products(items.Artikel, "delete", Alle_Artikel)
    if len(Artikel) > 0:
        print(f"Es werden {len(Artikel)} gelöscht, da diese EOL sind.")
        client = get_api_client()
        payload: list[Any] = []
        for item in Artikel:
            if item.Artikelnummer:
                payload.append({"id": Uuid(item.Artikelnummer)})

        try:
            _ = client.request_post(
                SYNC,
                {
                    "Bulk-Delete": {
                        "entity": "product",
                        "action": "delete",
                        "payload": payload,
                    }
                },
            )
        except Exception as e:
            print(f"Fehler beim löschen: {e}")
            exit(1)

    return len(Artikel)


def __sort_products(
    items: list[ImportArtikel], action: str, Alle_Artikel: Any
) -> list[ImportArtikel]:

    Artikelnummern: list[str] = []
    tmp: list[ImportArtikel] = []
    for x in Alle_Artikel:
        Artikelnummern.append(x["productNumber"])

    if action == "new":
        for x in items:
            if x.Artikelnummer not in Artikelnummern:
                tmp.append(x)
    if action == "update":
        for x in items:
            if x.Artikelnummer in Artikelnummern:
                tmp.append(x)
    if action == "delete":
        ids: list[str] = []
        copy = items
        for csvArtikel in reversed(copy):
            if csvArtikel.Artikelnummer in Artikelnummern:
                copy.remove(csvArtikel)
                Artikelnummern.remove(csvArtikel.Artikelnummer)
            else:
                copy.remove(csvArtikel)

        for Artikelnummer in reversed(Artikelnummern):
            if Artikelnummer.startswith("K") or Artikelnummer.startswith("W"):
                ids.append(Uuid(Artikelnummer))

        # finde die passenden Artikel zum löschen
        for item in items:
            if item.Artikelnummer:
                if Uuid(item.Artikelnummer) in ids:
                    tmp.append(item)

    return tmp


def get_shop_products():
    start = time.time()
    print(f"Download start @ {start}")
    client = get_api_client()
    res = client.request_post_paginated(SEARCH_PRODUCT)["data"]
    end = time.time()
    print(f"Download end @ {end}")
    return res


def __send_payload(payload: Any) -> None:
    client = get_api_client()
    try:
        _ = client.request_post(
            SYNC,
            {
                "Bulk-Update": {
                    "entity": "product",
                    "action": "upsert",
                    "payload": payload,
                }
            },
        )
    except Exception as e:
        print(f"Fehler im Update: {e}")
        exit(1)
