import codecs
import json
import attrs


class Uvp:
    def __init__(self):
        self.Artikelnummer: str | None = None
        self.Brutto: float | None = None
        self.Netto: float | None = None


class CustomAufschlag:
    def __init__(self):
        self.Kategorie: str | None = None
        self.Prozent: int | None = None


@attrs.define
class CategoryName(object):
    name: str | None = None


@attrs.define
class ManualCategories(object):
    name: str | None = None
    children: list[CategoryName] | None = None


class CategoryOverride:
    def __init__(self):
        self.Old: str | None = None
        self.New: str | None = None
        self.Index: int | None = None


class Config:
    def __init__(self):
        self.Aufschlag: int | None = None
        self.CustomAufschlag: list[CustomAufschlag] | None = None
        self.IgnoredCategories: list[str] | None = None
        self.IgnoredProducts: list[str] | None = None
        self.ManualCategories: list[ManualCategories] | None = None
        self.CategoryOverride: list[CategoryOverride] | None = None
        self.Uvp: list[Uvp] | None = None

    def Get_Config(self):
        with codecs.open("config.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.CustomAufschlag = []
        self.ManualCategories = []
        self.CategoryOverride = []
        for x in data["CustomAufschlag"]:
            tmpCA = CustomAufschlag()
            tmpCA.Kategorie = x["Kategorie"]
            tmpCA.Prozent = int(x["Prozent"])
            self.CustomAufschlag.append(tmpCA)
        for x in data["ManualCategories"]:
            tmpMA = ManualCategories()
            tmpMA.name = x["name"]
            tmpMA.children = []
            if len(x["children"]) > 0:
                for y in x["children"]:
                    z = CategoryName()
                    z.name = y["name"]
                    tmpMA.children.append(z)
            self.ManualCategories.append(tmpMA)

        for x in data["CategoryOverride"]:
            tmp2 = CategoryOverride()
            tmp2.Old = x["old"]
            tmp2.New = x["new"]
            tmp2.Index = int(x["index"])
            self.CategoryOverride.append(tmp2)

        self.Aufschlag = data["Aufschlag"]
        self.IgnoredCategories = data["IgnoredCategories"]
        self.IgnoredProducts = data["IgnoredProducts"]
        self.Uvp = []
        for x in data["UVP"]:
            tmp = Uvp()
            tmp.Artikelnummer = x["Artikelnummer"]
            tmp.Brutto = float(x["Brutto"])
            tmp.Netto = float(x["Netto"])
            self.Uvp.append(tmp)
