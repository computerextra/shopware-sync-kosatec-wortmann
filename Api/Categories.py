from typing import Any

from Api.Client import GetApiClient
from Api.Endpoints import SYNC
from Api.Products import Shopware6Category
from Files.Csv import ImportArtikel
from Helper.Uuid import Uuid
from config import Config
from env import Env


def SyncCategories(items: list[ImportArtikel]) -> None:
    config = Config()
    config.Get_Config()
    env = Env()
    client = GetApiClient()
    payload: list[Shopware6Category] = []

    if config.ManualCategories:
        for item in config.ManualCategories:

            if item.name:
                payload.append(__catHelper(item.name, env.MAIN_CATEGORY_ID))
                if item.children and len(item.children) > 0:
                    for child in item.children:
                        if child.name:
                            payload.append(
                                __catHelper(child.name, Uuid(item.name))
                            )
    if config.ManualCategories:
        for item in config.ManualCategories:
            if item.name:
                payload.append(__catHelper(item.name, env.MAIN_CATEGORY_ID))
                if item.children and len(item.children) > 0:
                    for child in item.children:
                        if child.name:
                            name = item.name
                            payload.append(__catHelper(child.name, Uuid(name)))

    if len(payload) > 0:
        shopware_payload: list[Any] = []
        for item in payload:
            shopware_payload.append(
                {
                    "id": item.id,
                    "name": item.name,
                    "parentId": item.parentId,
                    "active": item.active,
                    "displayNestedProducts": item.displayNestedProducts,
                    "type": item.type,
                    "productAssignmentType": item.productAssignmentType,
                }
            )

        try:
            print(f"Es werden {len(payload)} Kategorien vom Hauptmenü synchronisiert.")
            _ = client.request_post(
                SYNC,
                {
                    "Kategorien": {
                        "entity": "category",
                        "action": "upsert",
                        "payload": shopware_payload,
                    }
                },
            )

        except Exception as e:
            print(f"Fehler beim Anlegen des Hauptmenüs {e}")
            exit(1)

    payload = []
    shopware_payload = []

    for Artikel in items:
        if Artikel.Artikelnummer and not Artikel.Artikelnummer.startswith("K"):
            continue
        if Artikel.Kategorie1 and len(Artikel.Kategorie1) > 0:
            parent_id = ""
            if config.ManualCategories:
                for pos in config.ManualCategories:
                    if (
                        pos.name
                        and Artikel.Kategorie1
                        and Artikel.Kategorie1.strip() == pos.name.strip()
                    ):
                        parent_id = env.MAIN_CATEGORY_ID
                    elif pos.children and len(pos.children) > 0:
                        for child in pos.children:
                            if (
                                child.name
                                and pos.name
                                and child.name.strip() == Artikel.Kategorie1.strip()
                            ):
                                parent_id = Uuid(pos.name)
            if parent_id == "":
                parent_id = env.MAIN_CATEGORY_ID
            payload.append(__catHelper(Artikel.Kategorie1.strip(), parent_id))

        if Artikel.Kategorie1 and Artikel.Kategorie2 and len(Artikel.Kategorie2) > 0:
            payload.append(
                __catHelper(
                    Artikel.Kategorie2.strip(), Uuid(Artikel.Kategorie1.strip())
                )
            )
        if Artikel.Kategorie2 and Artikel.Kategorie3 and len(Artikel.Kategorie3) > 0:
            payload.append(
                __catHelper(
                    Artikel.Kategorie3.strip(), Uuid(Artikel.Kategorie2.strip())
                )
            )
        if Artikel.Kategorie3 and Artikel.Kategorie4 and len(Artikel.Kategorie4) > 0:
            payload.append(
                __catHelper(
                    Artikel.Kategorie4.strip(), Uuid(Artikel.Kategorie3.strip())
                )
            )
        if Artikel.Kategorie4 and Artikel.Kategorie5 and len(Artikel.Kategorie5) > 0:
            payload.append(
                __catHelper(
                    Artikel.Kategorie5.strip(), Uuid(Artikel.Kategorie4.strip())
                )
            )
        if Artikel.Kategorie5 and Artikel.Kategorie6 and len(Artikel.Kategorie6) > 0:
            payload.append(
                __catHelper(
                    Artikel.Kategorie6.strip(), Uuid(Artikel.Kategorie5.strip())
                )
            )

    # doppelte Einträge entfernen
    tmp: set[Any] = set()
    Uniques: list[Shopware6Category] = []
    for item in payload:
        if item.id not in tmp:
            tmp.add(item.id)
            Uniques.append(item)

    shopware_payload: list[Any] = []
    for item in Uniques:
        shopware_payload.append(
            {
                "id": item.id,
                "name": item.name,
                "parentId": item.parentId,
                "active": item.active,
                "displayNestedProducts": item.displayNestedProducts,
                "type": item.type,
                "productAssignmentType": item.productAssignmentType,
            }
        )
    try:
        print(f"Es werden {len(shopware_payload)} Kategorien synchronisiert.")
        client.request_post(
            SYNC,
            {
                "Kategorien": {
                    "entity": "category",
                    "action": "upsert",
                    "payload": shopware_payload,
                }
            },
        )
    except Exception as e:
        print(f"Fehler beim Anlegen der Kategorien {e}")
        exit(1)


def __catHelper(name: str, parent_id: str) -> Shopware6Category:
    cat = Shopware6Category()
    cat.id = Uuid(name)
    cat.active = True
    cat.displayNestedProducts = True
    cat.name = name
    cat.parentId = parent_id
    return cat
