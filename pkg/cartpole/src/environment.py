import gymnasium as gym


class Environment():
    def __init__(self,
                 env_name: str = "CartPole-v1",
                 render_mode: str = "human") -> None:
        self.env = gym.make(env_name, render_mode=render_mode)

    def reset(self):
        self.env.reset()

    def step(self, action):
        return self.env.step(action)


class CartPole(Environment):
    def __init__(self):
        self.env_name: str = "CartPole-v1"
        self.render_mode: str = "human"

        super().__init__(env_name=self.env_name, 
                         render_mode=self.render_mode)
        
        