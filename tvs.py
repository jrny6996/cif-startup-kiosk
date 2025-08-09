import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager

def run_and_refresh_page(url: str, sleep_time: float = 3) -> None:
    options = Options()
    options.add_argument("--start-fullscreen")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    """
    Microsoft seems to have moved the url for edge driver, using chrome
    """
    # service = Service(EdgeChromiumDriverManager().install())
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    driver.implicitly_wait(3)

    while True:
        time.sleep(sleep_time)
        driver.refresh()

    driver.quit()


if __name__ == "__main__":
    url = "https://rutgers.my.site.com/OneStopWalkIn/s/newarkwalkinstatus"
    run_and_refresh_page(url, sleep_time=60)
