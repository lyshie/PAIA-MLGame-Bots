import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, scrolledtext, messagebox
from PIL import Image, ImageTk
import subprocess
import os
import sys
import json
import re


class MazeLauncher():
    def __init__(self, paia=''):
        self.win = tk.Tk()
        self.win.title("PAIA 迷宮車競賽")
        self.align_right = 'e'
        self.align_left = 'w'
        self.align_full = 'nswe'
        '''
            定位 PAIA Desktop 目錄
            1. MLGame.py   (遊戲引擎)
            2. interpreter (Python 直譯器)

            windows: PAIA-Desktop-win32-x64-2.0.0\PAIA Desktop.exe
            linux:   /usr/lib/paia-desktop/PAIA Desktop
        '''
        if not paia:
            paia = filedialog.askopenfilename(
                title='找出 PAIA Desktop 應用程式',
                filetypes=("執行檔 {PAIA\ Desktop*}", ))
        if not paia:
            messagebox.showerror(message='找不到 PAIA Desktop')
            self.win.destroy()
            sys.exit(1)

        self.paia = os.path.normpath(os.path.dirname(paia))
        self.mlgame = os.path.join(self.paia, 'resources', 'app', 'MLGame')
        '''
            Option variables
        '''
        self.imgCars = []
        self.options = {
            'mlgame': StringVar(value=self.mlgame),
            'mode': StringVar(value='MAZE'),
            'map': IntVar(value='1'),
            'fps': IntVar(value='30'),
            'frames': IntVar(value='1200'),
            'cars': [StringVar() for x in range(0, 6)],
            'oneshot': BooleanVar(value=True)
        }
        '''
            Layout
        '''
        self.frameOpts = ttk.Frame(self.win)
        self.frameCars = ttk.Frame(self.win)
        self.frameCmds = ttk.Frame(self.win)
        self.frameOutputs = ttk.Frame(self.win)

        self.frameOpts.grid(column=0, row=0, sticky=self.align_right)
        self.frameCars.grid(column=1, row=0, sticky=self.align_left)
        self.frameCmds.grid(column=0, row=1, columnspan=2)
        self.frameOutputs.grid(column=0,
                               row=2,
                               columnspan=2,
                               sticky=self.align_full)

        self.layoutOptions()
        self.layoutCars()
        self.layoutCommands()
        self.layoutOutputs()

        self.win.update_idletasks()

        # auto-resize frame
        self.win.columnconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        self.win.rowconfigure(0, weight=0)
        self.win.rowconfigure(1, weight=0)
        self.win.rowconfigure(2, weight=1)

        self.win.mainloop()

    def layoutOptions(self):
        '''
            Options
        '''
        # 遊戲模式
        lblMode = ttk.Label(self.frameOpts, text='遊戲模式', anchor='e')
        lblMode.grid(column=0, row=0, sticky=self.align_right)
        cmbMode = ttk.Combobox(self.frameOpts,
                               textvariable=self.options['mode'],
                               values=['MAZE', 'MOVE_MAZE', 'PRACTICE'],
                               state='readonly')
        cmbMode.grid(column=1, row=0, sticky=self.align_left)

        # 地圖
        lblMap = ttk.Label(self.frameOpts, text='地圖', anchor='e')
        lblMap.grid(column=0, row=1, sticky=self.align_right)
        spinMap = ttk.Spinbox(self.frameOpts,
                              from_=1,
                              to=9999,
                              textvariable=self.options['map'])
        spinMap.grid(column=1, row=1, sticky=self.align_left)

        # FPS
        lblFPS = ttk.Label(self.frameOpts, text='每秒影格數', anchor='e')
        lblFPS.grid(column=0, row=2, sticky=self.align_right)
        spinFPS = ttk.Spinbox(self.frameOpts,
                              from_=1,
                              to=9999,
                              textvariable=self.options['fps'])
        spinFPS.grid(column=1, row=2, sticky=self.align_left)

        # 總影格數
        lblFrames = ttk.Label(self.frameOpts, text='總影格數', anchor='e')
        lblFrames.grid(column=0, row=3, sticky=self.align_right)
        spinFrames = ttk.Spinbox(self.frameOpts,
                                 from_=1,
                                 to=9999,
                                 textvariable=self.options['frames'])
        spinFrames.grid(column=1, row=3, sticky=self.align_left)

        # 遊戲次數
        lblOneshot = ttk.Label(self.frameOpts, text='遊戲次數', anchor='e')
        lblOneshot.grid(column=0, row=4, sticky=self.align_right)
        chkOneshot = ttk.Checkbutton(self.frameOpts,
                                     text='只玩一次',
                                     variable=self.options['oneshot'],
                                     onvalue=True,
                                     offvalue=False)
        chkOneshot.grid(column=1, row=4, sticky=self.align_left)

    def layoutCars(self):
        '''
            Cars
        '''
        path = os.path.dirname(os.path.realpath(__file__))
        for i in range(0, 6):
            img = Image.open(
                os.path.join(path, 'images', 'car_%02d.png' % (i + 1, )))
            self.imgCars.append(ImageTk.PhotoImage(img))

        for i, c in enumerate(self.imgCars):
            lblCar = ttk.Label(self.frameCars, image=c)
            lblCar.grid(column=0, row=i)
            entryCar = ttk.Entry(self.frameCars,
                                 name='car_%d' % (i),
                                 state='readonly',
                                 textvariable=self.options['cars'][i])
            entryCar.grid(column=1, row=i)
            entryCar.bind('<ButtonPress-1>', self.cmdSelectCar)

    def layoutCommands(self):
        '''
            Commands
        '''
        btnRun = ttk.Button(self.frameCmds, text='開始比賽', command=self.cmdRun)
        btnRun.grid(column=0, row=0)
        btnClear = ttk.Button(self.frameCmds,
                              text='清除結果',
                              command=self.cmdClear)
        btnClear.grid(column=1, row=0)
        btnQuit = ttk.Button(self.frameCmds, text='結束程式', command=self.cmdQuit)
        btnQuit.grid(column=2, row=0)

    def layoutOutputs(self):
        '''
            Outputs
        '''
        # MLGame 路徑
        entryPath = ttk.Entry(self.frameOutputs,
                              textvariable=self.options['mlgame'],
                              state='readonly',
                              justify=tk.CENTER)
        entryPath.grid(column=0, row=0, sticky=self.align_full)
        entryPath.xview(tk.END)

        # 輸出結果
        self.scrollOutput = tk.scrolledtext.ScrolledText(self.frameOutputs,
                                                         state=tk.DISABLED,
                                                         height=10,
                                                         font='TkFixedFont')
        self.scrollOutput.grid(column=0, row=1, sticky=self.align_full)

        # auto-resize
        self.frameOutputs.rowconfigure(0, weight=0)
        self.frameOutputs.rowconfigure(1, weight=1)
        self.frameOutputs.columnconfigure(0, weight=1)

    def cmdSelectCar(self, event):
        ml_play_path = os.path.join(self.options['mlgame'].get(), 'games',
                                    'Maze_Car', 'ml')
        dlg = filedialog.askdirectory(initialdir=ml_play_path)
        dlg = os.path.basename(dlg)
        index = int(str(event.widget).split('_')[-1])
        self.options['cars'][index].set(dlg)
        event.widget.xview(tk.END)

    def cmdRun(self):
        '''
        for k in self.options.keys():
            if not isinstance(self.options[k], list):
                print(k, self.options[k].get())
        '''

        mlgame_py = os.path.join(self.options['mlgame'].get(), 'MLGame.py')
        interpreter = os.path.join(self.paia, 'resources', 'app', 'python',
                                   'dist', 'interpreter', 'interpreter')
        args = [interpreter, mlgame_py]

        if self.options['oneshot'].get():
            args.append('-1')

        cars = []
        for car in self.options['cars']:
            if car.get() != '':
                cars.append(
                    os.path.join(os.path.basename(car.get()), 'ml_play.py'))
            else:
                break

        args.extend([
            '-f',
            str(self.options['fps'].get()),
        ])

        for car in cars:
            args.extend(['-i', car])

        # 修改自 MLGame 9.2.*
        args.extend([
            'Maze_Car',
            '--user_num',
            str(len(cars)),
            '--game_type',
            self.options['mode'].get(),
            '--map',
            str(self.options['map'].get()),
            '--time_to_play',
            str(self.options['frames'].get()),
            '--sensor_num',
            '5',
            '--sound',
            'off',
        ])

        #print(args)

        process = subprocess.Popen(args,
                                   shell=False,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)

        while True:
            out = process.stdout.readline()
            if not out:
                break
            self.scrollOutput.configure(state=tk.NORMAL)
            self.scrollOutput.insert(tk.END,
                                     self.parseGameResult(out.decode('utf-8')))
            self.scrollOutput.configure(state=tk.DISABLED)
            self.scrollOutput.see(tk.END)
            self.scrollOutput.update_idletasks()

    def cmdClear(self):
        self.scrollOutput.configure(state=tk.NORMAL)
        self.scrollOutput.delete('1.0', tk.END)
        self.scrollOutput.configure(state=tk.DISABLED)

    def cmdQuit(self):
        self.win.destroy()

    def parseGameResult(self, data):
        resList = re.compile(r"(\['1P.+frame'\])", flags=re.M)
        resDict = re.compile(r"({'frame_used':.+\}\]})", flags=re.M)

        result = ''

        m = resList.search(data)
        if m:
            j = json.loads(m.group(1).replace("'", '"'))
            result = os.linesep.join([result, json.dumps(j, indent=4)])

        m = resDict.search(data)
        if m:
            j = json.loads(m.group(1).replace("'", '"'))
            result = os.linesep.join([result, json.dumps(j, indent=4)])

        return result


def main():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        os.chdir(sys._MEIPASS)

    if len(sys.argv) > 1:
        maze = MazeLauncher(os.path.normpath(sys.argv[1]))
    else:
        if os.path.isfile('PAIA Desktop') or os.path.isfile(
                'PAIA Desktop.exe'):
            maze = MazeLauncher(
                os.path.join(os.path.dirname(__file__), 'PAIA Desktop'))
        else:
            maze = MazeLauncher()


if __name__ == "__main__":
    main()
