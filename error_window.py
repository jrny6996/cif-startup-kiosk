import sys
import traceback
from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton
from PyQt5.QtCore import QCoreApplication
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox

def run_with_error_popup(func, *args, **kwargs):
    val =True
    while True:
        try:
            if val == True:
                raise Exception("Something went wrong on purpose!")
            return func(*args, **kwargs)
        except Exception:
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

            ret = QMessageBox.critical(
                None,
                "Error running Kiosk",
                error_msg,
                buttons=QMessageBox.Retry | QMessageBox.Cancel,
                defaultButton=QMessageBox.Retry
            )
            val = False
            if ret == QMessageBox.Retry:
                continue  # retry the function
            else:
                if owns_app:
                    sys.exit(1)  # exit app if we created QApplication
                break
