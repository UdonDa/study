import random
from environment import Environment

class Agent():
    def __init__(self, env):
        self.actions= env.actions

    def policy(self, state):
        return random.choice(self.actions)



def main():
    grid = [
        [0, 0, 0, 1],
        [0, 9, 0, -1],
        [0, 0, 0, 0]
    ]
    env = Environment(grid)
    agent = Agent(env)


    for i in range(10):
        state = env.reset()
        total_reward = 0
        is_done = False
        while not is_done:
            action = agent.policy(state)
            next_state, reward, is_done = env.step(action)
            # print(reward)
            total_reward += reward
            state = next_state
        print("Episode {}: Agent gets {:.4f} reward.".format(i, total_reward))


if __name__ == "__main__":
    main()