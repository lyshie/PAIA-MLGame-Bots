#!/usr/bin/env bash

# ./pingpong.sh [組隊名稱1] [組隊名稱2] [得分]
# ./pingpong.sh 850 851 3

python MLGame.py                              \
                 `# FPS` -f  50               \
                `# 玩家` -i  $1/ml_play.py    \
                `# 玩家` -i  $2/ml_play.py    \
                         pingpong             \
            `# 難度模式` NORMAL               \
                `# 得分` $3
