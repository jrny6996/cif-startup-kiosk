# Scripts for running browsers

Included file in `\dist\ez-run.exe\ez-run`

## Building

1. Build python Virtual Envirnment(optional) `python -m venv env` & activate it `.\env\Scripts\activate`
2. Install dependancies `pip install -r requirements.txt`
3. Run `python kiosks.py` to run the appicaltion
4. Build an executable file using pyinstaller `pyinstaller kiosks.py --name ez-run` which will output the .exe file in `\dist\ez-run\ez-run`

## Kiosks @ Conklin

These should run the kiosks.py script which is the one setup in `.\dist\ez-run.exe` by default. I believe you'll need to drag the entire ez-run.exe folder as it include some important files in `_internal` & it shouldn't require a python interpretter on the final system, but this needs to be tested
