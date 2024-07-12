from Api.Client import get_api_client
from Api.Endpoints import SYNC
from Helper import Uuid
from typing import Any


def sync_manufacturer(manufacturer: list[str]) -> None:
    client = get_api_client()
    payload: list[Any] = []
    for name in manufacturer:
        payload.append(
            {
                "id": Uuid(name),
                "name": name,
            }
        )
    try:
        print(f"Es werden {len(payload)} Hersteller synchronisiert.")
        _ = client.request_post(
            SYNC,
            {
                "Hersteller": {
                    "entity": "product_manufacturer",
                    "action": "upsert",
                    "payload": payload,
                }
            },
        )
    except Exception as e:
        print(f"Fehler beim Anlegen von Herstellern: {e}")
        exit(1)
