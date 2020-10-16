import numpy as np
import time
import sys
import tkinter as tk
from PIL import ImageTk, Image

PhotoImage = ImageTk.PhotoImage

  # pixels
MAZE_H = 4  # grid height
MAZE_W = 4  # grid width
UNIT = 40
UNIT1=100

class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.HEIGHT=4
        self.WIDTH=4
        self.title('maze')
        self.shapes = self.load_images()
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
        self._build_maze()
        self.texts=[]


        #self.canvas = self._build_maze()
    def load_images(self):
        rectangle = PhotoImage(
            Image.open("pjimg/robot.png").resize((20, 20)))
        tree = PhotoImage(
            Image.open("pjimg/trap.png").resize((20, 20)))
        star = PhotoImage(
            Image.open("pjimg/goal.png").resize((20, 20)))
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
        self.canvas = tk.Canvas(self, bg='white',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)

        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # create origin
        origin = np.array([20, 20])

        # hell
        hell1_center = origin + np.array([UNIT * 3, UNIT])
        self.hell1 = self.canvas.create_image(
            hell1_center[0],hell1_center[1],
            image=self.shapes[1])

        # self.hell1 = self.canvas.create_rectangle(
        #     hell1_center[0] - 15, hell1_center[1] - 15,
        #     hell1_center[0] + 15, hell1_center[1] + 15,
        #     fill='black')
        # hell
        hell2_center = origin + np.array([0, UNIT * 3])
        self.hell2 = self.canvas.create_image(
            hell2_center[0],hell2_center[1],
            image=self.shapes[1])
        # self.hell2 = self.canvas.create_rectangle(
        #     hell2_center[0] - 15, hell2_center[1] - 15,
        #     hell2_center[0] + 15, hell2_center[1] + 15,
        #     fill='black')

        hell3_center = origin + np.array([UNIT, UNIT])
        self.hell3 = self.canvas.create_image(
            hell3_center[0],hell3_center[1],
            image=self.shapes[1])
        # self.hell3 = self.canvas.create_rectangle(
        #     hell3_center[0] - 15, hell3_center[1] - 15,
        #     hell3_center[0] + 15, hell3_center[1] + 15,
        #     fill='black')

        hell4_center = origin + np.array([UNIT*3, UNIT *2])
        self.hell4 = self.canvas.create_image(
            hell4_center[0],hell4_center[1],
            image=self.shapes[1])
        # self.hell4 = self.canvas.create_rectangle(
        #     hell4_center[0] - 15, hell4_center[1] - 15,
        #     hell4_center[0] + 15, hell4_center[1] + 15,
        #     fill='black')
        # create oval
        oval_center = origin + UNIT * 3
        self.oval = self.canvas.create_image(
            oval_center[0] , oval_center[1] ,
            image=self.shapes[2])
        # self.oval = self.canvas.create_oval(
        #     oval_center[0] - 15, oval_center[1] - 15,
        #     oval_center[0] + 15, oval_center[1] + 15,
        #     fill='yellow')

        # create red rect
        self.rect = self.canvas.create_image(
            origin[0] , origin[1],
           image=self.shapes[0])
        # self.rect = self.canvas.create_rectangle(
        #     origin[0] - 15, origin[1] - 15,
        #     origin[0] + 15, origin[1] + 15,
        #     fill='red')

        # pack all
        self.canvas.pack()

    def reset(self):
        self.update()
        self.canvas.delete(self.rect)
        origin = np.array([20, 20])
        self.rect = self.canvas.create_image(
            origin[0] , origin[1],
           image=self.shapes[0])
        # self.rect = self.canvas.create_rectangle(
        #     origin[0] - 15, origin[1] - 15,
        #     origin[0] + 15, origin[1] + 15,
        #     fill='red')
        self.render()
        # return observation
        return self.canvas.coords(self.rect)

    def step(self, action):
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        print(s)
        if action == 0:   # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])  # move agent

        s_ = self.canvas.coords(self.rect)  # next state

        # reward function
        if s_ == self.canvas.coords(self.oval):
            reward = 1
            done = True
            s_ = 'terminal'
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3),self.canvas.coords(self.hell4)]:
            reward = -1
            done = True
            s_ = 'terminal'
        else:
            reward = 0
            done = False

        return s_, reward, done

    def render(self):
        self.update()

    def text_value(self, row, col, contents, action, font='Helvetica', size=8, style='normal', anchor='nw'):
        if action == 0:
            origin_x, origin_y = -4, -20
        elif action == 1:
            origin_x, origin_y = -4, 10
        elif action == 2:
            origin_x, origin_y = 8, -4
        else:
            origin_x, origin_y = -18, -4
        x, y = row + origin_x, col + origin_y
        font = (font, str(size), style)
        text = self.canvas.create_text(x, y, fill='black', text=contents, font=font, anchor=anchor)
        return self.texts.append(text)

    def print_value_all(self, data_q):
        for i in range(1, data_q.shape[0]):
            x = data_q['x'][i]
            y = data_q['y'][i]
            for j in range(1, data_q.shape[0]):
                temp1 = data_q.iat[i, 1]
                temp2 = data_q.iat[i, 2]
                temp3 = data_q.iat[i, 3]
                temp4 = data_q.iat[i, 4]
                self.text_value(x, y, round(temp1, 1), 0)
                self.text_value(x, y, round(temp2, 1), 1)
                self.text_value(x, y, round(temp3, 1), 2)
                self.text_value(x, y, round(temp4, 1), 3)

    def show_road(self,n_x,n_y,best_one):
        if best_one==0:
            self.canvas.create_image(n_x, n_y, image=self.shapes[3])
        elif best_one==1:
            self.canvas.create_image(n_x, n_y, image=self.shapes[4])
        elif best_one==2:
            self.canvas.create_image(n_x, n_y, image=self.shapes[6])
        elif best_one==3:
            self.canvas.create_image(n_x, n_y, image=self.shapes[5])


class Maze_info(tk.Tk, object):
    def __init__(self):
        super(Maze_info, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.HEIGHT=4
        self.WIDTH=4
        self.title('maze')
        # self.shapes = self.load_images()
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT1, MAZE_H * UNIT1))
        self._build_maze()
        self.texts=[]
    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                           height=MAZE_H * UNIT1,
                           width=MAZE_W * UNIT1)

        # create grids
        for c in range(0, MAZE_W * UNIT1, UNIT1):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT1
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT1, UNIT1):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT1, r
            self.canvas.create_line(x0, y0, x1, y1)

        # create origin
        origin = np.array([20, 20])
        self.canvas.pack()
    def render(self):
        self.update()
    def text_value(self,row,col,contents,action,font='Helvetica',size=8,style='normal',anchor='nw'):
        if action==0:
            origin_x,origin_y=-10,-40
        elif action==1:
            origin_x,origin_y=-10,25
        elif action==2:
            origin_x,origin_y=23,-10
        else:
            origin_x,origin_y=-45,-10
        x,y=row+origin_x,col+origin_y
        font=(font,str(size),style)
        text=self.canvas.create_text(x,y,fill='black',text=contents,font=font,anchor=anchor)
        return self.texts.append(text)
    def print_value_all(self,data_q):
        for i in range(1,data_q.shape[0]):
            x=data_q['x'][i]*2.5
            y=data_q['y'][i]*2.5
            for j in range(1,data_q.shape[0]):
                temp1=data_q.iat[i,1]
                temp2 = data_q.iat[i, 2]
                temp3 = data_q.iat[i, 3]
                temp4 = data_q.iat[i, 4]
                self.text_value(x, y, round(temp1, 2), 0)
                self.text_value(x, y, round(temp2, 2), 1)
                self.text_value(x, y, round(temp3, 2), 2)
                self.text_value(x, y, round(temp4, 2), 3)