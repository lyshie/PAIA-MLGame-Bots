# How to rebuild the Python interpreter for PAIA Desktop

```
$ cd [PAIA-Desktop]/resources/app/python

$ mv dist dist2

$ python -m venv build_env

$ source build_env/bin/activate.fish

$ pip install pyinstaller

$ wget https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Paia-Desktop/master/requirements.txt

$ pip install --upgrade -r requirements.txt
$ pip install --upgrade pyinstaller

$ wget https://raw.githubusercontent.com/lyshie/PAIA-MLGame-Bots/main/launcher/interpreter.py

$ pyinstaller --clean                      \
              --hidden-import pygame       \
              --hidden-import Box2D        \
              --hidden-import sklearn      \
              --hidden-import matplotlib   \
              --hidden-import pynput       \
              interpreter.py
```
