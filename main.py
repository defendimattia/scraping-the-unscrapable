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

        cards_elements = extract_cards(container)
        cards_data = [parse_card_data(card) for card in cards_elements]

        # Stampa test nel terminale

        for card in cards_data[::2]:
            print(
                f"""

                library_id: {card["library_id"]}
                start_date: {card["start_date"]}
                active_time: {card["active_time"]}
                platform: {card["platforms"]}
                description: {card["description"]}
                brand: {card["brand"]}
                product_name: {card["product_name"]}
                img: {card["img"]}
                link: {card["link"]}

                """
            )

        print("Numero di cards:", int(len(cards) / 2))

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
