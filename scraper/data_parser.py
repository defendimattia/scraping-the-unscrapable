from selenium.webdriver.common.by import By


def extract_cards(container):
    """
    Riceve il container (raw Selenium element) e restituisce una lista
    di elementi/strutture con i dati.
    """
    cards = container.find_elements(
        By.XPATH, ".//div[contains(@class, 'x78zum5') and contains(@class, 'xdt5ytf')]"
    )
    return cards


def parse_card_data(card):
    """
    Funzione che estrae dati da una singola card.
    """
    pass
