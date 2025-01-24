# model.py
import torch.nn as nn

class TransactionPredictor(nn.Module):
    def __init__(self, input_dim):
        super(TransactionPredictor, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Linear(32, 1)  # Output a single value (Amount)
        )

    def forward(self, x):
        return self.fc(x)