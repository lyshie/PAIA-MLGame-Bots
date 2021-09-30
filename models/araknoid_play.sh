#!/bin/sh
python MLGame.py -r -f 720 -i ml_play.py       arkanoid EASY $1 &
python MLGame.py -r -f 720 -i ml_play_rand.py  arkanoid EASY $1 &
python MLGame.py -r -f 720 -i ml_play_rand2.py arkanoid EASY $1 &
python MLGame.py -r -f 720 -i ml_play_rand3.py arkanoid EASY $1 &
