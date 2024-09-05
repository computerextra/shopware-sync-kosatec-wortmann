from typing import Any
from Api.Client import GetApiClient
from Api.Endpoints import SYNC
from Helper.Uuid import Uuid


def SyncManufacturer(Manufacturer: list[str]) -> None:
    client = GetApiClient()
    payload: list[Any] = []
    for name in Manufacturer:
        payload.append(
            {
                "id": Uuid(name),
                "name": name,
            }
        )
    try:
        _ = client.request_post(
            SYNC,
            {
                "Hersteller-Bulk": {
                    "entity": "product_manufacturer",
                    "action": "upsert",
                    "payload": payload,
                }
            },
        )
    except Exception as e:
        print(f"Manufacturer sync failed: {e}")
        exit(1)
