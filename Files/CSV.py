import csv
import codecs
from Config.pickle_my_configs import get_config
from __config__ import WORTMANN_KATEGORIEN_IGNORE


class ImportArtikel:
    def __init__(self):
        self.Artikelnummer: str | None = None
        self.Bestand: str | None = None
        self.HerstellerNummer: str | None = None
        self.Name: str | None = None
        self.ean: str | None = None
        self.Beschreibung: str | None = None
        self.Hersteller: str | None = None
        self.Kategorie1: str | None = None  # Separator: |
        self.Kategorie2: str | None = None  # Separator: |
        self.Kategorie3: str | None = None  # Separator: |
        self.Kategorie4: str | None = None  # Separator: |
        self.Kategorie5: str | None = None  # Separator: |
        self.Kategorie6: str | None = None  # Separator: |
        self.ek: str | None = None
        self.vk: str | None = None  # Ohne MwSt!
        self.Bilder: str | None = None  # Separator: |


class CSV_Package:
    def __init__(self):
        self.Artikel: list[ImportArtikel] = []
        self.Hersteller: list[str] = []


class Kosatec_Row:
    def __init__(self):
        self.artnr: str | None = None
        self.herstnr: str | None = None
        self.artname: str | None = None
        self.hersteller: str | None = None
        self.hersturl: str | None = None
        self.ean: str | None = None
        self.hek: str | None = None  # decimal point: "."
        self.vkbrutto: str | None = None
        self.verfuegbar: str | None = None
        self.menge: str | None = None
        self.eta: str | None = None
        self.indate: str | None = None
        self.gewicht: str | None = None
        self.eol: str | None = None
        self.kat1: str | None = None
        self.kat2: str | None = None
        self.kat3: str | None = None
        self.kat4: str | None = None
        self.kat5: str | None = None
        self.kat6: str | None = None
        self.title: str | None = None
        self.short_desc: str | None = None
        self.short_summary: str | None = None
        self.long_summary: str | None = None
        self.marketing_text: str | None = None
        self.specs: str | None = None
        self.pdf: str | None = None
        self.pdf_manual: str | None = None
        self.images_s: str | None = None  # delimiter ";"
        self.images_m: str | None = None  # delimiter ";"
        self.images_l: str | None = None  # delimiter ";"
        self.images_xl: str | None = None  # delimiter ";"


class Wortmann_Product_Catalog_Row:
    def __init__(self) -> None:
        self.ProductId: str | None = None
        self.ReferenceNo: str | None = None
        self.EAN: str | None = None
        self.Manufacturer: str | None = None
        self.Price_B2B_Regular: str | None = None
        self.Price_B2B_Discounted: str | None = None
        self.Price_B2B_DiscountPercent: str | None = None
        self.Price_B2B_DiscountAmount: str | None = None
        self.Price_B2C_exclVAT: str | None = None
        self.Price_B2C_inclVAT: str | None = None  # decimal point: ","
        self.Price_B2C_VATRate: str | None = None
        self.Price_B2C_VATCountry: str | None = None
        self.Price_B2X_Currency: str | None = None
        self.Stock: str | None = None
        self.StockNextDelivery: str | None = None
        self.StockNextDeliveryAccessVolume: str | None = None
        self.WarrantyCode: str | None = None
        self.EOL: str | None = None
        self.Promotion: str | None = None
        self.NonReturnable: str | None = None
        self.RemainingStock: str | None = None
        self.ImagePrimary: str | None = None
        self.ImageAdditional: str | None = None  # delimiter "|"
        self.ProductLink: str | None = None
        self.GrossWeight: str | None = None
        self.NetWeight: str | None = None
        self.RelatedProducts: str | None = None
        self.AccessoryProducts: str | None = None
        self.Description_1031_German: str | None = None
        self.CategoryName_1031_German: str | None = None
        self.CategoryPath_1031_German: str | None = None
        self.WarrantyDescription_1031_German: str | None = None
        self.Description_1033_English: str | None = None
        self.CategoryName_1033_English: str | None = None
        self.CategoryPath_1033_English: str | None = None
        self.WarrantyDescription_1033_English: str | None = None
        self.Description_1036_French: str | None = None
        self.CategoryName_1036_French: str | None = None
        self.CategoryPath_1036_French: str | None = None
        self.WarrantyDescription_1036_French: str | None = None
        self.Description_1043_Dutch: str | None = None
        self.CategoryName_1043_Dutch: str | None = None
        self.CategoryPath_1043_Dutch: str | None = None
        self.WarrantyDescription_1043_Dutch: str | None = None
        self.ProductDisplayType: str | None = None
        self.LicenseTypeCode: str | None = None
        self.LicenseTypeDescription: str | None = None


class Wortmann_Content_Row:
    def __init__(self) -> None:
        self.ProductId: str | None = None
        self.PrintText_1031_German: str | None = None
        self.PrintText_1033_English: str | None = None
        self.PrintText_1036_French: str | None = None
        self.PrintText_1043_Dutch: str | None = None
        self.LongDescription_1031_German: str | None = None
        self.LongDescription_1033_English: str | None = None
        self.LongDescription_1036_French: str | None = None
        self.LongDescription_1043_Dutch: str | None = None


def parse_csv_files() -> CSV_Package:
    Artikel: list[ImportArtikel] = []
    Hersteller: list[str] = []
    Package = CSV_Package()

    config = get_config()

    # Read Kosatec File
    Kosatec_File: list[Kosatec_Row] = []
    reader = csv.reader(
        codecs.open("kosatec.csv", "r", "utf-8"), delimiter="\t", quotechar='"'
    )
    for row in reader:
        tmp = Kosatec_Row()
        tmp.artnr = row[0]
        tmp.herstnr = row[1]
        tmp.artname = row[2]
        tmp.hersteller = row[3]
        tmp.hersturl = row[4]
        tmp.ean = row[5]
        tmp.hek = row[6]
        tmp.vkbrutto = row[7]
        tmp.verfuegbar = row[8]
        tmp.menge = row[9]
        tmp.eta = row[10]
        tmp.indate = row[11]
        tmp.gewicht = row[12]
        tmp.eol = row[13]
        tmp.kat1 = row[14]
        tmp.kat2 = row[15]
        tmp.kat3 = row[16]
        tmp.kat4 = row[17]
        tmp.kat5 = row[18]
        tmp.kat6 = row[19]
        tmp.title = row[20]
        tmp.short_desc = row[21]
        tmp.short_summary = row[22]
        tmp.long_summary = row[23]
        tmp.marketing_text = row[24]
        tmp.specs = row[25]
        tmp.pdf = row[26]
        tmp.pdf_manual = row[27]
        tmp.images_s = row[28]
        tmp.images_m = row[29]
        tmp.images_l = row[30]
        tmp.images_xl = row[31]
        Kosatec_File.append(tmp)

    # Read Wortmann Files
    Wortmann_Product_Catalog_File: list[Wortmann_Product_Catalog_Row] = []
    Wortmann_Content_File: list[Wortmann_Content_Row] = []
    reader = csv.reader(
        codecs.open("productcatalog.csv", "r", "utf-8"), delimiter=";", quotechar='"'
    )
    for row in reader:
        tmp = Wortmann_Product_Catalog_Row()
        tmp.ProductId = row[0]
        tmp.ReferenceNo = row[1]
        tmp.EAN = row[2]
        tmp.Manufacturer = row[3]
        tmp.Price_B2B_Regular = row[4]
        tmp.Price_B2B_Discounted = row[5]
        tmp.Price_B2B_DiscountPercent = row[6]
        tmp.Price_B2B_DiscountAmount = row[7]
        tmp.Price_B2C_exclVAT = row[8]
        tmp.Price_B2C_inclVAT = row[9]
        tmp.Price_B2C_VATRate = row[10]
        tmp.Price_B2C_VATCountry = row[11]
        tmp.Price_B2X_Currency = row[12]
        tmp.Stock = row[13]
        tmp.StockNextDelivery = row[14]
        tmp.StockNextDeliveryAccessVolume = row[15]
        tmp.WarrantyCode = row[16]
        tmp.EOL = row[17]
        tmp.Promotion = row[18]
        tmp.NonReturnable = row[19]
        tmp.RemainingStock = row[20]
        tmp.ImagePrimary = row[21]
        tmp.ImageAdditional = row[22]
        tmp.ProductLink = row[23]
        tmp.GrossWeight = row[24]
        tmp.NetWeight = row[25]
        tmp.RelatedProducts = row[26]
        tmp.AccessoryProducts = row[27]
        tmp.Description_1031_German = row[28]
        tmp.CategoryName_1031_German = row[29]
        tmp.CategoryPath_1031_German = row[30]
        tmp.WarrantyDescription_1031_German = row[31]
        tmp.Description_1033_English = row[32]
        tmp.CategoryName_1033_English = row[33]
        tmp.CategoryPath_1033_English = row[34]
        tmp.WarrantyDescription_1033_English = row[35]
        tmp.Description_1036_French = row[36]
        tmp.CategoryName_1036_French = row[37]
        tmp.CategoryPath_1036_French = row[38]
        tmp.WarrantyDescription_1036_French = row[39]
        tmp.Description_1043_Dutch = row[40]
        tmp.CategoryName_1043_Dutch = row[41]
        tmp.CategoryPath_1043_Dutch = row[42]
        tmp.WarrantyDescription_1043_Dutch = row[43]
        tmp.ProductDisplayType = row[44]
        tmp.LicenseTypeCode = row[45]
        tmp.LicenseTypeDescription = row[46]
        Wortmann_Product_Catalog_File.append(tmp)

    reader = csv.reader(
        codecs.open("content.csv", "r", "utf-8"), delimiter=";", quotechar='"'
    )
    for row in reader:
        tmp = Wortmann_Content_Row()
        tmp.ProductId = row[0]
        tmp.PrintText_1031_German = row[1]
        tmp.PrintText_1033_English = row[2]
        tmp.PrintText_1036_French = row[3]
        tmp.PrintText_1043_Dutch = row[4]
        tmp.LongDescription_1031_German = row[5]
        tmp.LongDescription_1033_English = row[6]
        tmp.LongDescription_1036_French = row[7]
        tmp.LongDescription_1043_Dutch = row[8]
        Wortmann_Content_File.append(tmp)

    # Sort Wortmann Files
    for Wortmann_Row_Artikel in Wortmann_Product_Catalog_File:
        if (
            Wortmann_Row_Artikel.Manufacturer
            and Wortmann_Row_Artikel.CategoryName_1031_German
            and config.IgnoredCategories
            and Wortmann_Row_Artikel.ProductId
            and config.IgnoredProducts
            and Wortmann_Row_Artikel.Description_1031_German
            and Wortmann_Row_Artikel.Manufacturer.strip() == "WORTMANN AG"
            and Wortmann_Row_Artikel.CategoryName_1031_German
            not in config.IgnoredCategories
            and Wortmann_Row_Artikel.ProductId not in config.IgnoredProducts
            and Wortmann_Row_Artikel.ProductId not in WORTMANN_KATEGORIEN_IGNORE
            and not Wortmann_Row_Artikel.Description_1031_German.startswith(
                "TERRA CLOUD"
            )
        ):
            tmp = ImportArtikel()
            tmp.Artikelnummer = "W" + Wortmann_Row_Artikel.ProductId.strip()
            tmp.Hersteller = Wortmann_Row_Artikel.Manufacturer.strip()
            tmp.ean = (
                Wortmann_Row_Artikel.EAN.strip() if Wortmann_Row_Artikel.EAN else ""
            )
            if Wortmann_Row_Artikel.Price_B2C_inclVAT:
                tmp.vk = Wortmann_Row_Artikel.Price_B2C_inclVAT.strip()
            else:
                continue
            tmp.Bestand = (
                Wortmann_Row_Artikel.Stock.strip()
                if Wortmann_Row_Artikel.Stock
                else "0"
            )
            tmp.Bilder = ""
            if Wortmann_Row_Artikel.ImagePrimary:
                tmp.Bilder += Wortmann_Row_Artikel.ImagePrimary.strip()
            if (
                Wortmann_Row_Artikel.ImageAdditional
                and len(Wortmann_Row_Artikel.ImageAdditional) > 0
            ):
                tmp.Bilder += "|" + Wortmann_Row_Artikel.ImageAdditional.strip()

            kat = Wortmann_Row_Artikel.CategoryName_1031_German.strip()
            tmp.Kategorie1 = kat
            if kat == "PC":
                tmp.Kategorie1 = "Marken PCs"
            if kat == "LCD":
                tmp.Kategorie1 = "Monitore"
            if kat == "Dockingstations":
                tmp.Kategorie1 = "Zubehör Notebooks"
            if kat == "PC- & Netzwerkkameras":
                tmp.Kategorie1 = "WebCams"
            if kat == "PAD":
                tmp.Kategorie1 = "Tablets"
            if kat == "Taschen":
                tmp.Kategorie1 = "Notebooktaschen"
            if kat == "MOBILE":
                tmp.Kategorie1 = "Notebooks"
            if kat == "FIREWALL":
                tmp.Kategorie1 = "Firewall"
            if kat == "Headset & Mikro":
                tmp.Kategorie1 = "Kopfhörer & Headsets"
            if kat == "THINCLIENT":
                tmp.Kategorie1 = "Mini-PC / Barebones"
            if kat == "ALL-IN-ONE":
                tmp.Kategorie1 = "All in One PC-Systeme"
            Artikel.append(tmp)

    for Wortmann_Row_Artikel in Wortmann_Content_File:
        tmp = ImportArtikel()
        findung: ImportArtikel | None = None
        if Wortmann_Row_Artikel.ProductId:
            findung = next(
                (
                    x
                    for x in Artikel
                    if x.Artikelnummer == "W" + Wortmann_Row_Artikel.ProductId
                ),
                None,
            )
        index: int | None = None
        if findung:
            index = Artikel.index(findung)

        if index:
            Artikel[index].Beschreibung = (
                Wortmann_Row_Artikel.LongDescription_1031_German
            )

    # Sort Kosatec Artikel
    for Kosatec_Row_Artikel in Kosatec_File:
        if not Kosatec_Row_Artikel.artnr:
            continue
        if (
            config.IgnoredProducts
            and Kosatec_Row_Artikel.artnr.strip() in config.IgnoredProducts
        ):
            continue
        if not Kosatec_Row_Artikel.hek:
            continue
        if not Kosatec_Row_Artikel.artname:
            continue
        if len(Kosatec_Row_Artikel.artname) < 1:
            continue
        if Kosatec_Row_Artikel.artnr.strip() == "artnr":
            continue
        if not Kosatec_Row_Artikel.kat1:
            continue
        if len(Kosatec_Row_Artikel.kat1.strip()) < 1:
            continue
        if not Kosatec_Row_Artikel.hersteller:
            continue
        if len(Kosatec_Row_Artikel.hersteller.strip()) < 1:
            continue
        if (
            Kosatec_Row_Artikel.kat1
            and config.IgnoredCategories
            and Kosatec_Row_Artikel.kat1.strip() in config.IgnoredCategories
        ):
            continue
        if (
            Kosatec_Row_Artikel.kat2
            and config.IgnoredCategories
            and Kosatec_Row_Artikel.kat2.strip() in config.IgnoredCategories
        ):
            continue
        if (
            Kosatec_Row_Artikel.kat3
            and config.IgnoredCategories
            and Kosatec_Row_Artikel.kat3.strip() in config.IgnoredCategories
        ):
            continue
        if (
            Kosatec_Row_Artikel.kat4
            and config.IgnoredCategories
            and Kosatec_Row_Artikel.kat4.strip() in config.IgnoredCategories
        ):
            continue
        if (
            Kosatec_Row_Artikel.kat5
            and config.IgnoredCategories
            and Kosatec_Row_Artikel.kat5.strip() in config.IgnoredCategories
        ):
            continue
        if (
            Kosatec_Row_Artikel.kat6
            and config.IgnoredCategories
            and Kosatec_Row_Artikel.kat6.strip() in config.IgnoredCategories
        ):
            continue

        tmp = ImportArtikel()
        tmp.Artikelnummer = "K" + Kosatec_Row_Artikel.artnr.strip()
        if Kosatec_Row_Artikel.herstnr:
            tmp.HerstellerNummer = Kosatec_Row_Artikel.herstnr.strip()
        else:
            tmp.HerstellerNummer = ""

        tmp.Name = Kosatec_Row_Artikel.artname.strip()
        tmp.Hersteller = Kosatec_Row_Artikel.hersteller.strip()
        Hersteller.append(Kosatec_Row_Artikel.hersteller.strip())
        if Kosatec_Row_Artikel.ean:
            tmp.ean = Kosatec_Row_Artikel.ean.strip()
        else:
            tmp.ean = ""

        tmp.ek = Kosatec_Row_Artikel.hek.strip()
        if Kosatec_Row_Artikel.menge:
            tmp.Bestand = Kosatec_Row_Artikel.menge.strip()
        else:
            tmp.Bestand = "0"

        # Sortiere Kategorien
        if config.CategoryOverride and len(config.CategoryOverride) > 0:
            for x in config.CategoryOverride:
                tmp.Kategorie1 = (
                    x.new
                    if x.index == 1 and Kosatec_Row_Artikel.kat1.strip() == x.old
                    else Kosatec_Row_Artikel.kat1.strip()
                )
                if Kosatec_Row_Artikel.kat2:
                    tmp.Kategorie2 = (
                        x.new
                        if x.index == 2 and Kosatec_Row_Artikel.kat2.strip() == x.old
                        else Kosatec_Row_Artikel.kat2.strip()
                    )
                if Kosatec_Row_Artikel.kat3:
                    tmp.Kategorie3 = (
                        x.new
                        if x.index == 3 and Kosatec_Row_Artikel.kat3.strip() == x.old
                        else Kosatec_Row_Artikel.kat3.strip()
                    )
                if Kosatec_Row_Artikel.kat4:
                    tmp.Kategorie4 = (
                        x.new
                        if x.index == 4 and Kosatec_Row_Artikel.kat4.strip() == x.old
                        else Kosatec_Row_Artikel.kat4.strip()
                    )
                if Kosatec_Row_Artikel.kat5:
                    tmp.Kategorie5 = (
                        x.new
                        if x.index == 5 and Kosatec_Row_Artikel.kat5.strip() == x.old
                        else Kosatec_Row_Artikel.kat5.strip()
                    )
                if Kosatec_Row_Artikel.kat6:
                    tmp.Kategorie6 = (
                        x.new
                        if x.index == 6 and Kosatec_Row_Artikel.kat6.strip() == x.old
                        else Kosatec_Row_Artikel.kat6.strip()
                    )
        else:
            tmp.Kategorie1 = (
                Kosatec_Row_Artikel.kat1.strip()
                if Kosatec_Row_Artikel.kat1
                and len(Kosatec_Row_Artikel.kat1.strip()) > 0
                else None
            )
            tmp.Kategorie2 = (
                Kosatec_Row_Artikel.kat2.strip()
                if Kosatec_Row_Artikel.kat2
                and len(Kosatec_Row_Artikel.kat2.strip()) > 0
                else None
            )
            tmp.Kategorie3 = (
                Kosatec_Row_Artikel.kat3.strip()
                if Kosatec_Row_Artikel.kat3
                and len(Kosatec_Row_Artikel.kat3.strip()) > 0
                else None
            )
            tmp.Kategorie4 = (
                Kosatec_Row_Artikel.kat4.strip()
                if Kosatec_Row_Artikel.kat4
                and len(Kosatec_Row_Artikel.kat4.strip()) > 0
                else None
            )
            tmp.Kategorie5 = (
                Kosatec_Row_Artikel.kat5.strip()
                if Kosatec_Row_Artikel.kat5
                and len(Kosatec_Row_Artikel.kat5.strip()) > 0
                else None
            )
            tmp.Kategorie6 = (
                Kosatec_Row_Artikel.kat6.strip()
                if Kosatec_Row_Artikel.kat6
                and len(Kosatec_Row_Artikel.kat6.strip()) > 0
                else None
            )

        tmp.Beschreibung = (
            (
                Kosatec_Row_Artikel.marketing_text.strip()
                if Kosatec_Row_Artikel.marketing_text
                else ""
            )
            + "<br>"
            + (
                Kosatec_Row_Artikel.long_summary.strip()
                if Kosatec_Row_Artikel.long_summary
                else ""
            )
            + "<br>"
            + (Kosatec_Row_Artikel.specs.strip() if Kosatec_Row_Artikel.specs else "")
        )

        tmp.Bilder = (
            Kosatec_Row_Artikel.images_xl.replace(";", "|")
            if Kosatec_Row_Artikel.images_xl and len(Kosatec_Row_Artikel.images_xl) > 0
            else (
                Kosatec_Row_Artikel.images_l.replace(";", "|")
                if Kosatec_Row_Artikel.images_l
                and len(Kosatec_Row_Artikel.images_l) > 0
                else (
                    Kosatec_Row_Artikel.images_m.replace(";", "|")
                    if Kosatec_Row_Artikel.images_m
                    and len(Kosatec_Row_Artikel.images_m) > 0
                    else (
                        Kosatec_Row_Artikel.images_s.replace(";", "|")
                        if Kosatec_Row_Artikel.images_s
                        and len(Kosatec_Row_Artikel.images_s) > 0
                        else ""
                    )
                )
            )
        )
        Artikel.append(tmp)

    # Sortiere Hersteller
    Hersteller = list(set(Hersteller))
    Hersteller.append("WORTMANN AG")

    Package.Artikel = Artikel
    Package.Hersteller = Hersteller
    return Package
