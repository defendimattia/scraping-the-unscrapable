from selenium.webdriver.common.by import By


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
    """
    pass
