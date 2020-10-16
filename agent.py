import random
import pandas as pd
__all__ = [
    "MonteCarloAgent"
]

####################
# utility function #
####################
def _all_equal(actions):
    for action in actions:
        for action_ in actions:
            if actions[action] != actions[action_]:
                return False
    return True

#########
# agent #
#########
class MonteCarloAgent(object):

    #def __init__(self, act_n, gamma=0.99, epsilon=0.05): #for 10x10
    def __init__(self, act_n, gamma=0.9, epsilon=0.2): #for 4x4
        self.act_n = act_n
        self.gamma = gamma
        self.epsilon = epsilon
        self.value_q = {}
        self.value_n = {}
        self.episode = []

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
            for k, v in actions.items():
                if v == m:
                    return k

    def store(self, state, action, reward):
        self.episode.append((state, action, reward))

    def learn(self,epi):
        total_reward = 0
        for state, action, reward in reversed(self.episode):
            total_reward = reward + self.gamma * total_reward
            self.value_n[state][action] += 1
            self.value_q[state][action] += (total_reward +self.value_q[state][action])/self.value_n[state][action]
        self.episode = []
        q=self.value_q
        # df_1 = pd.DataFrame.from_dict(s, orient='index')
        # df_1.to_csv('monto_carlo.csv')
        if epi==9999:
            df_2=pd.DataFrame.from_dict(q,orient='index')
            df_2.to_csv('monto_carloq.csv')
