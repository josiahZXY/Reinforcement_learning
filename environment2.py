import numpy as np
import tkinter as tk
from PIL import ImageTk, Image

PhotoImage = ImageTk.PhotoImage
np.random.seed(1)
UNIT = 40
MAZE_H = 10
MAZE_W = 10

class Maze_carlo(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('maze')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_W * UNIT))
        self._build_maze()
        self.shapes = self.load_images()
    def load_images(self):
        rectangle = PhotoImage(
            Image.open("pjimg/robot.png").resize((65, 65)))
        tree = PhotoImage(
            Image.open("pjimg/trap.png").resize((65, 65)))
        star = PhotoImage(
            Image.open("pjimg/goal.png").resize((65, 65)))
        up = PhotoImage(
            Image.open("img/up.png").resize((20, 20)))
        down = PhotoImage(
            Image.open("img/down.png").resize((20, 20)))
        left = PhotoImage(
            Image.open("img/left.png").resize((20, 20)))
        right = PhotoImage(
            Image.open("img/right.png").resize((20, 20)))
        circle = PhotoImage(
            Image.open("img/circle.png").resize((20, 20)))
        return rectangle, tree, star,up,down,left,right,circle

    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white', height=MAZE_H * UNIT, width=MAZE_W * UNIT)
        origin = np.array([20, 20])

        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_H * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # create red rect
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red'
        )

        # create hell1
        hell1_center = origin + np.array([UNIT * 3, UNIT])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 15, hell1_center[1] - 15,
            hell1_center[0] + 15, hell1_center[1] + 15,
            fill='black')
        # hell
        hell2_center = origin + np.array([UNIT * 4, UNIT ])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 15, hell2_center[1] - 15,
            hell2_center[0] + 15, hell2_center[1] + 15,
            fill='black')

        hell3_center = origin + np.array([0, UNIT*2])
        self.hell3 = self.canvas.create_rectangle(
            hell3_center[0] - 15, hell3_center[1] - 15,
            hell3_center[0] + 15, hell3_center[1] + 15,
            fill='black')

        hell4_center = origin + np.array([UNIT, UNIT *2])
        self.hell4 = self.canvas.create_rectangle(
            hell4_center[0] - 15, hell4_center[1] - 15,
            hell4_center[0] + 15, hell4_center[1] + 15,
            fill='black')
        hell5_center = origin + np.array([UNIT*4, UNIT *2])
        self.hell5 = self.canvas.create_rectangle(
            hell5_center[0] - 15, hell5_center[1] - 15,
            hell5_center[0] + 15, hell5_center[1] + 15,
            fill='black')
        hell6_center = origin + np.array([UNIT*8, UNIT *3])
        self.hell6 = self.canvas.create_rectangle(
            hell6_center[0] - 15, hell6_center[1] - 15,
            hell6_center[0] + 15, hell6_center[1] + 15,
            fill='black')
        hell7_center = origin + np.array([UNIT*9, UNIT *3])
        self.hell7 = self.canvas.create_rectangle(
            hell7_center[0] - 15, hell7_center[1] - 15,
            hell7_center[0] + 15, hell7_center[1] + 15,
            fill='black')
        hell8_center = origin + np.array([0, UNIT *5])
        self.hell8 = self.canvas.create_rectangle(
            hell8_center[0] - 15, hell8_center[1] - 15,
            hell8_center[0] + 15, hell8_center[1] + 15,
            fill='black')
        hell9_center = origin + np.array([UNIT, UNIT *5])
        self.hell9 = self.canvas.create_rectangle(
            hell9_center[0] - 15, hell9_center[1] - 15,
            hell9_center[0] + 15, hell9_center[1] + 15,
            fill='black')
        hell10_center = origin + np.array([UNIT*3, UNIT *5])
        self.hell10 = self.canvas.create_rectangle(
            hell10_center[0] - 15, hell10_center[1] - 15,
            hell10_center[0] + 15, hell10_center[1] + 15,
            fill='black')
        hell11_center = origin + np.array([0, UNIT *6])
        self.hell11 = self.canvas.create_rectangle(
            hell11_center[0] - 15, hell11_center[1] - 15,
            hell11_center[0] + 15, hell11_center[1] + 15,
            fill='black')
        hell12_center = origin + np.array([UNIT*4, UNIT *6])
        self.hell12 = self.canvas.create_rectangle(
            hell12_center[0] - 15, hell12_center[1] - 15,
            hell12_center[0] + 15, hell12_center[1] + 15,
            fill='black')
        hell13_center = origin + np.array([UNIT*7, UNIT *6])
        self.hell13 = self.canvas.create_rectangle(
            hell13_center[0] - 15, hell13_center[1] - 15,
            hell13_center[0] + 15, hell13_center[1] + 15,
            fill='black')
        hell14_center = origin + np.array([UNIT*4, UNIT *7])
        self.hell14 = self.canvas.create_rectangle(
            hell14_center[0] - 15, hell14_center[1] - 15,
            hell14_center[0] + 15, hell14_center[1] + 15,
            fill='black')
        hell15_center = origin + np.array([UNIT*2, UNIT *8])
        self.hell15 = self.canvas.create_rectangle(
            hell15_center[0] - 15, hell15_center[1] - 15,
            hell15_center[0] + 15, hell15_center[1] + 15,
            fill='black')
        hell16_center = origin + np.array([UNIT*5, UNIT *8])
        self.hell16 = self.canvas.create_rectangle(
            hell16_center[0] - 15, hell16_center[1] - 15,
            hell16_center[0] + 15, hell16_center[1] + 15,
            fill='black')
        hell17_center = origin + np.array([UNIT*4, UNIT *9])
        self.hell17 = self.canvas.create_rectangle(
            hell17_center[0] - 15, hell17_center[1] - 15,
            hell17_center[0] + 15, hell17_center[1] + 15,
            fill='black')
        hell18_center = origin + np.array([UNIT*5, UNIT *9])
        self.hell18 = self.canvas.create_rectangle(
            hell18_center[0] - 15, hell18_center[1] - 15,
            hell18_center[0] + 15, hell18_center[1] + 15,
            fill='black')
        hell19_center = origin + np.array([UNIT*0, UNIT *9])
        self.hell19 = self.canvas.create_rectangle(
            hell19_center[0] - 15, hell19_center[1] - 15,
            hell19_center[0] + 15, hell19_center[1] + 15,
            fill='black')
        # create oval
        oval_center = origin + UNIT * 9
        self.oval = self.canvas.create_oval(
            oval_center[0] - 15, oval_center[1] - 15,
            oval_center[0] + 15, oval_center[1] + 15,
            fill='yellow')

        # create red rect
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red')

        self.canvas.pack()

    def reset(self):
        self.canvas.delete(self.rect)
        origin = np.array([20, 20])
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red'
        )
        return tuple(self.canvas.coords(self.rect))

    def step(self, action):
        s = self.canvas.coords(self.rect)

        base_action = np.array([0, 0])
        if action == 0:
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:
            if s[0] > UNIT:
                base_action[0] -= UNIT
        self.canvas.move(self.rect, base_action[0], base_action[1])
        s_ = self.canvas.coords(self.rect)

        if s_ == self.canvas.coords(self.oval):
            reward = 100
            done = True
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3),self.canvas.coords(self.hell4),self.canvas.coords(self.hell5),self.canvas.coords(self.hell6),self.canvas.coords(self.hell7),self.canvas.coords(self.hell8),self.canvas.coords(self.hell9),self.canvas.coords(self.hell10),self.canvas.coords(self.hell11),self.canvas.coords(self.hell12),self.canvas.coords(self.hell13),self.canvas.coords(self.hell14),self.canvas.coords(self.hell15),self.canvas.coords(self.hell16),self.canvas.coords(self.hell17),self.canvas.coords(self.hell18),self.canvas.coords(self.hell19)]:
            reward = -10
            done = True
        else:
            reward = -0.1
            done = False

        return tuple(s), reward, done

    def render(self):
        self.update()
    def show_road(self,n_x,n_y,best_one):
        if best_one==0:
            self.canvas.create_image(n_x, n_y, image=self.shapes[3])
        elif best_one==1:
            self.canvas.create_image(n_x, n_y, image=self.shapes[4])
        elif best_one==2:
            self.canvas.create_image(n_x, n_y, image=self.shapes[6])
        elif best_one==3:
            self.canvas.create_image(n_x, n_y, image=self.shapes[5])