import time
import random


def human_sleep(min_s=3, max_s=7):
    """Pausa casuale tra min_s e max_s secondi."""
    time.sleep(random.uniform(min_s, max_s))


def human_mouse_move(driver):
    """Simula movimento casuale del mouse."""
    x = random.randint(100, 1800)
    y = random.randint(100, 900)
    driver.execute_script(
        f"window.dispatchEvent(new MouseEvent('mousemove', {{clientX:{x}, clientY:{y}}}))"
    )


def human_scroll(driver):
    """Scroll casuale verticale."""
    step = random.randint(200, 500)
    driver.execute_script(f"window.scrollBy(0, {step});")
    time.sleep(random.uniform(0.5, 1.2))
