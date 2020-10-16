import numpy as np
import time
import sys
import tkinter as tk
from PIL import ImageTk, Image

PhotoImage = ImageTk.PhotoImage
UNIT = 40   # pixels
MAZE_H = 10  # grid height
MAZE_W = 10  # grid width
UNIT1=100


class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('maze')
        self.shapes = self.load_images()
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
        self._build_maze()

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
        hell2_center = origin + np.array([UNIT * 4, UNIT ])
        hell3_center = origin + np.array([0, UNIT*2])
        hell4_center = origin + np.array([UNIT, UNIT *2])
        hell5_center = origin + np.array([UNIT*4, UNIT *2])
        hell6_center = origin + np.array([UNIT*8, UNIT *3])
        hell7_center = origin + np.array([UNIT*9, UNIT *3])
        hell8_center = origin + np.array([0, UNIT *5])
        hell9_center = origin + np.array([UNIT, UNIT *5])
        hell10_center = origin + np.array([UNIT*3, UNIT *5])
        hell11_center = origin + np.array([0, UNIT *6])
        hell12_center = origin + np.array([UNIT*4, UNIT *5])
        hell13_center = origin + np.array([UNIT*7, UNIT *6])
        hell14_center = origin + np.array([UNIT*3, UNIT *8])
        hell15_center = origin + np.array([UNIT*2, UNIT *8])
        hell16_center = origin + np.array([UNIT*5, UNIT *8])
        hell17_center = origin + np.array([UNIT*4, UNIT *9])
        hell18_center = origin + np.array([UNIT*5, UNIT *9])
        hell19_center = origin + np.array([UNIT*0, UNIT *9])
        hell20_center = origin + np.array([UNIT * 7, UNIT * 7])
        hell21_center = origin + np.array([UNIT * 8, UNIT * 7])
        hell22_center = origin + np.array([UNIT * 8, UNIT * 6])
        hell23_center = origin + np.array([UNIT * 9, UNIT * 4])
        hell24_center = origin + np.array([UNIT * 5, UNIT * 3])
        hell25_center = origin + np.array([UNIT * 4, UNIT * 4])
        self.hell1 = self.canvas.create_image(
            hell1_center[0],hell1_center[1],
            image=self.shapes[1])

        self.hell2 = self.canvas.create_image(
            hell2_center[0],hell2_center[1],
            image=self.shapes[1])

        self.hell3 = self.canvas.create_image(
            hell3_center[0],hell3_center[1],
            image=self.shapes[1])

        self.hell4 = self.canvas.create_image(
            hell4_center[0],hell4_center[1],
            image=self.shapes[1])

        self.hell5 = self.canvas.create_image(
            hell5_center[0],hell5_center[1],
            image=self.shapes[1])

        self.hell6 = self.canvas.create_image(
            hell6_center[0],hell6_center[1],
            image=self.shapes[1])

        self.hell7 = self.canvas.create_image(
            hell7_center[0],hell7_center[1],
            image=self.shapes[1])

        self.hell8 = self.canvas.create_image(
            hell8_center[0],hell8_center[1],
            image=self.shapes[1])

        self.hell9 = self.canvas.create_image(
            hell9_center[0],hell9_center[1],
            image=self.shapes[1])

        self.hell10 = self.canvas.create_image(
            hell10_center[0],hell10_center[1],
            image=self.shapes[1])

        self.hell11 = self.canvas.create_image(
            hell11_center[0],hell11_center[1],
            image=self.shapes[1])

        self.hell12 = self.canvas.create_image(
            hell12_center[0],hell12_center[1],
            image=self.shapes[1])

        self.hell13 = self.canvas.create_image(
            hell13_center[0],hell13_center[1],
            image=self.shapes[1])
        self.hell14 = self.canvas.create_image(
            hell14_center[0],hell14_center[1],
            image=self.shapes[1])

        self.hell15 = self.canvas.create_image(
            hell15_center[0],hell15_center[1],
            image=self.shapes[1])

        self.hell16 = self.canvas.create_image(
            hell16_center[0],hell16_center[1],
            image=self.shapes[1])

        self.hell17 = self.canvas.create_image(
            hell17_center[0],hell17_center[1],
            image=self.shapes[1])

        self.hell18 = self.canvas.create_image(
            hell18_center[0],hell18_center[1],
            image=self.shapes[1])

        self.hell19 = self.canvas.create_image(
            hell19_center[0],hell19_center[1],
            image=self.shapes[1])
        self.hell20 = self.canvas.create_image(
            hell20_center[0], hell20_center[1],
            image=self.shapes[1])
        self.hell21 = self.canvas.create_image(
            hell21_center[0], hell21_center[1],
            image=self.shapes[1])
        self.hell22 = self.canvas.create_image(
            hell22_center[0], hell22_center[1],
            image=self.shapes[1])
        self.hell23 = self.canvas.create_image(
            hell23_center[0], hell23_center[1],
            image=self.shapes[1])
        self.hell24 = self.canvas.create_image(
            hell24_center[0], hell24_center[1],
            image=self.shapes[1])
        self.hell25 = self.canvas.create_image(
            hell25_center[0], hell25_center[1],
            image=self.shapes[1])
        # hell1_center = origin + np.array([UNIT * 3, UNIT])
        # self.hell1 = self.canvas.create_image(
        #     hell1_center[0],hell1_center[1],
        #     image=self.shapes[1])
        # # self.hell1 = self.canvas.create_rectangle(
        # #     hell1_center[0] - 15, hell1_center[1] - 15,
        # #     hell1_center[0] + 15, hell1_center[1] + 15,
        # #     fill='black')
        #
        # hell2_center = origin + np.array([UNIT * 4, UNIT ])
        # self.hell2 = self.canvas.create_rectangle(
        #     hell2_center[0] - 15, hell2_center[1] - 15,
        #     hell2_center[0] + 15, hell2_center[1] + 15,
        #     fill='black')
        #
        # hell3_center = origin + np.array([0, UNIT*2])
        # self.hell3 = self.canvas.create_rectangle(
        #     hell3_center[0] - 15, hell3_center[1] - 15,
        #     hell3_center[0] + 15, hell3_center[1] + 15,
        #     fill='black')
        #
        # hell4_center = origin + np.array([UNIT, UNIT *2])
        # self.hell4 = self.canvas.create_rectangle(
        #     hell4_center[0] - 15, hell4_center[1] - 15,
        #     hell4_center[0] + 15, hell4_center[1] + 15,
        #     fill='black')
        # hell5_center = origin + np.array([UNIT*4, UNIT *2])
        # self.hell5 = self.canvas.create_rectangle(
        #     hell5_center[0] - 15, hell5_center[1] - 15,
        #     hell5_center[0] + 15, hell5_center[1] + 15,
        #     fill='black')
        # hell6_center = origin + np.array([UNIT*8, UNIT *3])
        # self.hell6 = self.canvas.create_rectangle(
        #     hell6_center[0] - 15, hell6_center[1] - 15,
        #     hell6_center[0] + 15, hell6_center[1] + 15,
        #     fill='black')
        # hell7_center = origin + np.array([UNIT*9, UNIT *3])
        # self.hell7 = self.canvas.create_rectangle(
        #     hell7_center[0] - 15, hell7_center[1] - 15,
        #     hell7_center[0] + 15, hell7_center[1] + 15,
        #     fill='black')
        # hell8_center = origin + np.array([0, UNIT *5])
        # self.hell8 = self.canvas.create_rectangle(
        #     hell8_center[0] - 15, hell8_center[1] - 15,
        #     hell8_center[0] + 15, hell8_center[1] + 15,
        #     fill='black')
        # hell9_center = origin + np.array([UNIT, UNIT *5])
        # self.hell9 = self.canvas.create_rectangle(
        #     hell9_center[0] - 15, hell9_center[1] - 15,
        #     hell9_center[0] + 15, hell9_center[1] + 15,
        #     fill='black')
        # hell10_center = origin + np.array([UNIT*3, UNIT *5])
        # self.hell10 = self.canvas.create_rectangle(
        #     hell10_center[0] - 15, hell10_center[1] - 15,
        #     hell10_center[0] + 15, hell10_center[1] + 15,
        #     fill='black')
        # hell11_center = origin + np.array([0, UNIT *6])
        # self.hell11 = self.canvas.create_rectangle(
        #     hell11_center[0] - 15, hell11_center[1] - 15,
        #     hell11_center[0] + 15, hell11_center[1] + 15,
        #     fill='black')
        # hell12_center = origin + np.array([UNIT*4, UNIT *6])
        # self.hell12 = self.canvas.create_rectangle(
        #     hell12_center[0] - 15, hell12_center[1] - 15,
        #     hell12_center[0] + 15, hell12_center[1] + 15,
        #     fill='black')
        # hell13_center = origin + np.array([UNIT*7, UNIT *6])
        # self.hell13 = self.canvas.create_rectangle(
        #     hell13_center[0] - 15, hell13_center[1] - 15,
        #     hell13_center[0] + 15, hell13_center[1] + 15,
        #     fill='black')
        # hell14_center = origin + np.array([UNIT*4, UNIT *7])
        # self.hell14 = self.canvas.create_rectangle(
        #     hell14_center[0] - 15, hell14_center[1] - 15,
        #     hell14_center[0] + 15, hell14_center[1] + 15,
        #     fill='black')
        # hell15_center = origin + np.array([UNIT*2, UNIT *8])
        # self.hell15 = self.canvas.create_rectangle(
        #     hell15_center[0] - 15, hell15_center[1] - 15,
        #     hell15_center[0] + 15, hell15_center[1] + 15,
        #     fill='black')
        # hell16_center = origin + np.array([UNIT*5, UNIT *8])
        # self.hell16 = self.canvas.create_rectangle(
        #     hell16_center[0] - 15, hell16_center[1] - 15,
        #     hell16_center[0] + 15, hell16_center[1] + 15,
        #     fill='black')
        # hell17_center = origin + np.array([UNIT*4, UNIT *9])
        # self.hell17 = self.canvas.create_rectangle(
        #     hell17_center[0] - 15, hell17_center[1] - 15,
        #     hell17_center[0] + 15, hell17_center[1] + 15,
        #     fill='black')
        # hell18_center = origin + np.array([UNIT*5, UNIT *9])
        # self.hell18 = self.canvas.create_rectangle(
        #     hell18_center[0] - 15, hell18_center[1] - 15,
        #     hell18_center[0] + 15, hell18_center[1] + 15,
        #     fill='black')
        # hell19_center = origin + np.array([UNIT*0, UNIT *9])
        # self.hell19 = self.canvas.create_rectangle(
        #     hell19_center[0] - 15, hell19_center[1] - 15,
        #     hell19_center[0] + 15, hell19_center[1] + 15,
        #     fill='black')
        # create oval
        oval_center = origin + UNIT * 9
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
        # return observation
        self.render()
        return self.canvas.coords(self.rect)

    def step(self, action):
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
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
        self.canvas.tag_raise(self.rect)
        s_ = self.canvas.coords(self.rect)  # next state

        # reward function
        if s_ == self.canvas.coords(self.oval):
            reward = 1
            done = True
            s_ = 'terminal'
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3),self.canvas.coords(self.hell4),self.canvas.coords(self.hell5)
                    ,self.canvas.coords(self.hell6),self.canvas.coords(self.hell7),self.canvas.coords(self.hell8),self.canvas.coords(self.hell9),self.canvas.coords(self.hell10)
                    ,self.canvas.coords(self.hell11),self.canvas.coords(self.hell12),self.canvas.coords(self.hell13),self.canvas.coords(self.hell14),self.canvas.coords(self.hell15)
                    ,self.canvas.coords(self.hell16),self.canvas.coords(self.hell17),self.canvas.coords(self.hell19),self.canvas.coords(self.hell18),self.canvas.coords(self.hell20),
                    self.canvas.coords(self.hell21),self.canvas.coords(self.hell22),self.canvas.coords(self.hell23),self.canvas.coords(self.hell24),self.canvas.coords(self.hell25)]:
            reward = -1
            done = True
            s_ = 'terminal'
        else:
            reward = 0
            done = False

        return s_, reward, done

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

class Maze_info(tk.Tk, object):
    def __init__(self):
        super(Maze_info, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.HEIGHT=10
        self.WIDTH=10
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