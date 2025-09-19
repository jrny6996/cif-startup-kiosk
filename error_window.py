import sys
import traceback
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QCoreApplication

def run_with_error_popup(func, *args, **kwargs):
    try:
        # raise Exception("Something went wrong on purpose!")

        return func(*args, **kwargs)
    except Exception:
        # error_msg = traceback.format_exc()
        
        error_msg = """
        Seems there was an error when starting application.
        Please confirm device has internet and site is available.
        If still running into issues, contact 833-OIT-HELP
"""
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
            owns_app = True
        else:
            owns_app = False

        QMessageBox.critical(None, "Error running Kiosk", error_msg)

        if owns_app:
            QCoreApplication.exit()