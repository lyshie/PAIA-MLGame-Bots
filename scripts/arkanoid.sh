#!/usr/bin/env bash

# ./arkanoid.sh [timeout] [組隊名稱] [關卡]
# ./arkanoid.sh 90 850 1

timeout `# 強制中止時間` $1                   \
python MLGame.py                              \
                `# 一次` -1                   \
                 `# FPS` -f  50               \
                `# 玩家` -i  $2/ml_play.py    \
                         arkanoid             \
            `# 難度模式` NORMAL               \
            `# 關卡編號` $3
