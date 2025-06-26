from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time
from pynput import mouse, keyboard

# === Config ===
INACTIVITY_THRESHOLD = 5  # seconds
CHECK_INTERVAL = 5
URL = "https://rutgers.my.site.com/OneStopWalkIn/s/newarkwalkinstatus"

# Track last activity time globally
last_active_time = time.time()

def on_input(_):
    global last_active_time
    last_active_time = time.time()

def start_input_listeners():
    mouse.Listener(on_move=on_input, on_click=on_input, on_scroll=on_input).start()
    keyboard.Listener(on_press=on_input).start()

def is_user_inactive():
    return time.time() - last_active_time > INACTIVITY_THRESHOLD

def prompt_user(driver):
    driver.execute_script("window._userConfirmed = confirm('Are you still there?');")
    time.sleep(1)

    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"[?] Alert: {alert_text}")

        alert.accept()  # User clicked OK
        return True
    except NoAlertPresentException:
        return False
    except Exception as e:
        print(f"[!] Error handling alert: {e}")
        return False

def run_and_refresh_page(url: str, sleep_time: float = 60) -> None:
    options = Options()
    options.add_argument("--start-fullscreen")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Edge(options=options)
    driver.get(url)
    driver.implicitly_wait(3)

    start_input_listeners()

    while True:
        time.sleep(CHECK_INTERVAL)

        if is_user_inactive():
            print("[*] System inactive. Prompting user...")
            if prompt_user(driver):
                print("[+] User confirmed. Refreshing page...")
                driver.get(url)
                global last_active_time
                last_active_time = time.time()
            else:
                print("[-] No confirmation. Skipping refresh.")
        else:
            print("[*] User active. Refreshing normally after sleep...")
            time.sleep(sleep_time - CHECK_INTERVAL)
            driver.get(url)

    driver.quit()

if __name__ == "__main__":
    run_and_refresh_page(URL, sleep_time=10)  # sleep_time short for testing
