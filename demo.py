import matplotlib.pyplot as plt
from environment import Maze_carlo
from agent import MonteCarloAgent
import pandas as pd

########
# demo #
########
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
            env.render()
            if done:
                env.render()
                print('episode: {episode}, total reward: {total_reward}'.format(episode=episode, total_reward=total_reward))
                r += total_reward
                rs.append(r / (episode + 1))
                #env.render()
                agent.learn(episode)
                break
    return rs
########
# test #
########
def test_monte_carlo():
    env = Maze_carlo()
    agent = MonteCarloAgent(act_n=4)
    rs = monte_carlo_demo(env, agent, 2000)
    plt.plot(range(2000), rs), plt.grid(), plt.show()
if __name__ == "__main__":
    # env = Maze_carlo()
    # agent = MonteCarloAgent(act_n=4)
    # rs = monte_carlo_demo(env, agent, 50000)
    # plt.plot(range(50000), rs), plt.grid(), plt.show()
    env = Maze_carlo()
    x = []
    y = []
    position = []
    iteration = 10000
    agent = MonteCarloAgent(act_n=4)
    rs = monte_carlo_demo(env, agent, iteration)
    df = pd.read_csv('monto_carloq.csv')
    for i in range(df.shape[0]):
        x.append(df.iat[i, 0] + 15)
        y.append(df.iat[i, 1] + 15)
        b = [df['0'][i], df['1'][i], df['2'][i], df['3'][i]]
        position.append(b.index(max(b)))
    df['x'] = x
    df['y']=  y
    df['best'] = position
    # df = df.sort_values('y')
    df.to_csv('monto_carloq.csv')
    for i in range(df.shape[0]):
        env.show_road(df['x'][i], df['y'][i], df['best'][i])
        env.render()
    plt.plot(range(iteration), rs), plt.grid(), plt.show()
