import torch.nn as nn

class BlockchainModel(nn.Module):
    def __init__(self):
        super(BlockchainModel, self).__init__()
        self.embedding = nn.Embedding(10, 16) # 10 wallet-nodes, 16 dimension-features
        self.fc = nn.Linear(16, 1)

    def forward(self, source, target):
        source_embed = self.embedding(source)
        target_embed = self.embedding(target)
        combined = source_embed + target_embed
        return self.fc(combined)

model = BlockchainModel()