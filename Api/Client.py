from lib_shopware6_api_base import Shopware6AdminAPIClientBase, ConfShopware6ApiBase
from __config__ import CLIENT_ID, CLIENT_SECRET, BASE_URL


def get_api_client() -> Shopware6AdminAPIClientBase:
    conf = ConfShopware6ApiBase()
    conf.client_id = CLIENT_ID
    conf.client_secret = CLIENT_SECRET
    conf.shopware_admin_api_url = BASE_URL + "/api"
    conf.grant_type = "resource_owner"
    client = Shopware6AdminAPIClientBase(config=conf)  # type: ignore
    return client
