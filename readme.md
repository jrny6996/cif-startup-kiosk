# Scripts for running browsers


## Building

### Must be built on same os as target system

1. Build python Virtual Envirnment(optional) `python -m venv env` & activate it `.\env\Scripts\activate`
2. Install dependancies `pip install -r requirements.txt`
3. Run `python kiosks.py` to run the appicaltion
4. Build an executable file using pyinstaller `pyinstaller kiosks.py --name windows-kiosk.exe` which will output the .exe file in `\dist\windows-kiosk.exe\windows-kiosk`

## Kiosks @ Conklin

These should run the kiosks.py script which is the one setup in `.\dist\windows-kiosk.exe` by default. I believe you'll need to drag the entire windows-kiosk.exe folder as it include some important files in `_internal` & it shouldn't require a python interpretter on the final system, but this needs to be tested
