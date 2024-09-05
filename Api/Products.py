from typing import Any

from lib_shopware6_api_base import os

from Api.Client import GetApiClient
from Api.Endpoints import PRODUCT, SEARCH_PRODUCT, SYNC
from Api.Tax import GetTax
from Files.Csv import ImportArtikel
from Helper.Uuid import Uuid
from config import Config
from env import Env


MAX_UPLOAD = 500


class Shopware6Category:
    def __init__(self):
        self.name: str | None = None
        self.id: str | None = None
        self.parentId: str | None = None
        self.active: bool | None = None
        self.displayNestedProducts: bool | None = None
        self.type: str = "page"
        self.productAssignmentType = "product"


class Shopware6ProduktPreis:
    #  Aufbau des Preis Payloads für die Shopware Api
    def __init__(self):
        self.currencyId: str | None = None
        self.net: float | None = None
        self.gross: float | None = None
        self.linked: bool = True
        self.listPrice = None
        self.percentage = None
        self.regulationPrice = None
        self.extensions: list[dict[Any, Any]] = [{}]
        self.apiAlias: str = "price"


class Shopware6Cover:
    #  Aufbau des Produkt Cover Payloads für die Shopware Api
    def __init__(self):
        self.productId: str | None = None
        self.mediaId: str | None = None
        self.media: Shopware6Media | None = None


class Shopware6Media:
    #  Aufbau des Media Payloads für die Shopware Api
    def __init__(self):
        self.id: str | None = None
        self.mediaFolderId: str | None = None
        self.media: Media | None = None


class Media:
    #  Aufbau des Media Payloads für die Shopware Api um ein Bild per URL hochzuladen
    def __init__(self):
        self.id: str | None = None
        self.url: str | None = None


class Shopware6NewProduct:
    def __init__(self) -> None:
        self.id: str | None = None
        self.taxId: str | None = None
        self.coverId: str | None = None
        self.price: list[Shopware6ProduktPreis] | None = None
        self.productNumber: str | None = None
        self.stock: int | None = None
        self.active: bool | None = None
        self.manufacturerNumber: str | None = None
        self.shippingFree: bool = False
        self.name: str | None = None
        self.ean: str | None = None
        self.description: str | None = None
        self.manufacturer: dict[Any, Any] = {"id": None}
        self.categories: list[dict[Any, Any]] = [{"id": None}]
        self.visibilities: list[dict[Any, Any]] = [
            {
                "salesChannelId": None,
                "visibility": 30,
            }
        ]
        self.cover: Shopware6Cover | None = None
        self.media: list[Shopware6Media] | None = None


def GetShopProducts():
    client = GetApiClient()
    res = client.request_post_paginated(SEARCH_PRODUCT)["data"]
    return res


def UpdateProducts(Kosatec: list[ImportArtikel], Wortmann: list[ImportArtikel]) -> None:
    env = Env()
    count = 0
    payload: list[Any] = []

    config = Config()
    config.Get_Config()
    tax = GetTax()

    All: list[ImportArtikel] = []
    for x in Kosatec:
        All.append(x)
    for x in Wortmann:
        All.append(x)
    print(f"Es werden insgesamt {len(All)} Artikel synchronisiert")
    rest = len(All)
    for item in All:
        if not item.Artikelnummer:
            continue
        if count >= MAX_UPLOAD:
            print(f"Es werden {count} von insgesamt {len(All)} Artikeln aktualisiert.")
            rest = rest - count
            print(
                f"Noch {rest} Artikel verbleibend. ({(((rest / len(All)) * 100) - 100) * -1}%)"
            )
            __sendPayload(payload)
            payload = []
            count = 0
        count += 1
        Kategorie = __find_Category(item)
        vkBrutto = 0
        if item.Ek and len(item.Ek) > 0:
            vkBrutto = __calc_price(item.Ek, Kategorie, item.Artikelnummer)
        if item.Vk and len(item.Vk) > 0:
            vkBrutto = float(item.Vk.replace(",", "."))
        vkNetto = vkBrutto / tax
        if config.Uvp and len(config.Uvp) > 0:
            for uvp in config.Uvp:
                if item.Artikelnummer == uvp.Artikelnummer:
                    vkBrutto = uvp.Brutto
                    vkNetto = uvp.Netto
        Bestand = int(item.Bestand) if item.Bestand else 0
        Aktiv = True if Bestand > 0 else False
        payload.append(
            {
                "id": Uuid(item.Artikelnummer),
                "deliveryTimeId": env.LIEFERZEIT_ID,
                "price": [
                    {
                        "currencyId": env.CURRENCY_ID,
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
        print(f"Es werden {count} von insgesamt {len(All)} Artikeln aktualisiert.")
        __sendPayload(payload)


def DeleteProducts(Kosatec: list[ImportArtikel], Wortmann: list[ImportArtikel]) -> None:
    print("Start deleting Products")
    All: list[ImportArtikel] = []
    for x in Kosatec:
        All.append(x)
    for x in Wortmann:
        All.append(x)
    print(f"{len(All)} products will be removed")
    client = GetApiClient()
    payload: list[Any] = []

    for item in All:
        if item.Artikelnummer:
            payload.append({"id": Uuid(item.Artikelnummer)})
    if len(payload) > 0:
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
            print(f"Bulk Deletion Failed: {e}")
            exit(1)
    print("Products deleted")


def CreateProducts(Kosatec: list[ImportArtikel], Wortmann: list[ImportArtikel]) -> None:
    env = Env()
    tax = GetTax()

    All: list[ImportArtikel] = []
    for x in Kosatec:
        All.append(x)
    for x in Wortmann:
        All.append(x)

    count = 1
    for item in All:
        client = GetApiClient()
        print(f"Product {item.Artikelnummer}: {count} of {len(All)} will be created.")
        count += 1
        if not item.Artikelnummer:
            continue
        if not item.Name:
            continue
        NeuerArtikel = Shopware6NewProduct()
        NeuerArtikel.name = item.Name.strip()
        NeuerArtikel.id = Uuid(item.Artikelnummer)
        NeuerArtikel.taxId = env.TAX_ID
        NeuerArtikel.categories = [{"id": Uuid(__find_Category(item))}]
        vkBrutto: float = 0
        if item.Ek and len(item.Ek) > 0:
            vkBrutto = __calc_price(item.Ek, __find_Category(item), item.Artikelnummer)
        if item.Vk and len(item.Vk) > 0:
            vkBrutto = float(item.Vk.replace(",", "."))
        NeuerArtikel.price = []

        price = Shopware6ProduktPreis()
        price.currencyId = env.CURRENCY_ID
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
                "salesChannelId": env.SALES_CHANNEL_ID,
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
            "deliveryTimeId": env.LIEFERZEIT_ID,
        }
        try:
            _ = client.request_post(
                request_url=PRODUCT, payload=product_payload, content_type="json"
            )

        except Exception as e:
            print(f"Product creation Failed!: {e}")
            continue

        if item.Bilder and len(item.Bilder) > 0:
            BilderSplit = item.Bilder.split("|")
            if len(BilderSplit) > 0:
                image_count = 1
                for x in reversed(BilderSplit):
                    print(f"Image {image_count} of {len(BilderSplit)} will be created.")
                    image_count += 1
                    FileName = os.path.basename(x)
                    FileSuffix = os.path.splitext(FileName)[1][1:]
                    MediaId = Uuid(x)
                    ProductMediaId = Uuid(MediaId)
                    brokenImage = False
                    try:
                        _ = client.request_post(
                            SYNC,
                            {
                                "Bulk-Media": {
                                    "entity": "media",
                                    "action": "upsert",
                                    "payload": [
                                        {
                                            "id": MediaId,
                                            "mediaFolderId": env.MEDIA_FOLDER_ID,
                                        }
                                    ],
                                }
                            },
                        )
                    except Exception as e:
                        print(f"Product Image: {item.Artikelnummer}: {e}")
                        brokenImage = True
                        continue
                    try:
                        if not brokenImage:
                            continue
                        _ = client.request_post(
                            f"_action/media/{MediaId}/upload",
                            {"mediaId": MediaId, "url": x},
                            "json",
                            {"extension": FileSuffix, "fileName": FileName},
                        )
                    except Exception as e:
                        print(f"{item.Artikelnummer}: Bild: {x}: {e}")
                        continue
                    try:
                        if not brokenImage:
                            continue
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
                        print(
                            f"{item.Artikelnummer} Product Media creation failed: {e}"
                        )
                        continue

                try:
                    print(f"Cover of Product {item.Artikelnummer} will be created.")
                    CoverId = Uuid(Uuid(BilderSplit[0]))
                    _ = client.request_patch(
                        f"product/{NeuerArtikel.id}",
                        {"coverId": CoverId},
                        "json",
                    )
                except Exception as e:
                    print(f"Cover creation failed: {e}")
                    continue

    return


def __sendPayload(payload: list[Any]) -> None:
    client = GetApiClient()
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
        print(f"Bulk Update failed!: {e}")
        exit(1)
    return


def __find_Category(Item: ImportArtikel) -> str:
    cat = ""
    if Item.Kategorie1 and len(Item.Kategorie1) > 1:
        cat = Item.Kategorie1
    if Item.Kategorie2 and len(Item.Kategorie2) > 1:
        cat = Item.Kategorie2
    if Item.Kategorie3 and len(Item.Kategorie3) > 1:
        cat = Item.Kategorie3
    if Item.Kategorie4 and len(Item.Kategorie4) > 1:
        cat = Item.Kategorie4
    if Item.Kategorie5 and len(Item.Kategorie5) > 1:
        cat = Item.Kategorie5
    if Item.Kategorie6 and len(Item.Kategorie6) > 1:
        cat = Item.Kategorie6
    return cat


def __calc_price(ek: str, cat: str, art: str) -> float:
    config = Config()
    config.Get_Config()
    tax = GetTax()
    Aufschlag = config.Aufschlag if config.Aufschlag else 20
    if config.CustomAufschlag and len(config.CustomAufschlag) > 0:
        for cA in config.CustomAufschlag:
            if cat == cA.Kategorie:
                Aufschlag = cA.Prozent
    if not Aufschlag:
        Aufschlag = 20
    AufschlagProzent = (Aufschlag / 100) + 1
    price = float(ek) * AufschlagProzent
    taxPercent = (tax / 100) + 1
    vk = price * taxPercent
    vk = round(vk / 5) * 5
    vk -= 0.1

    if vk < 9.90:
        vk = 9.90
    Gewinn = (vk / taxPercent) - float(ek)
    if Gewinn < 5.0:
        return __calc_price(str(float(ek) + 5), cat, art)

    return vk
