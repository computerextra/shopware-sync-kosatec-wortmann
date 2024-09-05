from typing import Any
import uuid

from env import Env


def Uuid(name: Any) -> str:
    env = Env()
    ret = ""
    try:
        if type(name) is str:
            ret = str(
                object=uuid.uuid5(namespace=uuid.UUID(hex=env.MY_NAMESPACE), name=name)
            ).replace("-", "")
        if type(name) is dict:
            ret = str(
                object=uuid.uuid5(
                    namespace=uuid.UUID(hex=env.MY_NAMESPACE), name=name["name"]
                )
            ).replace("-", "")
    except Exception as e:
        print(f"Failed to create a UUID with name: {name}\nError: {e}")
        exit(1)

    return ret
