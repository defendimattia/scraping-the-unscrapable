from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from scraper.human_actions import human_sleep, human_mouse_move, human_scroll
from config.settings import TIMEOUT, SCROLL_TIMEOUT


def load_page(driver, url):
    """Carica la pagina e attende che il container principale sia presente."""
    driver.get(url)
    human_sleep()
    human_mouse_move(driver)

    # Aspetta che il container esista nel DOM (ma non lo restituisce)
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[@class='x1dr75xp xh8yej3 xkopdvs']",
            )
        )
    )


def infinite_scroll(driver):
    """Scroll infinito simulando comportamento umano."""
    start_time = time.time()
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        for _ in range(8):
            human_scroll(driver)

        human_sleep()
        human_mouse_move(driver)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height and (time.time() - start_time) > SCROLL_TIMEOUT:
            break

        last_height = new_height


def get_container(driver):
    """Recupera il container aggiornato dopo lo scroll."""
    container = driver.find_element(
        By.XPATH, "//div[@class='x1dr75xp xh8yej3 xkopdvs']"
    )
    return container
