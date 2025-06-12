import os
import sys
import platform
import webbrowser

def open_tabs(tabs:list=[''], browser=""):
    # err handling for non found browser
    try:
        if(browser != ""):
            kiosk = webbrowser.get(browser)

        elif(platform.system == "Windows"):
            kiosk = webbrowser.get("windows-default")
        elif (platform.system == "Darwin"):
            kiosk = webbrowser.get("macosx")
        else:
            kiosk = webbrowser.get("google-chrome")
    except:
        kiosk = webbrowser
    
    # open 1st link in new window
    kiosk.open_new(tabs[0] ) 
    if(len(tabs) < 1): return
    
    # openings 2-end tabs in same window
    tabs = tabs[1:] 
    for i, link, in enumerate(tabs):
        kiosk.open_new_tab(link)
    return


if __name__ == "__main__":
    tab_list = [
        "google.com",
        "mytech.newark.rutgers.edu",
    ]
    open_tabs(tab_list )