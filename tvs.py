import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import platform
from error_window import run_with_error_popup

def run_and_refresh_page(url: str, sleep_time: float = 3) -> None:
    options = Options()
    options.add_argument("--start-fullscreen")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    """
    Microsoft seems to have moved or protected the url for edge driver, using hard coded path 
    """
    # service = Service(EdgeChromiumDriverManager().install())
    # service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service, options=options)
       
    operating_sys = platform.system()
    if operating_sys == "Linux":
        service = Service("./drivers/edgedriver_linux64/msedgedriver")
    elif operating_sys == "Windows":
        service = Service("./drivers/edgedriver_win32/msedgedriver.exe")

    else:
        print("Could not detect platform to run edge Kiosk. Please verify system is on Linux or Windows")
        return
    driver = webdriver.Edge(service=service, options=options)
  
    run_with_error_popup(lambda: (
    driver.get(url),
    driver.implicitly_wait(3),
    print("Running browser"),
    [driver.refresh() or time.sleep(sleep_time) for _ in iter(int, 1)]
))
        


    driver.quit()

    

if __name__ == "__main__":
    url = "https://rutgers.my.site.com/OneStopWalkIn/s/newarkwalkinstatus"
    run_and_refresh_page(url, sleep_time=60)
