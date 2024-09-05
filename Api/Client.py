from lib_shopware6_api_base import Shopware6AdminAPIClientBase, ConfShopware6ApiBase
from env import Env


def GetApiClient() -> Shopware6AdminAPIClientBase:
    env = Env()
    conf = ConfShopware6ApiBase()
    conf.client_id = env.CLIENT_ID
    conf.client_secret = env.CLIENT_SECRET
    conf.shopware_admin_api_url = env.BASE_URL + "/api"
    conf.grant_type = "resource_owner"
    client = Shopware6AdminAPIClientBase(conf)
    return client
