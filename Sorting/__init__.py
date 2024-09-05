from typing import Any

from Files import Csv
from Files.Csv import ImportArtikel


def SortShopProducts(Products: Any):
    KosatecArtikel: list[ImportArtikel] = []
    WortmannArtikel: list[ImportArtikel] = []

    for item in Products:
        if item["productNumber"]:
            tmp = ImportArtikel()
            tmp.Artikelnummer = item["productNumber"]
            tmp.Bestand = item["stock"]
            tmp.HerstellerNummer = item["manufacturerNumber"]
            tmp.Name = item["name"]
            tmp.Ean = item["ean"]
            tmp.Ek = item["price"][0]["net"]
            tmp.Vk = item["price"][0]["gross"]
            if tmp.Artikelnummer:
                if tmp.Artikelnummer.startswith("K"):
                    KosatecArtikel.append(tmp)
                if tmp.Artikelnummer.startswith("W"):
                    WortmannArtikel.append(tmp)

    return (KosatecArtikel, WortmannArtikel)


def SortAllProducts(
    KosatecShop: list[ImportArtikel],
    WortmannShop: list[ImportArtikel],
    CsvProducts: list[ImportArtikel],
):
    newKosatec: list[ImportArtikel] = []
    oldKosatec: list[ImportArtikel] = []
    deleteKosatec: list[ImportArtikel] = []
    newWortmann: list[ImportArtikel] = []
    oldWortmann: list[ImportArtikel] = []
    deleteWortmann: list[ImportArtikel] = []

    for item in CsvProducts:
        if item.Artikelnummer:
            found = [x for x in KosatecShop if x.Artikelnummer == item.Artikelnummer]
            if not found:
                found = [
                    x for x in WortmannShop if x.Artikelnummer == item.Artikelnummer
                ]
                if not found:
                    if item.Artikelnummer.startswith("K"):
                        newKosatec.append(item)
                    if item.Artikelnummer.startswith("W"):
                        newWortmann.append(item)
                    continue

            if found:
                if item.Artikelnummer.startswith("K"):
                    oldKosatec.append(item)
                    KosatecShop.remove(found[0])
                if item.Artikelnummer.startswith("W"):
                    oldWortmann.append(item)
                    WortmannShop.remove(found[0])
                continue

    for item in KosatecShop:
        deleteKosatec.append(item)
    for item in WortmannShop:
        deleteWortmann.append(item)

    return (
        newKosatec,
        oldKosatec,
        deleteKosatec,
        newWortmann,
        oldWortmann,
        deleteWortmann,
    )
