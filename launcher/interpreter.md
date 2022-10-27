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

Python 3.10.7 (Fedora 36)
$ pyinstaller --clean                                \
              --collect-all mlgame                   \
              --hidden-import cmath                  \
              --hidden-import csv                    \
              --hidden-import pathlib                \
              --hidden-import matplotlib.pyplot      \
              --hidden-import queue                  \
              --hidden-import pygame                 \
              --hidden-import multiprocessing        \
              --hidden-import pickle                 \
              --hidden-import Box2D                  \
              --hidden-import sklearn.neighbors      \
              --hidden-import sklearn.tree           \
              --hidden-import sklearn.svm            \
              --hidden-import sklearn.ensemble       \
              --hidden-import sklearn.neural_network \
              --hidden-import sklearn.linear_model   \
              --hidden-import sklearn.metrics        \
              --hidden-import sklearn.model_selection      \
              --hidden-import sklearn.utils._weight_vector \
              --hidden-import scipy.special.cython_special \
              --hidden-import pandas                       \
              --hidden-import pytmx                        \
              interpreter.py

Python 3.10.2 (Fedora 35)
$ pyinstaller --clean                      \
              --hidden-import pygame       \
              --hidden-import Box2D        \
              --hidden-import sklearn      \
              --hidden-import matplotlib   \
              --hidden-import pynput       \
              --hidden-import sklearn.utils._typedefs            \
              --hidden-import sklearn.neural_network             \
              --hidden-import sklearn.ensemble                   \
              --hidden-import sklearn.neighbors._partition_nodes \
              --exclude-module _bootlocale                       \
              interpreter.py
```
