from selenium.webdriver.common.by import By
import re

platform_map = {
    "-2234px": "Facebook",
    "-867px": "Instagram",
    "-880px": "Audience Network",
    "-270px": "Messenger",
    "-744px": "Threads",
    "-75px -309px": "Instagram",
    "-75px -668px": "Facebook",
    "-75px -296px": "Audience Network",
    "-32px -1333px": "Messenger",
    "-58px -1333px": "Threads",
}


def extract_cards(container):
    """
    Riceve il container (raw Selenium element) e restituisce una lista
    di elementi/strutture con i dati.
    """
    cards = container.find_elements(By.XPATH, ".//div[@class='xh8yej3']")
    return cards


def parse_card_data(card):
    """
    Funzione che estrae dati da una singola card.
    Restituisce un dizionario con i dati.
    """
    # ID libreria
    try:
        library_id_text = card.find_element(
            By.XPATH, ".//span[contains(text(), 'ID libreria')]"
        ).text
        library_id = library_id_text.split(":")[-1].strip()
    except:
        library_id = None

    # Data di inizio pubblicazione e tempo attiva
    try:
        date_info_text = card.find_element(
            By.XPATH, ".//span[contains(text(), 'Data di inizio')]"
        ).text

        # Estrarre solo la data (tutto dopo i due punti fino al punto centrale o fine stringa)
        date_match = re.search(r"Data di inizio.*?:\s*([^\u00b7]+)", date_info_text)
        start_date = date_match.group(1).strip() if date_match else None

        # Estrarre solo le ore di attività (numero intero prima di 'h')
        hours_match = re.search(r"(\d+)\s*h", date_info_text)
        active_time = hours_match.group(1) if hours_match else None

    except:
        start_date, active_time = None, None

    # Piattaforme
    platforms = []
    try:
        icon_divs = card.find_elements(
            By.XPATH, ".//div[contains(@style,'mask-image')]"
        )
        for div in icon_divs:
            style = div.get_attribute("style")
            for pos, name in platform_map.items():
                if pos in style:
                    platforms.append(name)
    except:
        pass

    # Descrizione
    try:
        description = card.find_element(
            By.XPATH, ".//div[contains(@style, 'white-space: pre-wrap')]/span"
        ).text
    except:
        description = None

    # Brand
    try:
        brand = card.find_element(By.XPATH, ".//a[@target='_blank']").text
    except:
        brand = None

    # Nome prodotto
    try:
        product_name = card.find_element(
            By.XPATH,
            ".//div[@role='button']/div[contains(@style,'line-height: 14px')]",
        ).text
    except:
        product_name = None

    # Immagine
    try:
        img = card.find_element(
            By.XPATH,
            ".//a[contains(@href,'doubleclick') or contains(@href,'facebook.com')]//img[contains(@src,'fbcdn.net')]",
        ).get_attribute("src")
    except:
        img = None

    # Link
    try:
        link = card.find_element(
            By.XPATH,
            ".//a[@target='_blank' and (contains(@href,'l.facebook.com/l.php') or contains(@href,'doubleclick'))]",
        ).get_attribute("href")
    except:
        link = None

    # Dizionario finale
    return {
        "library_id": library_id,
        "start_date": start_date,
        "active_time": active_time,
        "platforms": set(platforms),
        "description": description,
        "brand": brand,
        "product_name": product_name,
        "img": img,
        "link": link,
    }
