from maze_env import Maze,Maze_info
#from RL_brain import SarsaTable,QLearningTable,MonteCarloAgent
from RL_brain import SarsaTablle,QlearningTable,RL_double,MonteCarloAgent,MCAgent
import matplotlib.pyplot as plt
import pandas as pd
from Monto_carlo_environment import Env
#from environment import Maze_carlo
from environment2 import Maze_carlo



def update(iteration):#main programme, for every single step
    r,rs,re=0,[],[]
    count = 0
    episode_show=100
    for episode in range(iteration):
        total_reward=0
        # initial observation
        observation = env.reset()
        reward=0
        # RL choose action based on observation
        action = RL_double.choose_action(str(observation),reward)
        #env.render()
        while True:
            # fresh env
            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL choose action based on next observation
            action_ = RL_double.choose_action(str(observation_),reward)

            # RL learn from this transition (s, a, r, s, a) ==> Sarsa
            RL_double.learn(str(observation), action, reward, str(observation_), action_,episode)

            # swap observation and action
            observation = observation_
            action = action_

            # break while loop when end of this episode
            total_reward+=reward
            if done:
                #env.render()

                r+=total_reward
                rs.append(r / (episode + 1))
                re.append(reward)
                count = count + 1
                print(count)
                print(reward)
                break

    # end of game
    print('game over')
    #env.destroy()
    return rs,re

def monte_carlo_demo(env, agent, episodes):
    r, rs = 0, []
    for episode in range(episodes):
        total_reward = 0
        state = env.reset()
        while True:
            #env.render()
            action = agent.choose(state)
            state_, reward, done = env.step(action)
            agent.store(state, action, reward)
            state = state_
            total_reward += reward
            if done:
                env.render()
                print('episode: {episode}, total reward: {total_reward}'.format(episode=episode, total_reward=total_reward))
                r += total_reward
                rs.append(r / (episode + 1))
                env.render()
                agent.learn()
                break
    return rs
if __name__ == "__main__":
    method_choose= 2 # 1 is qlearning and 2 is Sarsa,3 is monto_carlo with normal reward, 4 is monto carlo with innormal reward
    x=[]
    y=[]
    del_index=[]
    position=[]
    iteration=600

    if method_choose==1:
        env = Maze()
        env2 = Maze_info()
        RL_double = QlearningTable(actions=list(range(env.n_actions)))
        name='qlearning'
    elif method_choose==2:
        env = Maze()
        env2 = Maze_info()
        RL_double = SarsaTablle(actions=list(range(env.n_actions)))
        name='sarsa'
    elif method_choose==3:
        HEIGHT=10
        WIDTH=10
        env=Env(HEIGHT,WIDTH)
    elif method_choose==4:
        env = Maze_carlo()
        x = []
        y = []
        position = []

    #rs=update()
    #plt.plot(range(700), rs), plt.grid(), plt.show()
    if method_choose==1 or method_choose==2:
        rs,re=update(iteration)
        df = pd.read_csv('%s.csv'%name)
        for i in range(df.shape[0]):
            if df.iat[i, 0] == 'terminal':
                x.append(0)
                y.append(0)
                position.append(0)
                continue
            else:
                a = df.iat[i, 0]
                a = a.replace('.0', '').replace('[', '').replace(']', '').replace(' ', '')
                l = list(map(int, a.split(',')))
                x.append(l[0])
                y.append(l[1])
                b = [df['0'][i], df['1'][i], df['2'][i], df['3'][i]]
                position.append(b.index(max(b)))
        df['x'] = x
        df['y'] = y
        df['best'] = position
        df = df.sort_values('y')
        # for j in range(df.shape[0]):
        #     if df.iat[j, 0] == 'terminal':
        #         del_index.append(j)
        # df = df.drop(index=0)
        df.to_csv('%s.csv'%name, index=False)
        df=pd.read_csv('%s.csv'%name)
        env2.print_value_all(df)
        for i in range(1,df.shape[0]):
             # if df.iat[i,1]==0:
             #     continue
            # else:
            # env.print_value_all(df)
            env.show_road(df.iat[i,5],df.iat[i,6],df.iat[i,7])
            env.render()
        print(rs)
        plt.plot(range(iteration), rs), plt.grid(), plt.show()
        plt.plot(range(iteration), re), plt.grid(), plt.show()
    elif method_choose==3:
        agent = MCAgent(actions=list(range(env.n_actions)), HEIGHT=HEIGHT, WIDTH=HEIGHT)
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
                env.print_value_all(agent.q_table)
                env.show_route(agent.q_table)
                while True:
                    env.update()
    elif method_choose==4:
        agent = MonteCarloAgent(act_n=4)
        rs = monte_carlo_demo(env, agent, iteration)
        df = pd.read_csv('monto_carloq.csv')
        for i in range(df.shape[0]):
            x.append(df.iat[i, 0] + 15)
            y.append(df.iat[i, 1] + 15)
            b = [df['0'][i], df['1'][i], df['2'][i], df['3'][i]]
            position.append(b.index(max(b)))
        df['y'] = y
        df['x'] = x
        df['best'] = position
        # df = df.sort_values('y')
        df.to_csv('monto_carloq.csv')
        for i in range(df.shape[0]):
            env.show_road(df['x'][i], df['y'][i], df['best'][i])
            env.render()

        plt.plot(range(iteration), rs), plt.grid(), plt.show()


    #env.after(500, update)
    #env.mainloop()

# if __name__ == "__main__":
#     env = Maze_carlo()
#     x=[]
#     y=[]
#     position=[]
#     iteration=10000
#     agent = MonteCarloAgent(act_n=4)
#     rs = monte_carlo_demo(env, agent, iteration)
#     df=pd.read_csv('monto_carloq.csv')
#     for i in range(df.shape[0]):
#         x.append(df.iat[i,0]+15)
#         y.append(df.iat[i,1]+15)
#         b = [df['0'][i], df['1'][i], df['2'][i], df['3'][i]]
#         position.append(b.index(max(b)))
#     df['y']=y
#     df['x']=x
#     df['best']=position
#    # df = df.sort_values('y')
#     df.to_csv('monto_carloq.csv')
#     for i in range(df.shape[0]):
#         env.show_road(df['x'][i], df['y'][i], df['best'][i])
#         env.render()
#
#     plt.plot(range(iteration), rs), plt.grid(), plt.show()