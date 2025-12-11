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

        cards_elements = extract_cards(container)
        cards_data = [parse_card_data(card) for card in cards_elements]

        # Stampa test nel terminale
        print(
            f"""

            library_id: {cards_data[0]["library_id"]}
            start_date: {cards_data[0]["start_date"]}
            active_time: {cards_data[0]["active_time"]}
            platform: {cards_data[0]["platforms"]}
            description: {cards_data[0]["description"]}
            brand: {cards_data[0]["brand"]}
            product_name: {cards_data[0]["product_name"]}\n

            """
        )

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
