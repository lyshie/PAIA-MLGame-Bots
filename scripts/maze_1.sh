#!/usr/bin/env bash

python MLGame.py                              \
	          `# 玩一次` -1                   \
                 `# FPS` -f  30               \
                  `# 1P` -i  850/ml_play.py   \
                  `# 2P` -i 1317/ml_play.py   \
                  `# 3P` -i 1318/ml_play.py   \
                  `# 4P` -i  953/ml_play.py   \
                         Maze_Car             \
          `# 參賽者數量` 4                    \
            `# 比賽模式` MAZE                 \
                `# 地圖` $1                   \
            `# 結束時間` $2                   \
          `# 五個感應器` 5                    \
            `# 關閉音效` off                  \
