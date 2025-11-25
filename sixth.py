import sys
import requests
from bs4 import BeautifulSoup

def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []

    try:
        response = requests.get(url)
        response.raise_for_status()  # vyvola vyjimku pri chybnem HTTP kodu
    except requests.RequestException as e:
        print(f"Chyba pri stahovani stranky: {e}")
        return hrefs

    # parsujeme HTML obsah
    soup = BeautifulSoup(response.content, "html.parser")

    # projdeme vsechny <a> tagy a ulozime href
    for tag in soup.find_all("a"):
        href = tag.get("href")
        if href:
            hrefs.append(href)

    return hrefs



if __name__ == "__main__":
    try:
        # Pokusíme se načíst URL z argumentu příkazové řádky
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            # Pokud argument není, zeptáme se uživatele
            url = input("Zadejte URL stránky: ")

        links = download_url_and_get_all_hrefs(url)
        for link in links:
            print(link)

    except Exception as e:
        print(f"Program skoncil chybou: {e}")

