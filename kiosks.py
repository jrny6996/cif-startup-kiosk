import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from pynput import mouse, keyboard

# === Config ===
INACTIVITY_THRESHOLD = 30  # seconds
CHECK_INTERVAL = 5
URL = "https://rutgers.my.site.com/OneStopWalkIn/s/newark"

# Track last activity time globally
last_active_time = time.time()
has_user_interacted = False  

def on_input(_):
    global last_active_time, has_user_interacted
    last_active_time = time.time()
    has_user_interacted = True 

def start_input_listeners():
    mouse.Listener(on_move=on_input, on_click=on_input, on_scroll=on_input).start()
    keyboard.Listener(on_press=on_input).start()

def is_user_inactive():
    return time.time() - last_active_time > INACTIVITY_THRESHOLD

def prompt_user(driver):
    driver.execute_script("window._userConfirmed = confirm('Are you still there? Please select \"cancel\" to continue');")
    time.sleep(10)

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

def run_and_refresh_page(url: str, sleep_time: float = 10, kiosk_flag:str= "--start-fullscreen") -> None:
    options = Options()
    options.add_argument(kiosk_flag)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.get(url)
   

    driver.implicitly_wait(3)

    start_input_listeners()

    while True:
        global has_user_interacted
        time.sleep(CHECK_INTERVAL)
        # ✅ Skip nested loop if no user interaction yet
        if not has_user_interacted:
            print("[*] Waiting for initial user interaction...")
            continue

        if is_user_inactive():
            print("[*] System inactive. Prompting user...")
            if prompt_user(driver):
                print("[+] User confirmed. Refreshing page...")
                driver.delete_all_cookies()
                driver.get(url)
                has_user_interacted = False
                global last_active_time
                last_active_time = time.time()

            else:
                print("[-] No confirmation. Skipping refresh.")

        else:
            print("[*] User active. No refresh needed.")

    driver.quit()

if __name__ == "__main__":
    run_and_refresh_page(URL, kiosk_flag="--kiosk" )
