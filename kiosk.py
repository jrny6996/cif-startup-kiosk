from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# returns options to be passed into webdriver.Edge()
def get_default_edge_options():
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    return options

def run_and_refresh_page(url:str, sleep_time:float=3)->None:
    options = get_default_edge_options()
    driver = webdriver.Edge(options=options)

    driver.get(url)

    while True:
        time.sleep(sleep_time)
        driver.refresh()

    driver.quit()
if __name__ == "__main__":
    url= "https://google.com"
    run_and_refresh_page(url)