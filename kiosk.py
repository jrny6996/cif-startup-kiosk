from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time



def run_and_refresh_page(url:str, sleep_time:float=3)->None:
    options=""
    options = Options()
    options.add_argument("--start-fullscreen")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Edge(options=options)

    driver.get(url)
    driver.implicitly_wait(3)
    while True:
        time.sleep(sleep_time)
        driver.refresh()

    driver.quit()
if __name__ == "__main__":
    url= "https://rutgers.my.site.com/OneStopWalkIn/s/newarkwalkinstatus"
    run_and_refresh_page(url, sleep_time=60)