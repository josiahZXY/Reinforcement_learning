import numpy as np
import tkinter as tk
from PIL import ImageTk, Image

PhotoImage = ImageTk.PhotoImage
np.random.seed(1)
UNIT = 40
MAZE_H = 4
MAZE_W = 4

class Maze_carlo(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('maze')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_W * UNIT))
        self._build_maze()
        self.shapes = self.load_images()
        #self.canvas = self._build_canvas()
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
        hell1_center = origin + np.array([UNIT , UNIT])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 15, hell1_center[1] - 15,
            hell1_center[0] + 15, hell1_center[1] + 15,
            fill='black'
        )

        # create hell2
        hell2_center = origin + np.array([UNIT*3, UNIT ])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 15, hell2_center[1] - 15,
            hell2_center[0] + 15, hell2_center[1] + 15,
            fill='black'
        )

        hell3_center = origin + np.array([0, UNIT * 3])
        self.hell3 = self.canvas.create_rectangle(
            hell3_center[0] - 15, hell3_center[1] - 15,
            hell3_center[0] + 15, hell3_center[1] + 15,
            fill='black'
        )
        hell4_center = origin + np.array([UNIT*3, UNIT * 2])
        self.hell4 = self.canvas.create_rectangle(
            hell4_center[0] - 15, hell4_center[1] - 15,
            hell4_center[0] + 15, hell4_center[1] + 15,
            fill='black'
        )
        # create oval
        oval_center = origin + UNIT * 3
        self.oval = self.canvas.create_oval(
            oval_center[0] - 15, oval_center[1] - 15,
            oval_center[0] + 15, oval_center[1] + 15,
            fill='yellow'
        )

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
            reward = 1
            done = True
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3),self.canvas.coords(self.hell4)]:
            reward = -1
            done = True
        else:
            reward = 0
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