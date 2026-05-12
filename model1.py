import torch
import torch.nn as nn

class Model1(nn.Module):

    def __init__(self):

        super().__init__()

        self.network = nn.Sequential(

            nn.Linear(4, 64),
            nn.ReLU(),

            nn.Linear(64, 128),
            nn.ReLU(),

            nn.Linear(128, 3)
        )

    def forward(self, x):

        return self.network(x)