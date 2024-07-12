from Api.Client import get_api_client
from Api.Endpoints import SEARCH_TAX
from __config__ import TAX_ID


def get_tax() -> int:
    client = get_api_client()
    try:
        res = client.request_post(SEARCH_TAX, {"ids": TAX_ID})["data"]
        tax = res[0]["taxRate"]
        return int(tax)
    except Exception as e:
        print(f"Fehler beim request von TAX: {e}")
        exit(1)
