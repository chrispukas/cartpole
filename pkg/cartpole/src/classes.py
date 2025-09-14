from dataclasses import dataclass


@dataclass
class Config:
    max_epochs: int # Number of epochs to train
    max_episodes: int # Number of episodes per epoch

    learning_rate: float # Gradient descent steps
    gamma: float # Discount factor
    epsilon: float # Exploration
    epsilon_decay: float # Exploration decay rate