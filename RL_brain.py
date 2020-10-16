import numpy as np
import pandas as pd
import random
from collections import defaultdict
import re
from environment2 import Maze_carlo
# __all__ = [
#     "MonteCarloAgent",
# ]
#
# def _all_equal(actions):
#     for action in actions:
#         for action_ in actions:
#             if actions[action] != actions[action_]:
#                 return False
#     return True
#
# class RL(object):
#     def __init__(self, action_space, learning_rate=0.01, reward_decay=0.99, e_greedy=0.5):
#         self.actions = action_space  # a list
#         self.lr = learning_rate
#         self.gamma = reward_decay
#         self.epsilon = e_greedy
#
#         self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
#
#     def check_state_exist(self, state):
#         if state not in self.q_table.index:
#             # append new state to q table
#             self.q_table = self.q_table.append(
#                 pd.Series(
#                     [0]*len(self.actions),
#                     index=self.q_table.columns,
#                     name=state,
#                 )
#             )
#             q_table=self.q_table
#             q_table.to_csv('q_table.csv')
#
#     def choose_action(self, observation,reward):
#         if reward==1:
#             self.epsilon=self.epsilon+0.5/5000
#
#         self.check_state_exist(observation)
#         # action selection
#         if np.random.rand() < self.epsilon:
#             # choose best action
#             state_action = self.q_table.loc[observation, :]
#             # some actions may have the same value, randomly choose on in these actions
#             action = np.random.choice(state_action[state_action == np.max(state_action)].index)
#         else:
#             # choose random action
#             action = np.random.choice(self.actions)
#         return action
#
#     def learn(self, *args):
#         pass
#
#
# # off-policy
# class QLearningTable(RL):
#     def __init__(self, actions, learning_rate=0.01, reward_decay=0.99, e_greedy=0.9):
#         super(QLearningTable, self).__init__(actions, learning_rate, reward_decay, e_greedy)
#
#     def learn(self, s, a, r, s_,a_):
#         self.check_state_exist(s_)
#         q_predict = self.q_table.loc[s, a]
#         if s_ != 'terminal':
#             q_target = r + self.gamma * self.q_table.loc[s_, :].max()  # next state is not terminal
#         else:
#             q_target = r  # next state is terminal
#         self.q_table.loc[s, a] += self.lr * (q_target - q_predict)  # update
#
#
# # on-policy
# class SarsaTable(RL):
#
#     def __init__(self, actions, learning_rate=0.1, reward_decay=0.999, e_greedy=0.5):
#         super(SarsaTable, self).__init__(actions, learning_rate, reward_decay, e_greedy)
#
#     def learn(self, s, a, r, s_, a_):
#         self.check_state_exist(s_)
#         q_predict = self.q_table.loc[s, a]
#         if s_ != 'terminal':
#             q_target = r + self.gamma * self.q_table.loc[s_, a_]  # next state is not terminal
#         else:
#             q_target = r  # next state is terminal
#         self.q_table.loc[s, a] += self.lr * (q_target - q_predict)  # update
#
# class MonteCarloAgent(object):
#
#     #def __init__(self, act_n, gamma=0.99, epsilon=0.05): #for 10x10
#     def __init__(self, act_n, gamma=0.99, epsilon=0.1): #for 4x4
#         self.act_n = act_n
#         self.gamma = gamma
#         self.epsilon = epsilon
#         self.value_q = {}
#         self.value_n = {}
#         self.episode = []
#
#     def _initialize_state(self, state):
#         if state not in self.value_q:
#             self.value_q[state] = {a: 0.0 for a in range(self.act_n)}
#             self.value_n[state] = {a: 0.0 for a in range(self.act_n)}
#
#     def choose(self, state):
#         self._initialize_state(state)
#         actions = self.value_q[state]
#         if random.random() < self.epsilon or _all_equal(actions):
#             return random.choice(range(self.act_n))
#         else:
#             m = max(actions.values())
#             for k, v in actions.items():
#                 if v == m:
#                     return k
#
#     def store(self, state, action, reward):
#         self.episode.append((state, action, reward))
#
#     def learn(self):
#         total_reward = 0
#         for state, action, reward in reversed(self.episode):
#             total_reward = reward + self.gamma * total_reward
#             self.value_n[state][action] += 1
#             self.value_q[state][action] += (total_reward - self.value_q[state][action]) / self.value_n[state][action]
#         self.episode = []
#
# # class monte_carlo(RL):
# #     def __init__(self,actions,learning_rtate=0.01,reward_decay=0.99,e_greedy=0.9):
# #         super(monte_carlo, self).__init__(actions, learning_rate, reward_decay, e_greedy)
# #     def learn(self,):
all=["MonteCarlo"]
def _all_equal(actions):
    for action in actions:
        for action_ in actions:
            if actions[action] !=actions[action_]:
                return False

class RL_double(object):
    def __init__(self,action_space,learning_rate,reward_decay,greddy_p):
        self.actions=action_space
        self.lr=learning_rate
        self.gamma=reward_decay
        self.epsilon=greddy_p
        self.q_table=pd.DataFrame(columns=self.actions)#,dtype=np.float64)
    def check_state_exist(self,state): #check if there is any state existing or not
        if state not in self.q_table.index:
            self.q_table=self.q_table.append(pd.Series([0]*len(self.actions),index=self.q_table.columns,name=state))
    def choose_action(self,observation,reward):
        if reward==1:
            self.epsilon=self.epsilon+0.1/2000
            #self.lr=self.lr-0.09/3000
        self.check_state_exist(observation)
        if np.random.rand()<self.epsilon:
            state_action=self.q_table.loc[observation,:]
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
        else:
            action=np.random.choice(self.actions)
        return action
    def learn(selfself,*args):
        pass
class QlearningTable(RL_double):
    def __init__(self,actions,learning_rate=0.01,reward_decay=0.99,greddy_p=0.9):
        super(QlearningTable,self).__init__(actions,learning_rate,reward_decay,greddy_p)
    def learn(self,s,a,r,s_1,a_1,epi):
        self.check_state_exist(s_1)
        q_predict=self.q_table.loc[s,a]
        if s_1 !='terminal':
            q_target=r+self.gamma*self.q_table.loc[s_1,:].max()
        else:
            q_target=r
        self.q_table.loc[s,a] +=self.lr*(q_target-q_predict)
        if epi%500==0:
            self.q_table.to_csv('qlearning.csv',index='s')
class SarsaTablle(RL_double):
    # def __init__(self,actions,learning_rate=0.1,reward_decay=0.99,greddy_p=0.5):
    #     super(SarsaTablle,self).__init__(actions,learning_rate,reward_decay,greddy_p)
    def __init__(self,actions,learning_rate=0.1,reward_decay=0.99,greddy_p=0.6):
        super(SarsaTablle,self).__init__(actions,learning_rate,reward_decay,greddy_p)
    def learn(self,s,a,r,s_1,a_1,epi):
        self.check_state_exist(s_1)
        q_predict=self.q_table.loc[s,a]
        if s_1 !='terminal':
            q_target=r+self.gamma*self.q_table.loc[s_1,a_1]
        else:
            q_target=r
        self.q_table.loc[s,a]+=self.lr*(q_target-q_predict)
        if epi%500==0:
            self.q_table.to_csv('sarsa.csv')
#---------------   this is for qlearning and sarsa
class MonteCarloAgent(object):

    #def __init__(self, act_n, gamma=0.99, epsilon=0.05): #for 10x10
    def __init__(self, act_n, gamma=0.99, epsilon=0.1): #for 4x4
        self.act_n = act_n
        self.gamma = gamma
        self.epsilon = epsilon
        self.value_q = {}
        self.value_n = {}
        self.episode = []
        self.n=0
        self.storein=[]

    def _initialize_state(self, state):
        if state not in self.value_q:
            self.value_q[state] = {a: 0.0 for a in range(self.act_n)}
            self.value_n[state] = {a: 0.0 for a in range(self.act_n)}

    def choose(self, state):
        self._initialize_state(state)
        actions = self.value_q[state]
        if random.random() < self.epsilon or _all_equal(actions):
            return random.choice(range(self.act_n))
        else:
            m = max(actions.values())
            #print(actions.items())
            for k, v in actions.items():
                if v == m:
                    self.storein.append(k)
                else:
                    pass

            return random.choice(self.storein)

    def store(self, state, action, reward):
        self.episode.append((state, action, reward))

    def learn(self):
        total_reward = 0
        for state, action, reward in reversed(self.episode):
            total_reward = reward + self.gamma * total_reward
            self.value_n[state][action] += 1
            self.value_q[state][action] += (total_reward - self.value_q[state][action]) / self.value_n[state][action]
        self.episode = []
        q=self.value_q
        # df_1 = pd.DataFrame.from_dict(s, orient='index')
        # df_1.to_csv('monto_carlo.csv')
        df_2=pd.DataFrame.from_dict(q,orient='index')
        df_2.to_csv('monto_carloq.csv')


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
