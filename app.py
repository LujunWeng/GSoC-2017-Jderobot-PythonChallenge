import tkinter as tk
from enum import Enum
import sys
from modules.config_reader import ConfigReader
from modules.conway import Universe


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class GameStatus(Enum):
    PAUSE = 0
    ONGOING = 1


class GameOfLife(tk.Frame):
    WIDTH = 800
    HEIGHT = 800

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.canvas = tk.Canvas(self, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack(side=tk.BOTTOM)
        self.control_info = tk.Frame(self)
        self.control_info.pack(side=tk.TOP, fill=tk.X)
        self.start_button = tk.Button(self.control_info, text='Start', command=self.start)
        self.start_button.pack(side=tk.RIGHT)
        self.pause_button = tk.Button(self.control_info, text='Pause', command=self.pause)
        self.pause_button.pack(side=tk.RIGHT)
        self.reset_button = tk.Button(self.control_info, text='Reset & Change Pattern', command=self.reset)
        self.reset_button.pack(side=tk.RIGHT)
        self.generation_text_var = tk.StringVar()
        self.generation_text = tk.Label(self.control_info, textvariable=self.generation_text_var)
        self.generation_text.pack()

        # Read config file
        cfg = ConfigReader()
        cfg.read('./')
        dim = (cfg.height, cfg.width)
        if cfg.height > 200 or cfg.width > 200:
            eprint("Height and Width must be equal to less than 200!")
            sys.exit()
        nos = cfg.numofseed
        self.u = Universe(dim)
        self.nseed = nos

        self.status = GameStatus.ONGOING
        self.reset()

    def draw(self):
        if self.status == GameStatus.ONGOING:
            self.canvas.delete('all')
            h, w = self.u.dim
            ds = self.WIDTH / max(h, w)
            for i in range(h):
                for j in range(w):
                    if self.u.space[i][j] == 1:
                        self.canvas.create_rectangle(
                            j*ds, i*ds, j*ds+ds, i*ds+ds, fill="black")
                    else:
                        self.canvas.create_rectangle(
                            j*ds, i*ds, j*ds+ds, i*ds+ds)
            self.generation_text_var.set("Width: {}, Height: {}, Number of initial seeds: {}\nGeneration: {} ".
                                         format(self.u.dim[1], self.u.dim[0], self.nseed, self.u.generation))
            self.u.next_generation()
            self.after(1000, self.draw)

    def start(self):
        self.status = GameStatus.ONGOING
        self.draw()

    def reset(self):
        self.u.random_reset(self.nseed)
        self.status = GameStatus.ONGOING
        self.draw()
        self.status = GameStatus.PAUSE

    def pause(self):
        self.status = GameStatus.PAUSE


root = tk.Tk()
root.geometry('+%d+%d' % (200, 200))
app = GameOfLife(master=root)
app.mainloop()
