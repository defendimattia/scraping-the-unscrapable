from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import USER_AGENT


def get_stealth_driver():
    chrome_options = Options()

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument(f"--user-agent={USER_AGENT}")

    driver = webdriver.Chrome(options=chrome_options)

    # --- PATCH STEALTH ---
    patches = [
        "Object.defineProperty(navigator, 'webdriver', { get: () => undefined });",
        "Object.defineProperty(navigator, 'plugins', { get: () => [1,2,3,4] }); "
        "Object.defineProperty(navigator, 'languages', { get: () => ['it-IT','it'] });",
        "for (const key in window) { if (key.startsWith('cdc_')) delete window[key]; }",
        "Object.defineProperty(window.navigator, 'chrome', { value: { runtime: {} } });",
        "Object.defineProperty(window.screen, 'width', { value: 1920 }); "
        "Object.defineProperty(window.screen, 'height', { value: 1080 }); "
        "Object.defineProperty(window.screen, 'availWidth', { value: 1920 }); "
        "Object.defineProperty(window.screen, 'availHeight', { value: 1080 });",
    ]

    for code in patches:
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument", {"source": code}
        )

    driver.execute_cdp_cmd(
        "Network.setExtraHTTPHeaders",
        {"headers": {"Accept-Language": "it-IT,it;q=0.9"}},
    )

    return driver
