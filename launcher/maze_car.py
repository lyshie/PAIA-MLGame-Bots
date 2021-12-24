import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, scrolledtext
from PIL import Image, ImageTk
import subprocess


class MazeOption():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("PAIA 迷宮車競賽")
        self.align_right = 'nse'
        self.align_left = 'nsw'
        '''
            Option variables
        '''
        self.imgCars = []
        self.options = {
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

    def layoutOutputs(self):
        '''
            Outputs
        '''
        self.scrollOutput = tk.scrolledtext.ScrolledText(self.frameOutputs)
        self.scrollOutput.grid(column=0, row=0)

    def cmdSelectCar(self, event):
        dlg = filedialog.askdirectory()
        index = int(str(event.widget).split('_')[-1])
        self.options['cars'][index].set(dlg)

    def cmdRun(self):
        for k in self.options.keys():
            if not isinstance(self.options[k], list):
                print(k, self.options[k].get())

        process = subprocess.Popen(['top'],
                                   shell=False,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)

        while True:
            out = process.stdout.readline()
            if not out:
                break
            self.scrollOutput.insert(tk.END, out)
            self.scrollOutput.see(tk.END)
            self.scrollOutput.update_idletasks()


def main():
    maze = MazeOption()


if __name__ == "__main__":
    main()
