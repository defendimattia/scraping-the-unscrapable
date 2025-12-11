from scraper.browser import get_stealth_driver
from scraper.page_scraper import load_page, infinite_scroll, get_container
from scraper.data_parser import extract_cards, parse_card_data
from config.settings import TARGET_URL


def main():
    driver = get_stealth_driver()

    try:
        load_page(driver, TARGET_URL)
        infinite_scroll(driver)

        container = get_container(driver)

        cards = extract_cards(container)
        print("Numero di cards:", len(cards))

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
