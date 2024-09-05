import time

from Api.Categories import SyncCategories
from Api.Manufacturer import SyncManufacturer
from Api.Products import CreateProducts, DeleteProducts, GetShopProducts, UpdateProducts
from Files.Csv import Parse_Csv_Files
from Files.Download import Download
from Sorting import SortAllProducts, SortShopProducts
from Files.Images import Upload_Images

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
    print("Download all Shop Products")
    start = time.time()
    ShopProducts = GetShopProducts()
    end = time.time()
    print(f"Download Finished in {round((end - start), 2)}s")

    print("Sort Shop Products.")
    start = time.time()
    KosatecShop, WortmannShop = SortShopProducts(ShopProducts)
    end = time.time()
    print(f"Sorting Finished in {round((end - start), 2)}s")

    print("Download Files")
    start = time.time()
    Download()
    end = time.time()
    print(f"Download Finished in {round((end - start), 2)}s")

    print("Upload Images")
    start = time.time()
    Upload_Images()
    end = time.time()
    print(f"Upload Finished in {round((end - start), 2)}s")

    print("Parse CSV Files")
    start = time.time()
    CsvProducts = Parse_Csv_Files(WORTMANN_KATEGORIEN_IGNORE)
    end = time.time()
    print(f"Parsing Finished in {round((end - start), 2)}s")

    print("Sort Products")
    start = time.time()
    newKosatec, oldKosatec, deleteKosatec, newWortmann, oldWortmann, deleteWortmann = (
        SortAllProducts(KosatecShop, WortmannShop, CsvProducts.Artikel)
    )
    end = time.time()
    print(f"Sorting Finished in {round((end - start), 2)}s")
    print(
        f"Kosatec: \nNew: {len(newKosatec)}\nOld: {len(oldKosatec)}\nDelete: {len(deleteKosatec)}\n\nWortmann:\nNew: {len(newWortmann)}\nOld: {len(oldWortmann)}\nDelete: {len(deleteWortmann)}"
    )

    print("Sync with Shopware")
    print("Sync Manufacturers")
    startSync = time.time()
    SyncManufacturer(CsvProducts.Hersteller)
    end = time.time()
    print(f"Manufacturers Sync Finished in {round((end - startSync), 2)}s")

    print("Sync Categories")
    start = time.time()
    SyncCategories(CsvProducts.Artikel)
    end = time.time()
    print(f"Categories Sync Finished in {round((end - start), 2)}s")

    print("Sync Products")
    start = time.time()
    UpdateProducts(oldKosatec, oldWortmann)
    CreateProducts(newKosatec, newWortmann)
    DeleteProducts(deleteKosatec, deleteWortmann)
    end = time.time()
    print(f"Products Sync Finished in {round((end - start), 2)}s")
    print(f"Full Sync Finished in {round((end - startSync), 2)}s")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()

    print(f"\n\nRuntime: {round((end - start), 2)}s")
    print(f"Runtime: {round(((end - start)/60), 2)}min")
    print(f"Runtime: {round(((end - start)/60/60), 2)}h")
