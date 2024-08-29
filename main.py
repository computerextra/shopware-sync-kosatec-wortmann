import time

from Files.Csv import Parse_Csv_Files
from Files.Download import Download_Kosatec, Download_Wortmann
from Files.Images import Upload_Images
from env import Env

WORTMANN_KATEGORIEN_IGNORE: list[str] = [
    "CLOUD_BACKUP",
    "Werbegeschenke",
    "Eingabe Adapter",
    "Optische- und Bandlaufwerke",
    "Netzteile & USVs",
    "AV-Zubehör",
    "Netzwerkzubehör",
    "CLOUD_IAAS",
    "Netzteil / Akku",
    "Systemzubehör",
    "Speicheradapter",
    "Verkaufsförderung",
    "Kartenleser",
    "System- & Stromkabel",
    "Mäuse",
    "Tastaturen",
    "Ersatzteile",
    "LCD Messeware",
    "Ausgabe Zubehör",
    "Bridges & Router",
    "Modems",
    "SERVER",
    "Schulungen",
    "CLOUD_SAAS",
    "Monitore",
    "TERRA CLOUD",
]


def main():
    env = Env()
    print("Download Files")
    start = time.time()
    Download_Kosatec(env.GetKosatecUrl())
    login = env.GetWortmannLogin()
    Download_Wortmann(login.Server, login.User, login.Pass)
    end = time.time()
    print(f"Download Finished in {round((end - start), 2)}s")
    print("Upload Images")
    start = time.time()
    Upload_Images(login.Server, login.User, login.Pass, env.GetFTPPath())
    end = time.time()
    print(f"Upload Finished in {round((end - start), 2)}s")
    print("Parse CSV Files")
    start = time.time()
    ListenArtikel = Parse_Csv_Files(WORTMANN_KATEGORIEN_IGNORE)
    end = time.time()
    print(f"Parsing Finished in {round((end - start), 2)}s")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()

    print(f"Runtime: {round((end - start), 2)}s")
    print(f"Runtime: {round(((end - start)/60), 2)}min")
    print(f"Runtime: {round(((end - start)/60/60), 2)}h")
