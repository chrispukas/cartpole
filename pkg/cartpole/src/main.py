import torch

import cartpole.src.environment as envs
from cartpole.src.classes import Config

def run_cartpole(cfg: Config):
    cartpole = envs.CartPole()

    for i in range(cfg.max_epochs):
        epoch(cartpole, cfg)


def epoch(cartpole: envs.CartPole, 
          cfg: Config):
    cartpole.reset()
    for i in range(cfg.max_episodes):
        episode(cartpole, cfg)

# REINFORCE policy first, collect all data then pass in final outcome

def episode(cartpole: envs.CartPole, 
            cfg: Config):
    pass


def calculate_total_returns(rewards: torch.Tensor, 
                            gamma: torch.Tensor) -> torch.Tensor:
    total_return: torch.Tensor = torch.zeros_like(rewards, dtype=torch.float32)
    total_return[0] = rewards[0]

    for i, reward in enumerate(rewards):
        if i == 0:
            continue
        total_return[i] = (gamma**i) * reward + total_return[i - 1]
    return total_return



rewards = torch.tensor([1., 1., 1., 1.], dtype=torch.float32)
print(calculate_total_returns(rewards, 0.9))