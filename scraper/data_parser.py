from selenium.webdriver.common.by import By

platform_map = {
    "-2234px": "Facebook",
    "-867px": "Instagram",
    "-880px": "Audience Network",
    "-270px": "Messenger",
    "-744px": "Threads",
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
        if "·" in date_info_text:
            start_date_text, active_time = [
                x.strip() for x in date_info_text.split("·")
            ]
        else:
            start_date_text, active_time = date_info_text, None

        # Estrarre solo la data dopo i due punti
        if ":" in start_date_text:
            start_date = start_date_text.split(": ")[1].strip()
        else:
            start_date = start_date_text.strip()

    except:
        start_date, active_time = None, None

    # Piattaforme tramite XPath usando gli ID
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
            By.XPATH, "//div[contains(@style, 'white-space: pre-wrap')]/span"
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

    # Dizionario finale
    return {
        "library_id": library_id,
        "start_date": start_date,
        "active_time": active_time,
        "platforms": set(platforms),
        "description": description,
        "brand": brand,
        "product_name": product_name,
    }
