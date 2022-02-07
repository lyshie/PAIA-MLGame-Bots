# PAIA-MLGame-Bots
  * [打磚塊地圖編輯器](https://lyshie.github.io/PAIA-MLGame-Bots/editor/arkanoid_editor.html)
  * [迷宮車離線競賽程式](#)
    * [rebuild Python interpreter (interpreter.py)](https://github.com/lyshie/PAIA-MLGame-Bots/blob/main/launcher/interpreter.md)
    * launch program
    ```
    $ git clone --depth 1 https://github.com/lyshie/PAIA-MLGame-Bots
    $ cd launcher
    $ python maze_car.py ~/Downloads/paia-desktop/PAIA\ Desktop
    ```
  * 迷宮地圖編輯
    - 先安裝 [Tiled Map Editor](https://thorbjorn.itch.io/tiled)
    - 下載「[迷宮地圖編輯器.7z](https://github.com/lyshie/PAIA-MLGame-Bots/raw/main/%E8%BF%B7%E5%AE%AE%E5%9C%B0%E5%9C%96%E7%B7%A8%E8%BC%AF%E5%99%A8.7z)」後解壓縮，直接執行「編輯地圖.cmd」
  * 檢查 AI 程式的合法性
    - 先下載 [validator/mazecar_validator.py](https://raw.githubusercontent.com/lyshie/PAIA-MLGame-Bots/main/validator/mazecar_validator.py)
     ```
     $ python mazecar_validator.py -f ml_play.py
     ```
  * 合併 CSV 檔案 (feature*.csv 與 target*.csv)
    ```
    $ rm temp.csv all.csv;
      for i in (seq 1 6);
          dos2unix "feature$i.csv";
          dos2unix "target$i.csv";
          paste -d, "feature$i.csv" "target$i.csv" >> temp.csv;
      end;
      cat headers temp.csv > all.csv;
      cp all.csv /tmp/all.csv
    ```
    ```
    $ cat headers
    "L","LF","F","RF","R","L-W","R-W"
    ```
