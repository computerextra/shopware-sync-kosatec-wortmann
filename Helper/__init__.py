import os
import uuid
from __config__ import MY_NAMESPACE, DEFAULT_AUFSCHLAG, DEFAULT_MIN_PREIS
from Files.CSV import ImportArtikel
from Config.pickle_my_configs import get_config
from Api.Tax import get_tax

tax = get_tax()


def check_if_file_exists(path: str) -> bool:
    return os.path.isfile(path)


def delete_file(path: str) -> None:
    if check_if_file_exists(path):
        os.remove(path)


def Uuid(name: str) -> str:
    return str(
        object=uuid.uuid5(namespace=uuid.UUID(hex=MY_NAMESPACE), name=name)
    ).replace("-", "")


def find_category(Artikel: ImportArtikel) -> str:
    cat = ""
    if Artikel.Kategorie1 and len(Artikel.Kategorie1) > 1:
        cat = Artikel.Kategorie1
    if Artikel.Kategorie2 and len(Artikel.Kategorie2) > 1:
        cat = Artikel.Kategorie2
    if Artikel.Kategorie3 and len(Artikel.Kategorie3) > 1:
        cat = Artikel.Kategorie3
    if Artikel.Kategorie4 and len(Artikel.Kategorie4) > 1:
        cat = Artikel.Kategorie4
    if Artikel.Kategorie5 and len(Artikel.Kategorie5) > 1:
        cat = Artikel.Kategorie5
    if Artikel.Kategorie6 and len(Artikel.Kategorie6) > 1:
        cat = Artikel.Kategorie6
    return cat


def calculate_price(ek: str, cat: str, art: str) -> float:
    Aufschlag = DEFAULT_AUFSCHLAG
    config = get_config()
    if config.Aufschlag:
        Aufschlag = int(config.Aufschlag)

    if config.CustomAufschlag and len(config.CustomAufschlag) > 0:
        for cA in config.CustomAufschlag:
            if cat == cA.Kategorie:
                Aufschlag = cA.Prozent
    if not Aufschlag:
        Aufschlag = DEFAULT_AUFSCHLAG
    AufschlagProzent = (Aufschlag / 100) + 1
    price = float(ek) * AufschlagProzent
    taxPercent = (tax / 100) + 1
    vk = price * taxPercent
    vk = round(vk / 5) * 5
    vk -= 0.1

    if vk < DEFAULT_MIN_PREIS:
        vk = DEFAULT_MIN_PREIS
    Gewinn = (vk / taxPercent) - float(ek)
    if Gewinn < 5.0:
        return calculate_price(str(float(ek) + 5.0), cat, art)

    return vk
