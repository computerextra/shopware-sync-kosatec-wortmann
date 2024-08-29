import codecs
import json


class Uvp:
    def __init__(self):
        self.Artikelnummer: str
        self.Brutto: float
        self.Netto: float

    def Create(self, Artikelnummer: str, Brutto: float, Netto: float):
        self.Artikelnummer = Artikelnummer
        self.Brutto = Brutto
        self.Netto = Netto


class CustomAufschlag:
    def __init__(self):
        self.Kategorie: str
        self.Prozent: int

    def Create(self, Kategorie: str, Prozent: int):
        self.Kategorie = Kategorie
        self.Prozent = Prozent


class ManualCategories:
    def __init__(self):
        self.Name: str
        self.Children: list[str]

    def Create(self, Name: str, Children: list[str]):
        self.Name = Name
        self.Children = Children


class CategoryOverride:
    def __init__(self):
        self.Old: str
        self.New: str
        self.Index: int

    def Create(self, Old: str, New: str, Index: int):
        self.Old = Old
        self.New = New
        self.Index = Index


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
            tmp = CustomAufschlag()
            tmp.Create(x["Kategorie"], int(x["Prozent"]))
            self.CustomAufschlag.append(tmp)

        for x in data["ManualCategories"]:
            tmp = ManualCategories()
            tmp.Create(x["Name"], [])
            if len(x["children"]) > 0:
                for y in x["children"]:
                    tmp.Children.append(y)
            self.ManualCategories.append(tmp)

        for x in data["CategoryOverride"]:
            tmp = CategoryOverride()
            tmp.Create(x["old"], x["new"], int(x["index"]))
            self.CategoryOverride.append(tmp)

        self.Aufschlag = data["Aufschlag"]
        self.IgnoredCategories = data["IgnoredCategories"]
        self.IgnoredProducts = data["IgnoredProducts"]
        self.Uvp = []
        for x in data["UVP"]:
            tmp = Uvp()
            tmp.Create(x["Artikelnummer"], float(x["Brutto"]), float(x["Netto"]))
            self.Uvp.append(tmp)
