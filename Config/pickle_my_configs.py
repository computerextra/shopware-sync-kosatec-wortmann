import pickle
from Config.Types import *
from Config.Types import Config
import json
import codecs


def write_config_file():
    config = Config()
    config.Aufschlag = 20
    config.CustomAufschlag = []
    c = C_CustomAufschlag()
    c.Kategorie = "DVI"
    c.Prozent = 500
    config.CustomAufschlag.append(c)
    c.Kategorie = "HDMI"
    c.Prozent = 500
    config.CustomAufschlag.append(c)
    c.Kategorie = "Displayport"
    c.Prozent = 500
    config.CustomAufschlag.append(c)
    c.Kategorie = "VGA"
    c.Prozent = 500
    config.CustomAufschlag.append(c)
    c.Kategorie = "USB 2.0"
    c.Prozent = 500
    config.CustomAufschlag.append(c)
    c.Kategorie = "Sonstige Kabel"
    c.Prozent = 500
    config.CustomAufschlag.append(c)
    c.Kategorie = "Netzanschlusskabel"
    c.Prozent = 500
    config.CustomAufschlag.append(c)
    c.Kategorie = "Cat-Kabel"
    c.Prozent = 500
    config.CustomAufschlag.append(c)
    c.Kategorie = "Sonstige Netzwerk-Kabel"
    c.Prozent = 500
    config.CustomAufschlag.append(c)
    c.Kategorie = "Audio"
    c.Prozent = 500
    config.CustomAufschlag.append(c)
    c.Kategorie = "USB 3.0"
    c.Prozent = 500
    config.CustomAufschlag.append(c)
    c.Kategorie = "USB C"
    c.Prozent = 500
    config.CustomAufschlag.append(c)
    c.Kategorie = "HDD-/ SSD-Kabel"
    c.Prozent = 500
    config.CustomAufschlag.append(c)

    config.IgnoredCategories = [
        "Server Barebone" "Server" "CSP Cloud" "ESD-Lizenzen" "Tinte / Toner kompatibel"
    ]
    config.IgnoredProducts = []

    config.ManualCategories = []
    d = C_ManualCategories()
    d.name = "Apple"
    d.children = []
    config.ManualCategories.append(d)

    d.name = "Komponenten"
    d.children = []
    e = C_CategoryName()
    e.name = "Arbeitsspeicher"
    d.children.append(e)
    e.name = "CPUs"
    d.children.append(e)
    e.name = "Gehäuse"
    d.children.append(e)
    e.name = "Grafikkarten"
    d.children.append(e)
    e.name = "Festplatten"
    d.children.append(e)
    e.name = "Laufwerke"
    d.children.append(e)
    e.name = "Mainboards & Zubehör"
    d.children.append(e)
    e.name = "Netzteile"
    d.children.append(e)
    e.name = "SSDs"
    d.children.append(e)
    e.name = "Multimedia"
    config.ManualCategories.append(d)

    d.name = "PC-Systeme"
    d.children = []
    e.name = "Marken PCs"
    d.children.append(e)
    e.name = "Mini-PC / Barebones"
    d.children.append(e)
    e.name = "All in one Systeme"
    d.children.append(e)
    e.name = "Innovation PC Systeme"
    d.children.append(e)
    e.name = "PC Zubehör"
    d.children.append(e)
    e.name = "Multimedia"
    d.children.append(e)
    config.ManualCategories.append(d)

    d.name = "Displays"
    d.children = []
    config.ManualCategories.append(d)

    d.name = "Home & Living"
    d.children = []
    config.ManualCategories.append(d)

    d.name = "Hardware"
    d.children = []
    e.name = "Beamer"
    d.children.append(e)
    e.name = "Drucker & Scanner"
    d.children.append(e)
    e.name = "Flash-Speicher"
    d.children.append(e)
    e.name = "Eingabegeräte"
    d.children.append(e)
    e.name = "Energie & USV"
    d.children.append(e)
    e.name = "Kabel & Adapter"
    d.children.append(e)
    e.name = "Verbrauchsmaterialien"
    d.children.append(e)
    config.ManualCategories.append(d)

    d.name = "Mobile"
    d.children = []
    e.name = "Notebooks & Zubehör"
    d.children.append(e)
    e.name = "Tablets & Smartphones"
    d.children.append(e)
    config.ManualCategories.append(d)

    d.name = "Networking"
    d.children = []
    e.name = "Festnetz-Telefonie"
    d.children.append(e)
    e.name = "Firewall"
    d.children.append(e)
    config.ManualCategories.append(d)

    d.name = "Software"
    d.children = []
    config.ManualCategories.append(d)

    d.name = "Used IT"
    d.children = []
    config.ManualCategories.append(d)

    d.name = "Warehouse Deals"
    d.children = []
    config.ManualCategories.append(d)

    config.CategoryOverride = []
    o = C_CategoryOverride()
    o.index = 1
    o.old = "Netzwerk"
    o.new = "Networking"
    config.CategoryOverride.append(o)

    config.Uvp = []
    u = C_Uvp()
    u.Artikelnummer = "K122998"
    u.Brutto = 259.9
    u.Netto = 218.4
    config.Uvp.append(u)

    u.Artikelnummer = "K123005"
    config.Uvp.append(u)

    u.Artikelnummer = "K122996"
    config.Uvp.append(u)

    u.Artikelnummer = "K122997"
    config.Uvp.append(u)

    u.Artikelnummer = "K122995"
    u.Brutto = 144.9
    u.Netto = 121.76
    config.Uvp.append(u)
    u.Artikelnummer = "K122993"
    config.Uvp.append(u)
    u.Artikelnummer = "K122994"
    config.Uvp.append(u)
    u.Artikelnummer = "K122991"
    config.Uvp.append(u)

    u.Artikelnummer = "K123403"
    u.Brutto = 219.9
    u.Netto = 184.03
    config.Uvp.append(u)

    u.Artikelnummer = "K126228"
    u.Brutto = 289.0
    u.Netto = 242.86
    config.Uvp.append(u)

    u.Artikelnummer = "K730173"
    u.Brutto = 79.0
    u.Netto = 66.39
    config.Uvp.append(u)

    u.Artikelnummer = "K121607"
    u.Brutto = 89.0
    u.Netto = 74.79
    config.Uvp.append(u)

    u.Artikelnummer = "K110595"
    u.Brutto = 89.0
    u.Netto = 74.79
    config.Uvp.append(u)

    u.Artikelnummer = "K775435"
    u.Brutto = 59.0
    u.Netto = 49.58
    config.Uvp.append(u)

    u.Artikelnummer = "K698122"
    u.Brutto = 109.0
    u.Netto = 91.6
    config.Uvp.append(u)

    u.Artikelnummer = "K124667"
    u.Brutto = 269.0
    u.Netto = 226.05
    config.Uvp.append(u)

    u.Artikelnummer = "K116596"
    u.Brutto = 269.0
    u.Netto = 226.05
    config.Uvp.append(u)

    u.Artikelnummer = "K124636"
    u.Brutto = 329.0
    u.Netto = 276.47
    config.Uvp.append(u)

    u.Artikelnummer = "K115086"
    u.Brutto = 159.0
    u.Netto = 133.61
    config.Uvp.append(u)

    u.Artikelnummer = "K126656"
    u.Brutto = 219.0
    u.Netto = 184.03
    config.Uvp.append(u)

    u.Artikelnummer = "K103907"
    u.Brutto = 439.0
    u.Netto = 368.91
    config.Uvp.append(u)

    u.Artikelnummer = "K124377"
    u.Brutto = 119.0
    u.Netto = 100.0
    config.Uvp.append(u)

    u.Artikelnummer = "K122629"
    u.Brutto = 199.0
    u.Netto = 167.23
    config.Uvp.append(u)

    u.Artikelnummer = "K125616"
    u.Brutto = 319.0
    u.Netto = 268.07
    config.Uvp.append(u)

    u.Artikelnummer = "K132256"
    u.Brutto = 99.0
    u.Netto = 83.19
    config.Uvp.append(u)

    u.Artikelnummer = "K124378"
    u.Brutto = 95.0
    u.Netto = 79.83
    config.Uvp.append(u)

    u.Artikelnummer = "K111847"
    u.Brutto = 109.0
    u.Netto = 91.6
    config.Uvp.append(u)

    u.Artikelnummer = "K128024"
    u.Brutto = 189.0
    u.Netto = 158.82
    config.Uvp.append(u)

    u.Artikelnummer = "K110217"
    u.Brutto = 39.0
    u.Netto = 32.77
    config.Uvp.append(u)

    u.Artikelnummer = "K391769"
    u.Brutto = 39.0
    u.Netto = 32.77
    config.Uvp.append(u)

    u.Artikelnummer = "K721081"
    u.Brutto = 49.0
    u.Netto = 41.18
    config.Uvp.append(u)

    u.Artikelnummer = "K130858"
    u.Brutto = 89.0
    u.Netto = 74.79
    config.Uvp.append(u)

    u.Artikelnummer = "K102455"
    u.Brutto = 59.0
    u.Netto = 49.58
    config.Uvp.append(u)

    u.Artikelnummer = "K127148"
    u.Brutto = 69.0
    u.Netto = 57.98
    config.Uvp.append(u)

    u.Artikelnummer = "K730174"
    u.Brutto = 49.0
    u.Netto = 41.18
    config.Uvp.append(u)

    u.Artikelnummer = "K154036"
    u.Brutto = 59.0
    u.Netto = 49.58
    config.Uvp.append(u)

    u.Artikelnummer = "K126671"
    u.Brutto = 65.0
    u.Netto = 54.62
    config.Uvp.append(u)

    u.Artikelnummer = "K108301"
    u.Brutto = 89.0
    u.Netto = 74.79
    config.Uvp.append(u)

    u.Artikelnummer = "K172240"
    u.Brutto = 139.0
    u.Netto = 116.81
    config.Uvp.append(u)

    u.Artikelnummer = "K133573"
    u.Brutto = 169.0
    u.Netto = 142.02
    config.Uvp.append(u)

    u.Artikelnummer = "K165628"
    u.Brutto = 149.0
    u.Netto = 125.21
    config.Uvp.append(u)

    u.Artikelnummer = "K103264"
    u.Brutto = 179.0
    u.Netto = 150.42
    config.Uvp.append(u)

    u.Artikelnummer = "K564200"
    u.Brutto = 59.0
    u.Netto = 49.58
    config.Uvp.append(u)

    u.Artikelnummer = "K503329"
    u.Brutto = 99.0
    u.Netto = 83.19
    config.Uvp.append(u)

    u.Artikelnummer = "K134504"
    u.Brutto = 39.0
    u.Netto = 32.77
    config.Uvp.append(u)

    with open("config.pkl", "wb") as f:
        pickle.dump(config, f)
        f.close()


# def get_config() -> Config:
#     with open("config.pkl", "rb") as f:
#         data: Config = pickle.load(f)
#     return data


def get_config() -> Config:
    with codecs.open("config.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    config = Config()
    config.CustomAufschlag = []
    config.ManualCategories = []
    config.CategoryOverride = []
    for x in data["CustomAufschlag"]:
        tmpCA = C_CustomAufschlag()
        tmpCA.Kategorie = x["Kategorie"]
        tmpCA.Prozent = int(x["Prozent"])
        config.CustomAufschlag.append(tmpCA)
    for x in data["ManualCategories"]:
        tmpMA: C_ManualCategories = C_ManualCategories()
        tmpMA.name = x["name"]
        tmpMA.children = []
        if len(x["children"]) > 0:
            for y in x["children"]:
                z: C_CategoryName = C_CategoryName()
                z.name = y["name"]
                tmpMA.children.append(z)
        config.ManualCategories.append(tmpMA)

    for x in data["CategoryOverride"]:
        tmp2: C_CategoryOverride = C_CategoryOverride()
        tmp2.old = x["old"]
        tmp2.new = x["new"]
        tmp2.index = int(x["index"])
        config.CategoryOverride.append(tmp2)

    config.Aufschlag = data["Aufschlag"]
    config.IgnoredCategories = data["IgnoredCategories"]
    config.IgnoredProducts = data["IgnoredProducts"]
    config.Uvp = []
    for x in data["UVP"]:
        tmp: C_Uvp = C_Uvp()
        tmp.Artikelnummer = x["Artikelnummer"]
        tmp.Brutto = float(x["Brutto"])
        tmp.Netto = float(x["Netto"])
        config.Uvp.append(tmp)

    return config
