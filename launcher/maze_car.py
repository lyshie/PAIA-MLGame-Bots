import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, scrolledtext
from PIL import Image, ImageTk
import subprocess
import os
import json
import re
import sys


class MazeOption():
    def __init__(self, mlgame):
        self.win = tk.Tk()
        self.win.title("PAIA 迷宮車競賽")
        self.align_right = 'nse'
        self.align_left = 'nsw'
        self.align_full = 'nswe'
        '''
            Option variables
        '''
        self.imgCars = []
        self.options = {
            'mlgame': StringVar(value=mlgame),
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

        self.frameOpts.grid(column=0, row=0)
        self.frameCars.grid(column=1, row=0)
        self.frameCmds.grid(column=0, row=1, columnspan=2)
        self.frameOutputs.grid(column=0, row=2, columnspan=2)

        self.layoutOptions()
        self.layoutCars()
        self.layoutCommands()
        self.layoutOutputs()

        self.win.update_idletasks()
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
        for i in range(0, 6):
            img = Image.open('car_%02d.png' % (i + 1, ))
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
        self.scrollOutput = tk.scrolledtext.ScrolledText(self.frameOutputs,
                                                         state=tk.DISABLED,
                                                         font='Sans')
        self.scrollOutput.grid(column=0, row=0)

        # MLGame 路徑
        entryPath = ttk.Entry(self.frameOutputs,
                              textvariable=self.options['mlgame'],
                              state='readonly')
        entryPath.grid(column=0, row=1, sticky=self.align_full)
        entryPath.xview_moveto(1)

    def cmdSelectCar(self, event):
        dlg = filedialog.askdirectory(initialdir=os.path.join(
            self.options['mlgame'].get(), 'games', 'Maze_Car', 'ml'))
        index = int(str(event.widget).split('_')[-1])
        self.options['cars'][index].set(dlg)
        event.widget.xview_moveto(1)

    def cmdRun(self):
        '''
        for k in self.options.keys():
            if not isinstance(self.options[k], list):
                print(k, self.options[k].get())
        '''

        mlgame = os.path.join(self.options['mlgame'].get(), 'MLGame.py')
        args = ['python', mlgame]

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

        args.extend([
            'Maze_Car',
            str(len(cars)),
            self.options['mode'].get(),
            str(self.options['map'].get()),
            str(self.options['frames'].get()),
            '5',
            'off',
        ])

        #print(args)

        process = subprocess.Popen(
            args,
            shell=False,
            stdout=subprocess.PIPE,
            #stderr=subprocess.STDOUT
        )

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
    mlgame = os.path.normpath(sys.argv[1])
    maze = MazeOption(mlgame)


if __name__ == "__main__":
    main()
