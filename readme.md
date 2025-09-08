# Scripts for running browsers

Script is currently compatible on Windows & Linux machines. It will require a compatible version of Edge installed.
As of 08/14/25, the latest should work & it's installer has been placed inside `./browser_installers`

Requires Python interpreter on system. While a standalone exe is possible, it generally makes it less robust, see [PyInstaller's documentation ](https://pyinstaller.org/en/stable/common-issues-and-pitfalls.html#launching-external-programs-from-the-frozen-application)

However you may want a standalone file you can install `pip install pyinstaller` & run `pyinstaller filename.py --onefile` to build exe. Just remember it's searching for Edge Driver in relative path. So it should be in the same directory as the other `.py` files to find it. For placing on desktop, create shortcuts to this exe and style as fit. Really only necessary if your python installation is different than mine(e.g admin priv, longer path, installed through Python's official site)

## Installing dependencies
Make sure you're inside the directory containing `kiosks.py` & other python files when running the following cmd 
`pip install -r requirements.txt`

## Usage

[🎬 Watch the demo](https://jrny6996.github.io/cif-startup-kiosk/)
Kiosks @ Conklin should use the `kiosks.py` file & tvs should use `tvs.py`

There is also a `kiosks.pyw` which is the same as `.py`, except it hides the terminal & runs Chrome in "Kiosk" mode instead of fullscreen.

### For testing
On Windows, the Python interpreter can be used via `python kiosks.py` while inside the folder. 
Also assuming Python was installed the standard way on Windows, you should be able to just double click the file


### On startup
The script can be added to the startup folder & should run automatically on next restart
To find the startup folder, type `shell:startup` in the File Explorer address bar. From there all that is required is to drag the `kiosks.pyw` file into the folder 

Consider also adding a copy on the desktop, should Chrome crash or a user closes the window. Someone can reopen it
