from Api.Client import GetApiClient
from Api.Endpoints import SEARCH_TAX
from env import Env


def GetTax() -> int:
    env = Env()
    client = GetApiClient()
    try:
        res = client.request_post(SEARCH_TAX, {"ids": env.TAX_ID})["data"]
        tax = res[0]["taxRate"]
        return int(tax)
    except Exception as e:
        print(f"POST Request Error on GetTax: {e}")
        exit(1)
