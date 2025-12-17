from scraper.browser import get_stealth_driver
from scraper.page_scraper import load_page, infinite_scroll, get_container
from scraper.data_parser import extract_cards, parse_card_data
from scraper.data_saver import save_to_csv
from config.settings import TARGET_URL


def main():
    driver = get_stealth_driver()

    try:
        load_page(driver, TARGET_URL)
        infinite_scroll(driver)

        container = get_container(driver)

        cards_elements = extract_cards(container)
        cards_data = [parse_card_data(card) for card in cards_elements]

        save_to_csv(
            data=cards_data[::2],
            output_path="data/data.csv",
            overwrite=True,
        )

        print("Done!")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
