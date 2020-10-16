import numpy as np
import tkinter as tk
from PIL import ImageTk, Image
import numpy as np
import random
from collections import defaultdict
import re

np.random.seed(1)
PhotoImage = ImageTk.PhotoImage
UNIT = 100
# HEIGHT = 4
# WIDTH = 4


class Env(tk.Tk):  # 环境继承于tk.Tk

    def __init__(self,HEIGHT,WIDTH):  # 初始化 在创建对象的时候自动调用
        super(Env, self).__init__()  # 父类初始化
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.action_space = ['u', 'd', 'l', 'r']  # 行动集
        self.n_actions = len(self.action_space)  # 可供行动的步数
        self.title('Q Learning')
        self.geometry('{0}x{1}'.format(HEIGHT * UNIT, WIDTH * UNIT))
        # 格式化输出 输出参数为 500 x 500 设定整个画布大小
        # geometry(geometry=None)
        # -- 设置和获取窗口的尺寸
        # -- geometry 参数的格式为："%dx%d%+d%+d" % (width, height, xoffset, yoffset)
        self.shapes = self.load_images()  # 定义类内函数
        self.canvas = self._build_canvas()  # 定义类内函数且是隐藏函数
        self.texts = []

    # 加载图象
    def load_images(self):
        rectangle = PhotoImage(
            Image.open("pjimg/robot.png").resize((65, 65)))
        tree = PhotoImage(
            Image.open("img/circle.png").resize((65, 65)))
        star = PhotoImage(
            Image.open("img/star.jpg").resize((65, 65)))
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

        # 绘制画布 背景为白色

    def _build_canvas(self):
        canvas = tk.Canvas(self, bg='white',
                           height=self.HEIGHT * UNIT,
                           width=self.WIDTH * UNIT)
        # create grids
        for c in range(0, self.WIDTH * UNIT, UNIT):  # 0~400 by 100
            x0, y0, x1, y1 = c, 0, c, self.HEIGHT * UNIT
            canvas.create_line(x0, y0, x1, y1)
        for r in range(0, self.HEIGHT * UNIT, UNIT):  # 0~400 by 100
            x0, y0, x1, y1 = 0, r, self.HEIGHT * UNIT, r
            canvas.create_line(x0, y0, x1, y1)

        # 把图标加载到环境中
        self.rectangle = canvas.create_image(50, 50, image=self.shapes[0])  # 部署图标
        self.trap1 = canvas.create_image(150, 150, image=self.shapes[1])
        self.trap2 = canvas.create_image(350, 150, image=self.shapes[1])
        self.trap3 = canvas.create_image(350, 250, image=self.shapes[1])
        self.trap4 = canvas.create_image(50, 350, image=self.shapes[1])
        self.goal = canvas.create_image(350, 350, image=self.shapes[2])

        # 对环境进行包装
        canvas.pack()

        return canvas

    # def text_value(self, row, col, contents, action, font='Helvetica', size=10,
    #                style='normal', anchor="nw"):
    #     if action == 0:  # 上
    #         origin_x, origin_y = 7, 42
    #     elif action == 1:  # 下
    #         origin_x, origin_y = 85, 42
    #     elif action == 2:  # 左
    #         origin_x, origin_y = 42, 5
    #     else:  # 右
    #         origin_x, origin_y = 42, 77
    #
    #     x, y = origin_y + (UNIT * col), origin_x + (UNIT * row)
    #     font = (font, str(size), style)
    #     text = self.canvas.create_text(x, y, fill="black", text=contents,
    #                                    font=font, anchor=anchor)
    #     return self.texts.append(text)
    #
    # def print_value_all(self, q_table):
    #     for i in self.texts:
    #         self.canvas.delete(i)
    #     self.texts.clear()
    #     for i in range(self.HEIGHT):
    #         for j in range(self.WIDTH):
    #             for action in range(0, 4):
    #                 state = [i, j]
    #                 if str(state) in q_table.keys():
    #                     temp = q_table[str(state)][action]
    #                     self.text_value(j, i, round(temp, 2), action)

    def coords_to_state(self, coords):
        x = int((coords[0] - 50) / 100)
        y = int((coords[1] - 50) / 100)
        return [x, y]

    def state_to_coords(self, state):
        x = int(state[0] * 100 + 50)
        y = int(state[1] * 100 + 50)
        return [x, y]

    def reset(self):
        self.update()
        #time.sleep(0.5)
        x, y = self.canvas.coords(self.rectangle)
        self.canvas.move(self.rectangle, UNIT / 2 - x, UNIT / 2 - y)
        self.render()
        # return observation
        return self.coords_to_state(self.canvas.coords(self.rectangle))

    def step(self, action):
        state = self.canvas.coords(self.rectangle)
        base_action = np.array([0, 0])
        self.render()

        if action == 0:  # up
            if state[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:  # down
            if state[1] < (self.HEIGHT - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:  # left
            if state[0] > UNIT:
                base_action[0] -= UNIT
        elif action == 3:  # right
            if state[0] < (self.WIDTH - 1) * UNIT:
                base_action[0] += UNIT

        # 移动
        self.canvas.move(self.rectangle, base_action[0], base_action[1])
        self.canvas.tag_raise(self.rectangle)
        next_state = self.canvas.coords(self.rectangle)
        # 判断得分条件
        if next_state == self.canvas.coords(self.goal):
            reward = 1
            done = True
        elif next_state in [self.canvas.coords(self.trap1),
                            self.canvas.coords(self.trap2),
                            self.canvas.coords(self.trap3),
                            self.canvas.coords(self.trap4),]:
            reward = -1
            done = True
        else:
            reward = 0
            done = False

        next_state = self.coords_to_state(next_state)
        return next_state, reward, done
    # 渲染环境
    def render(self):
        #time.sleep(0.03)
        self.update()

    def show_route(self, q_table):

        # self.canvas.create_image((100, 100), image=self.shapes[7])
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                try:
                    cor =(i,j)
                    state = str([i, j])
                    state_action = q_table[state]
                    if cor in [(1,1),(3,1),(0,3),(3,2),(3,3)]:
                        #self.canvas.create_image(i * UNIT + 50, j * UNIT + 50, image=self.shapes[7])
                        continue
                    else:
                        max_index_list = []
                        max_value = state_action[0]
                        for index, value in enumerate(state_action):
                            if value > max_value:
                                max_index_list.clear()
                                max_value = value
                                max_index_list.append(index)
                            elif value == max_value:
                                max_index_list.append(index)
                        if max_index_list[0] == 0:
                            direction = 'up'
                            self.canvas.create_image(i * UNIT + 50, j * UNIT + 50, image=self.shapes[3])
                        elif max_index_list[0] == 1:
                            direction = 'down'
                            self.canvas.create_image(i * UNIT + 50, j * UNIT + 50, image=self.shapes[4])
                        elif max_index_list[0] == 2:
                            direction = 'left'
                            self.canvas.create_image(i * UNIT + 50, j * UNIT + 50, image=self.shapes[5])
                        else:
                            direction = 'right'
                            self.canvas.create_image(i * UNIT + 50, j * UNIT + 50, image=self.shapes[6])
                        print(direction)

                except:
                    continue

class MCAgent:
    #一个随机的pi
    #一个随机的Q表
    def __init__(self, actions,HEIGHT,WIDTH):
        # 四种动作分别用序列表示：[0, 1, 2, 3]
        self.actions = actions
        self.learning_rate = 0.01
        self.discount_factor = 0.9
        #epsilon贪婪策略取值
        self.epsilon = 0.4
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.q_table =self.init_q_table()
        self.G_table = self.init_G_table()
        self.G_dir = self.init_G_dir()
        self.R = []
        self.G = []

    def default_to_regular(self,d):
        if isinstance(d, defaultdict):
            d = {k: self.default_to_regular(v) for k, v in d.items()}
        return d

    def init_q_table(self):
        q_table = defaultdict(lambda: [0.,0.,0.,0.])
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                q_table[str([i,j])]
        q_table = self.default_to_regular(q_table)
        return q_table



    def init_G_table(self):
        G_table = defaultdict(lambda:[0.])
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                G_table[str([i,j])]
        G_table = self.default_to_regular(G_table)
        return G_table

    def init_G_dir(self):
        G_dir = defaultdict(lambda:[0.] )
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                G_dir[str([i,j])]
        return G_dir



    def init_track(self):
        self.track = []

    def record_track(self,state):
        self.track.append(str(state))

    def init_R(self):
        self.R =[]

    def record_score(self,reward):
        self.R.append(reward)


    def caculate_G(self):
        length = len(self.R)
        self.G = np.zeros(length)
        for i in range(length):
            if i == 0:
                self.G[-1] = self.R[-1]
            else:
                self.G[length-(i+1)] = self.R[length-(i+1)] + self.discount_factor * self.G[length-(i+1)+1]


    # #更新G_dir 输入状态 和 相应的值
    # def update_G_dir(self,state,value):
    #     state = str(state)
    #     self.G_dir(state).append(value)

    #将训练结果写进G_dir中
    def writein_G_dir(self):
        # self.G
        # self.R
        # self.track
        states = []
        for index in range(len(self.G)):
            if self.track[index] in states:
                continue
            else:
                states.append(self.track[index])
                self.G_dir[self.track[index]].append(self.G[index])

    def update_G_table(self):
        for key in self.G_dir:
            self.G_table[key] = np.mean(self.G_dir[key])

    def update_Q_table(self):
        for key in self.q_table:
            cor = re.findall('\d', key)
            x = int(cor[0])
            y = int(cor[1])

            try:
                self.q_table[key][0] = self.G_table[str([x, y - 1])] #上
            except KeyError:
                self.q_table[key][0] = -100.0
            try:
                self.q_table[key][1] = self.G_table[str([x, y + 1])] #下
            except KeyError:
                self.q_table[key][1] = -100.0

            try:
                self.q_table[key][2] = self.G_table[str([x - 1 , y])] #左
            except KeyError:
                self.q_table[key][2] = -100.0
            try:
                self.q_table[key][3] = self.G_table[str([x + 1, y])] #右
            except KeyError:
                self.q_table[key][3] = -100.0


    def get_action(self, state):
        if np.random.rand() < self.epsilon:
            action = np.random.choice(self.actions)
        else:
            state_action = self.q_table[state]
            action = self.arg_max(state_action)
        return action

    @staticmethod
    def arg_max(state_action):
        max_index_list = []
        max_value = state_action[0]
        for index, value in enumerate(state_action):
            if value > max_value:
                max_index_list.clear()
                max_value = value
                max_index_list.append(index)
            elif value == max_value:
                max_index_list.append(index)
        return random.choice(max_index_list)


method = 'M'#S/Q/M
HEIGHT = 4
WIDTH = 4

if method == 'M':
    env = Env(HEIGHT,WIDTH)
    agent = MCAgent(actions=list(range(env.n_actions)),HEIGHT=HEIGHT,WIDTH=HEIGHT)
    train_n = 500
    for episode in range(train_n):
        state = env.reset()
        agent.init_R()
        agent.init_track()
        while True:
            env.render()
            action = agent.get_action(str(state))
            next_state, reward, done = env.step(action)
            agent.record_score(reward)
            agent.record_track(next_state)
            state = next_state
            # env.print_value_all(agent.q_table)
            if done:
                agent.caculate_G()
                agent.writein_G_dir()
                agent.update_G_table()
                agent.update_Q_table()
                break
        print("%d training ok" % (episode + 1))
        if episode == (train_n - 1):
            print(agent.q_table)
            env.show_route(agent.q_table)
            while True:
                env.update()

