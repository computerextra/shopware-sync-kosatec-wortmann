$host.UI.RawUI.WindowTitle = "Shopimport"

while ($true) {
    Clear-Host
    python .\main.py main

    $timeout = 4 # Timeout in Stunden
    $timeout = $timeout * 60 * 60 # Timeout in Sekunden
    Timeout /T $timeout
}