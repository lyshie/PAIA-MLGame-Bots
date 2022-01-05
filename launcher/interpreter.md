# How to rebuild the Python interpreter for PAIA Desktop

```
$ cd [PAIA-Desktop]/resources/app/python

$ mv dist dist2

$ python -m venv build_env

$ source build_env/bin/activate.fish

$ pip install pyinstaller

$ pip install box2d-py pygame sklearn matplotlib pynput

$ wget https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/Paia-Desktop/master/python/interpreter.py

$ pyinstaller --clean                      \
              --hidden-import pygame       \
              --hidden-import Box2D        \
              --hidden-import sklearn      \
              --hidden-import matplotlib   \
              --hidden-import pynput       \
              interpreter.py
```
