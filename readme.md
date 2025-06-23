# Scripts for running browsers

Included file in `\dist\ez-run.exe\ez-run`

## Building

1. Build python Virtual Envirnment(optional) `python -m venv env` & activate it `.\env\Scripts\activate`
2. Install dependancies `pip install -r requirements.txt`
3. Run `python kiosk.py` to run the appicaltion
4. Build an executable file using pyinstaller `pyinstaller kiosk.py --name ez-run.exe` which will output the .exe file in `\dist\ez-run.exe\ez-run`

## Kiosks @ Conklin

These should run the kiosk.py script which is the one setup in `.\dist\ez-run.exe` by default. If your I believe you'll need to drag the entire ez-run.exe folder as it include some important files in `_internal`
