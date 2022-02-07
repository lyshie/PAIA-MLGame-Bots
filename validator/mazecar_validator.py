#!/usr/bin/env python
'''
    使用方式
    $ python mazecar_validator.py -f/--file ml_play.py
'''

import argparse
import re


class Validator():
    def __init__(self, content):
        self._content = content
        self._funcs = list()

        self._reg_checks()

    '''
        自動註冊所有 check_* 函式
    '''

    def _reg_checks(self):
        for f in dir(self):
            if f.startswith("check_"):
                self._funcs.append(getattr(self, f))

    '''
         使用所有 check_* 函式做檢查
    '''

    def check(self):
        for func in self._funcs:
            print(func())

    '''
        檢查是否使用模型來預測
    '''

    def check_predict(self):
        pat = re.compile(r"\w+ \s+ = \s+ \w+\.predict\(.+?\)", re.X)
        matches = pat.findall(self._content)
        if matches:
            return "[ OK ] 有使用模型預測\n\t{}".format("\n\t".join(matches))
        else:
            return "[FAIL] 未使用模型預測"

    '''
        檢查是否有載入模型檔案 model.pickle
    '''

    def check_model(self):
        pat = re.compile(
            r"with \s+ open \s*? \( .+? '.pickle' .+? \) \s+ as \s+ f:", re.X)
        matches = pat.findall(self._content)
        if matches:
            return "[ OK ] 有載入模型 (model.pickle)\n\t{}".format(
                "\n\t".join(matches))
        else:
            return "[FAIL] 未載入模型 (model.pickle)"

    '''
        檢查是否有使用按鍵，避免人為介入
    '''

    def check_keyboard(self):
        pat = re.compile(r"_KEYBOARD_ON_PRESSED\[\" .+? \"\]", re.X)
        matches = pat.findall(self._content)
        if matches:
            return "[WARN] 使用按鍵\n\t{}".format("\n\t".join(matches))
        else:
            return "[ OK ] 未使用按鍵"


def main():
    args = argparse.ArgumentParser()
    args.add_argument("-f", "--file", help="輸入檔案 (ml_play.py)")
    args.add_argument("-q", "--quiet", action="store_true", help="隱藏資訊")
    options = args.parse_args()

    if not options.quiet:
        print("檢查檔案 {}".format(options.file))

    # 讀入 ml_play.py 原始碼
    content = ''
    with open(options.file) as f:
        content = f.read()

    # 檢查
    validator = Validator(content)
    validator.check()


if __name__ == "__main__":
    main()
