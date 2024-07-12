from typing import Any


class Shopware6Category:
    def __init__(self):
        self.name: str | None = None
        self.id: str | None = None
        self.parentId: str | None = None
        self.active: bool | None = None
        self.displayNestedProducts: bool | None = None
        self.type: str = "page"
        self.productAssignmentType = "product"


class Shopware6NewProduct:
    def __init__(self):
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


class Shopware6UpdateProdukt:
    #  Aufbau des Artikel Payloads für die Shopware Api um Artikel zu aktualisieren
    def __init__(self):
        self.id: str | None = None
        self.stock: int | None = None
        self.price: Shopware6ProduktPreis | None = None


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
