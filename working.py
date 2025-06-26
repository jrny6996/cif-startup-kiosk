import os
import sys
import subprocess
import platform
from shutil import which

def find_browser_executable(browser_name):
    """
    Find the executable path for Chrome or Edge based on OS.
    """
    system = platform.system()

    if browser_name.lower() == 'chrome':
        if system == 'Windows':
            # Default install paths for Chrome
            possible_paths = [
                os.path.expandvars(r'%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe'),
                os.path.expandvars(r'%ProgramFiles%\Google\Chrome\Application\chrome.exe'),
                os.path.expandvars(r'%LocalAppData%\Google\Chrome\Application\chrome.exe')
            ]
        elif system == 'Darwin':
            # macOS
            possible_paths = [
                '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
            ]
        else:
            # Linux: rely on `which`
            path = which('google-chrome') or which('chrome') or which('chromium')
            if path:
                return path
            possible_paths = []

    elif browser_name.lower() == 'edge':
        if system == 'Windows':
            possible_paths = [
                os.path.expandvars(r'%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe'),
                os.path.expandvars(r'%ProgramFiles%\Microsoft\Edge\Application\msedge.exe'),
                os.path.expandvars(r'%LocalAppData%\Microsoft\Edge\Application\msedge.exe')
            ]
        elif system == 'Darwin':
            possible_paths = [
                '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge'
            ]
        else:
            # Linux
            path = which('microsoft-edge') or which('edge')
            if path:
                return path
            possible_paths = []
    else:
        raise ValueError('Unsupported browser name')

    for path in possible_paths:
        if os.path.isfile(path):
            return path

    return None

def open_tabs_kiosk(browser_name, urls):
    browser_path = find_browser_executable(browser_name)
    if not browser_path:
        print(f"Could not find {browser_name} executable.")
        return

    # Build command
    # Use --kiosk, open all URLs separated by spaces
    cmd = [browser_path, '--kiosk'] + urls

    try:
        subprocess.Popen(cmd)
        print(f"Opened {len(urls)} tabs in {browser_name} in kiosk mode.")
    except Exception as e:
        print(f"Failed to open browser: {e}")

if __name__ == '__main__':
 
    browser = sys.argv[1]
    urls = sys.argv[2:]

    open_tabs_kiosk(browser, urls)
