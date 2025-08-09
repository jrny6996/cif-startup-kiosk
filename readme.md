# Scripts for running browsers

Requires Python interpreter on system. While a standalone exe is possible, it generally makes it less robust, see [PyInstaller's documentation ](https://pyinstaller.org/en/stable/common-issues-and-pitfalls.html#launching-external-programs-from-the-frozen-application)

## Installing dependencies
Make sure you're inside the directory containing `kiosks.py` & other python files when running the following cmd 
`pip install -r requirements.txt`

## Usage

[🎬 Watch the demo](./Conklinusage.webm)
Kiosks @ Conklin should use the `kiosks.py` file & tvs should use `tvs.py`

There is also a `kiosks.pyw` which is the same as `.py`, except it hides the terminal & runs Chrome in "Kiosk" mode instead of fullscreen.

### For testing
On Windows, the Python interpreter can be used via `python kiosks.py` while inside the folder. 
Also assuming Python was installed the standard way on Windows, you should be able to just double click the file


### On startup
The script can be added to the startup folder & should run automatically on next restart
To find the startup folder, type `shell:startup` in the File Explorer address bar. From there all that is required is to drag the `kiosks.pyw` file into the folder 

Consider also adding a copy on the desktop, should Chrome crash or a user closes the window. Someone can reopen it
