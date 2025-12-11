from scraper.browser import get_stealth_driver
from scraper.page_scraper import load_page, infinite_scroll
from scraper.data_parser import extract_cards, parse_card_data
from config.settings import TARGET_URL


def main():
    driver = get_stealth_driver()
    try:
        container = load_page(driver, TARGET_URL)
        infinite_scroll(driver)

        cards = extract_cards(container)
        print("Numero di cards:", len(cards))

        data = [parse_card_data(card) for card in cards]
        for d in data:
            print(d)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
